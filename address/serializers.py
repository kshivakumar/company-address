"""Serializers"""

from rest_framework import serializers

from .models import CompanyAddress


class CompanyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAddress
        fields = (
            'id',
            'company_name',
            'building_number',
            'postal_code',
            'locality',
            'city',
            'state',
        )
