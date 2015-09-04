import logging
import kalibro_client

from colab.plugins.data import PluginDataImporter

from .models import MezuroRepository

from kalibro_client.processor import Repository


LOGGER = logging.getLogger('colab_mezuro')



class MezuroDataImporter(PluginDataImporter):
    app_label = 'colab_mezuro'

    def __init__(self, *arg, **kwargs):
        super(MezuroDataImporter, self).__init__(*arg, **kwargs)
        kalibro_client.configure(self.config.get('extra').get('processor_address'), self.config.get('extra').get('configurations_address'))

    def get_plugin_model_instance(self, plugin_model_class, kalibro_model_instance):
        plugin_model = plugin_model_class()

        for attribute, value in kalibro_model_instance._asdict().iteritems():
            if hasattr(plugin_model, attribute):
                setattr(plugin_model, attribute, value)

        return plugin_model

class MezuroRepositoryImporter(MezuroDataImporter):
    def fetch_data(self):
        for repository in Repository.all():
            mezuro_repository = self.get_plugin_model_instance(MezuroRepository, repository)

            # These attributes are not part of _asdict()
            mezuro_repository.id = repository.id
            mezuro_repository.created_at = repository.created_at
            mezuro_repository.updated_at = repository.updated_at

            mezuro_repository.save()
