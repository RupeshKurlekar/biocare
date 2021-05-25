from rest_framework import serializers
from .models import Super


class SuperListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Super
        exclude = ['SUPER_PASSWORD']


class SuperSerializers(serializers.ModelSerializer):
    class Meta:
        model = Super
        exclude = ['SUPER_ID']