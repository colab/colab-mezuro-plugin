
from colab.plugins.utils.apps import ColabPluginAppConfig


class MezuroPluginAppConfig(ColabPluginAppConfig):
    name = 'colab_mezuro'
    verbose_name = 'Mezuro Plugin'
    namespace = 'mezuro'
