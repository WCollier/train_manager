from django.shortcuts import render
from django.views import generic

from .models import Collection, ModelTrain

class IndexView(generic.ListView):
    template_name = 'manager/index.html'

    context_object_name = 'collection_list'

    def get_queryset(self):
        """Return all the models (for now)"""
        return Collection.objects.all()