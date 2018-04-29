from collections import Counter
import random
from django.contrib.auth.models import User
from jchart import Chart
from jchart.config import DataSet

from .models import ModelTrain

class ManufacturerChart(Chart):
    chart_type = 'pie'

    responsive = False

    def set_owner(self, owner):
        self.owner = owner

    def get_labels(self, *args, **kwargs):
        models = ModelTrain.objects.filter(owner=self.owner)

        # Convert the query set to a list
        return models.values_list('manufacturer', flat=True)[::1]

    def get_datasets(self, *args, **kwargs):
        data = self.generate_data()

        colours = list(map(lambda col: self.random_colour(), data))

        # Convert the query set to a list
        return [DataSet(data=data, backgroundColor=colours)]

    def generate_data(self):
        models = ModelTrain.objects.filter(owner=self.owner)

        list_of_manufacturers = [manufacturer for manufacturer in models.values_list('manufacturer', flat=True)[::1]]

        counted = Counter(list_of_manufacturers)

        counted_values = counted.values()

        sum_of_counted = sum(counted_values) 

        return list(map(lambda value: value * 100.0 / sum_of_counted, counted_values))

    def random_colour(self):
        return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))