from django.utils.translation import ugettext_lazy as _
from colab.plugins.utils.menu import colab_url_factory

name = 'colab_mezuro'
verbose_name = 'Mezuro Plugin'

upstream = 'http://localhost:3000/mezuro/'
#middlewares = []

urls = {
    'include': 'colab_mezuro.urls',
    'prefix': '^mezuro/',
}

menu_title = _('Code Quality')

url = colab_url_factory('mezuro')

menu_urls = (
    url(display=_('Projects'), viewname='mezuro',
        kwargs={'path': 'projects'}, auth=False),
    url(display=_('Repositories'), viewname='mezuro',
        kwargs={'path': 'repositories'}, auth=False),
    url(display=_('Configurations'), viewname='mezuro',
        kwargs={'path': 'kalibro_configurations'}, auth=False),
    url(display=_('Reading Groups'), viewname='mezuro',
        kwargs={'path': 'reading_groups'}, auth=False),
)
