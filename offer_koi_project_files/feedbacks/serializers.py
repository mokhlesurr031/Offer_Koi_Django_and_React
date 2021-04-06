from rest_framework import serializers
from .models import UserFeedbacks


class UserFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedbacks

        fields = ['feedback', 'offer_id']
