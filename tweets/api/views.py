
from rest_framework import generics
from tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    # pagination_class = StandardResultsPagination

    def get_queryset(self):
        return Tweet.objects.all()

    # def get_serializer_context(self, *args, **kwargs):
    #     context = super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
    #     context['request'] = self.request
    #     return context