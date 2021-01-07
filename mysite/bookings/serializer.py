from rest_framework import serializers
from .models import Reservation, ReservedTable, LastVisit


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class ReservedTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservedTable
        fields = '__all__'


class LastVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastVisit
        fields = '__all__'
