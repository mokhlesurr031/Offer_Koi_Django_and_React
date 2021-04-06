from rest_framework import serializers
from .models import Offers


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers

        fields = ['name', 'image', 'discount_type', 'discount_amount', 'start_date', 'end_date', 'shop_id']
