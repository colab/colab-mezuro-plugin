
import datetime

from . import data
from kalibro_client.processor import Repository
from colab_mezuro.data_importer import MezuroRepositoryImporter
from colab_mezuro.models import MezuroRepository
from django.test import TestCase, Client
from mock import patch


class MezuroTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.data_importer = MezuroRepositoryImporter()

    def test_get_plugin_model_instance(self):
        model = self.data_importer.get_plugin_model_instance(MezuroRepository,
                                                             data.repository)
        self.assertEquals(model.id, 1)
        self.assertEquals(model.name, 'repository name')
        self.assertEquals(model.address, 'https://github.com/repository-name')
        self.assertEquals(model.created_at,
                          datetime.datetime(2015, 9, 7, 18, 20, 18, 888000))
        self.assertEquals(model.updated_at,
                          datetime.datetime(2015, 9, 7, 18, 20, 18, 888000))

    @patch.object(Repository, 'all')
    def test_fetch_data(self, mock_obj):
        mock_obj.side_effect = [data.repositories]

        before = MezuroRepository.objects.all()
        self.data_importer.fetch_data()
        after = MezuroRepository.objects.all()

        assert mock_obj.called
        self.assertGreater(after, before)
