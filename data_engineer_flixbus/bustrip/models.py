# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BusTrip(object):

    def __init__(self, trip_id, departure_datetime, time_in_hours, n_connections, distance, price):
        self.trip_id = trip_id
        self.departure_datetime = departure_datetime
        self.time_in_hours = time_in_hours
        self.n_connections = n_connections  # if multiple buses
        self.distance = distance
        self.price = price

    def __str__(self):
        return str(self.trip_id)
