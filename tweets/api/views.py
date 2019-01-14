
from rest_framework import generics
from django.db.models import Q
from tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    # pagination_class = StandardResultsPagination


    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user_id__username__icontains=query)
                    )
        return qs    

    # def get_serializer_context(self, *args, **kwargs):
    #     context = super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
    #     context['request'] = self.request
    #     return context