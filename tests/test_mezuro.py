
from django.test import TestCase, Client


class MezuroTest(TestCase):

    def setUp(self):
        self.client = Client()
