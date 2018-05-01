"""
The module which represents the charts
"""

import random

from collections import Counter
from jchart import Chart
from jchart.config import DataSet

from .models import ModelTrain, Collection

class ManufacturerChart(Chart):
    """
    The chart which represents the percentage of manufacturers in the collections
    """

    chart_type = 'pie'

    responsive = False

    def __init__(self, owner):
        self.models = ModelTrain.objects.filter(owner=owner)

        self.manufacturer_list = self.models.values_list('manufacturer', flat=True)[::1]

        self.percentage = calculate_percentage(self.manufacturer_list)

        self.ordered_list = self.percentage[0]

        self.data = self.percentage[1]

        super().__init__()

    def get_labels(self, *args, **kwargs):
        # Remove the duplicates from the manufacturer list
        return self.ordered_list 

    def get_datasets(self, *args, **kwargs):
        colours = list(map(lambda col: random_colour(), self.data))

        # Convert the query set to a list
        return [DataSet(data=self.data, backgroundColor=colours)]


class TractionChart(Chart):
    """
    This chart represents the different types of traction owned by the user
    """

    chart_type = 'pie'

    responsive = False

    def __init__(self, owner):
        self.models = ModelTrain.objects.filter(owner=owner)

        self.traction_list = self.models.values_list('traction', flat=True)[::1]

        self.percentage = calculate_percentage(self.traction_list)

        self.ordered_list = self.percentage[0]

        self.data = self.percentage[1]

        super().__init__()

    def get_labels(self, *args, **kwargs):
        return self.ordered_list

    def get_datasets(self, *args, **kwargs):
        colours = list(map(lambda col: random_colour(), self.data))

        # Convert the query set to a list
        return [DataSet(data=self.data, backgroundColor=colours)]

    def generate_data(self):
        """
        This function calculates a percentage from a list of repeated items
        """

        return calculate_percentage(self.traction_list)

class ScaleChart(Chart):
    """
    This chart represents the different types of scale owned by the user
    """

    chart_type = 'pie'

    responsive = False

    def __init__(self, owner):
        self.models = ModelTrain.objects.filter(owner=owner)

        self.scales_list = self.models.values_list('scale', flat=True)[::1]

        self.percentage = calculate_percentage(self.scales_list)

        self.ordered_list = self.percentage[0]

        self.data = self.percentage[1]

        super().__init__()

    def get_labels(self, *args, **kwargs):
        # Get the tuple, remove duplicates and convert to list
        return self.ordered_list

    def get_datasets(self, *args, **kwargs):
        colours = list(map(lambda col: random_colour(), self.data))

        # Convert the query set to a list
        return [DataSet(data=self.data, backgroundColor=colours)]

    def generate_data(self):
        """
        This function calculates a percentage from a list of repeated items
        """

        list_of_scales = self.models.values_list('scale', flat=True)[::1]

        return calculate_percentage(list_of_scales)

class CollectionChart(Chart):
    """
    This chart represents the number of trains in each collection
    """

    chart_type = 'bar'

    def __init__(self, owner):
        self.collections = Collection.objects.filter(owner=owner)

        self.collections_list = self.collections.values_list('name', flat=True)[::1]

        super().__init__()

    def get_labels(self, *args, **kwargs):
        return self.collections_list

    def get_datasets(self, *args, **kwargs):
        data = self.generate_data()

        colours = list(map(lambda col: random_colour(), data))

        # Convert the query set to a list
        return [DataSet(label='Number of Models Per Collection',
                        data=data,
                        backgroundColor=colours)]

    def generate_data(self):
        """
        This function calculates a percentage from a list of repeated items
        """

        return list(map(lambda collec: collec.trains.count(), self.collections))

def calculate_percentage(items):
    """
    This function takes a list of repeated items, the values are counted,
    then converted to a percentage
    """

    counted = Counter(items)

    counted_values = counted.values()

    sum_of_counted = sum(counted_values)

    return (list(counted.keys()), list(map(lambda value: (value * 100.0 // sum_of_counted), counted_values)))


def random_colour():
    """
    This function generates a random hexadecimal number
    """

    return '#%02X%02X%02X' % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255))
