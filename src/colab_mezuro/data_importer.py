import logging

from .models import MezuroRepository
from colab.plugins.data import PluginDataImporter
import kalibro_client
from kalibro_client.processor import Repository


LOGGER = logging.getLogger('colab_mezuro')


class MezuroDataImporter(PluginDataImporter):
    app_label = 'colab_mezuro'

    def __init__(self, *arg, **kwargs):
        super(MezuroDataImporter, self).__init__(*arg, **kwargs)
        kalibro_client.configure(
            self.config.get('extra').get('processor_address'),
            self.config.get('extra').get('configurations_address')
        )

    def get_plugin_model_instance(self, plugin_model_class,
                                  kalibro_model_instance):
        plugin_model = plugin_model_class()

        for attribute, value in kalibro_model_instance._asdict().iteritems():
            if hasattr(plugin_model, attribute):
                setattr(plugin_model, attribute, value)

            # These attributes are not part of _asdict()
            plugin_model.id = kalibro_model_instance.id
            plugin_model.created_at = kalibro_model_instance.created_at
            plugin_model.updated_at = kalibro_model_instance.updated_at

        return plugin_model


class MezuroRepositoryImporter(MezuroDataImporter):
    def fetch_data(self):
        for repository in Repository.all():
            mezuro_repo = self.get_plugin_model_instance(MezuroRepository,
                                                         repository)
            mezuro_repo.save()
