
from colab.plugins.utils.apps import ColabPluginAppConfig


class MezuroPluginAppConfig(ColabPluginAppConfig):
    name = 'colab_mezuro'
    namespace = 'mezuro'
    shortname = 'mezuro'
    verbose_name = 'Mezuro Plugin'
