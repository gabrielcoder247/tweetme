
from django.contrib.auth import get_user_model
# from django.urls import reverse_lazy
from tweets.models import Tweet # from ..models import Tweet

from rest_framework import serializers


User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    # follower_count = serializers.SerializerMethodField()
    # url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            # 'follower_count',
            # 'url',
            # 'email',
        ]

