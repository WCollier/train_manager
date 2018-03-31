from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Collection, ModelTrain

class IndexView(generic.ListView):
    model = Collection

    template_name = 'manager/index.html'

    context_object_name = 'collection_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            #return Collection.objects.filter(owner=self.request.user)
            return Collection.objects.all()

        else:
            return Collection.objects.none()