"""
The module for the manager app's administration interface
"""

from django.contrib import admin

from .models import ModelTrain, Collection, CollectionTrain

admin.site.register(ModelTrain)

admin.site.register(Collection)

admin.site.register(CollectionTrain)
