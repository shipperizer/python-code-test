from datetime import datetime, timedelta

from django.test import TestCase, Client
from stream.models import Stream


class StreamTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_streams_older_first(self):
        s1 = Stream(user_id=1, created_at=datetime.now())
        s2 = Stream(user_id=1, created_at=(datetime.now()-timedelta(days=3, milliseconds=4)))
        s1.save()
        s2.save()

        response = self.client.get('/stream/')

        assert response.status_code == 200
        assert response.context['streams'][0] == s2
        assert response.context['streams'][1] == s1
