from rest_framework import serializers

import models


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = ('name', 'abbreviation')


class ParkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Park
        country = CountrySerializer()
        fields = ('id', 'name', 'active', 'country', 'location')


class RollerCoasterSerializer(serializers.ModelSerializer):

    park = ParkSerializer()
    class Meta:
        model = models.RollerCoaster
        fields = ('id', 'name', 'year_opened', 'manufacturer', 'active', 'park')


class Manufacturer(serializers.ModelSerializer):

    class Meta:
        model = models.Manufacturer
        fields = ('id', 'name', 'verbose_name')
