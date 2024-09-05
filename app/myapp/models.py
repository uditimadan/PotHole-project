from django.db import models
from django.forms import ModelForm

# Create your models here.

# Report signals every time a report is made (like every individual pot hole)
class Report(models.Model):
    address = models.CharField(max_length=100)
    date = models.DateField()
    image = models.JSONField(null=True)
    coordinates = models.CharField(max_length=100)

# For every unit (as in like an area thats of high severity, one block?)
# Has an address range, a severity score, and an array of images
class Unit(models.Model):
    severity = models.FloatField(default=0.0)
    images = models.JSONField(null=True)
    frequency = models.IntegerField(default=0)
    flow_count = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    radius_m = models.FloatField(null=True)

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['address', 'date', 'image', 'coordinates']

class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['severity', 'images', 'frequency', 'flow_count', 'address', 'radius_m']
    def __init__(self, *args, **kwargs):
        super(UnitForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False