from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# Create your tests here.


from .models import Tweet


User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username='gabrielcoder247')

    def test_tweet_item(self):
        obj = Tweet.objects.create(
                user= User.objects.first(),
                content='Some random content'
            )
        self.assertTrue(obj.content == "Some random content")
        self.assertTrue(obj.id == 1)
        #self.assertEqual(obj.id, 1)