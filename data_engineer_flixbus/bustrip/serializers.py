from rest_framework import serializers
from models import BusTrip


class BusTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTrip
        fields = ('trip_id', 'departure_datetime', 'time_in_hours', 'n_connections', 'distance', 'price')

    trip_id = serializers.IntegerField()
    departure_datetime = serializers.DateTimeField()
    time_in_hours = serializers.IntegerField()
    n_connections = serializers.IntegerField(default=0)
    distance = serializers.IntegerField()
    price = serializers.IntegerField()
