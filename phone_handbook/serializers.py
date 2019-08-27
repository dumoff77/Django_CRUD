
from rest_framework import serializers
from phone_handbook.models import HandBook


class HandBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = HandBook
        fields = ("full_name", "number", "description")