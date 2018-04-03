from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Collection, ModelTrain

# pylint: disable=too-many-ancestors

class IndexView(ListView):
    model = Collection

    template_name = 'manager/index.html'

    context_object_name = 'collection_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Collection.objects.filter(owner=self.request.user)

        return Collection.objects.none()

class ModelTrains(LoginRequiredMixin, ListView):
    model = ModelTrain

    template_name = 'manager/modeltrains.html'

    context_object_name = 'model_trains'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return ModelTrain.objects.all()

class ModelTrainDetail(LoginRequiredMixin, DetailView):
    model = ModelTrain

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    fields = ['name', 'manufacturer', 'model_class', 'traction', 'scale', 'era']

class ModelTrainCreate(LoginRequiredMixin, CreateView):
    model = ModelTrain

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    fields = ['name', 'manufacturer', 'model_class', 'traction', 'scale', 'era']

class ModelTrainUpdate(LoginRequiredMixin, UpdateView):
    model = ModelTrain

    success_url = reverse_lazy('model-trains')

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    fields = ['name', 'manufacturer', 'model_class', 'traction', 'scale', 'era']

class ModelTrainDelete(LoginRequiredMixin, DeleteView):
    model = ModelTrain

    success_url = reverse_lazy('index')

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class Collections(LoginRequiredMixin, ListView):
    model = Collection

    template_name = 'manager/collections.html'

    context_object_name = 'collections'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Collection.objects.all()

class CollectionsDetail(LoginRequiredMixin, DetailView):
    model = Collection

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    fields = ['name', 'description', 'trains']
