from django import forms
from django.contrib.gis.forms import PointField
from leaflet.forms.widgets import LeafletWidget

class LocationForm(forms.Form):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())