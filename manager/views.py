from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelChoiceField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet

from .models import Collection, ModelTrain, CollectionTrain
from .charts import ManufacturerChart

# pylint: disable=too-many-ancestors

class IndexView(TemplateView):
    model = ModelTrain

    template_name = 'manager/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['models'] = ModelTrain.objects.filter(owner=self.request.user)

            manufacturer_chart = ManufacturerChart()

            manufacturer_chart.set_owner(self.request.user)

            context['manufactuter_chart'] = manufacturer_chart

        else:
            context['collections'] = Collection.objects.none()

        return context

class ModelTrains(LoginRequiredMixin, ListView):
    model = ModelTrain

    template_name = 'manager/modeltrains.html'

    context_object_name = 'model_trains'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return ModelTrain.objects.filter(owner=self.request.user.id)

class ModelTrainDetail(LoginRequiredMixin, DetailView):
    model = ModelTrain

    fields = ['name', 'manufacturer', 'model_class', 'traction', 'scale', 'era']

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class ModelTrainCreate(LoginRequiredMixin, CreateView):
    model = ModelTrain

    fields = ['name', 'manufacturer', 'model_class', 'traction', 'scale', 'era']

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)

class ModelTrainUpdate(LoginRequiredMixin, UpdateView):
    model = ModelTrain

    success_url = reverse_lazy('model-trains')

    fields = ['name', 'manufacturer', 'model_class', 'traction', 'scale', 'era']

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class ModelTrainDelete(LoginRequiredMixin, DeleteView):
    model = ModelTrain

    success_url = reverse_lazy('model-trains')

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class CollectionTrainInline(InlineFormSet):
    model = CollectionTrain

    fields = '__all__'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class Collections(LoginRequiredMixin, ListView):
    model = Collection

    template_name = 'manager/collections.html'

    context_object_name = 'collections'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user.id)

class CollectionsDetail(LoginRequiredMixin, DetailView):
    model = Collection

    fields = ['name', 'description', 'trains']

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class CollectionCreate(LoginRequiredMixin, CreateWithInlinesView):
    model = Collection

    inlines = [CollectionTrainInline]

    fields = ['name', 'description']

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def forms_valid(self, form, inlines):
        form.instance.owner = self.request.user

        return super().form_valid(form)

class CollectionsUpdate(LoginRequiredMixin, UpdateWithInlinesView):
    model = Collection 

    inlines = [CollectionTrainInline]

    fields = ['name', 'description']

    success_url = reverse_lazy('collections')

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class CollectionsDelete(LoginRequiredMixin, DeleteView):
    model = Collection 

    success_url = reverse_lazy('collections')

    login_url = '/login/'

    redirect_field_name = 'redirect_to'