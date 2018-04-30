"""
The module for the manager app's views
"""

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Collection, ModelTrain
from .forms import CollectionForm
from .charts import ManufacturerChart, TractionChart, ScaleChart, CollectionChart

# pylint: disable=too-many-ancestors

class IndexView(TemplateView):
    """
    The view which represents the index (/)
    """

    model = ModelTrain

    template_name = 'manager/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['models'] = ModelTrain.objects.filter(owner=self.request.user)

            context['user'] = self.request.user

        else:
            context['collections'] = Collection.objects.none()

        return context

class ModelTrains(LoginRequiredMixin, ListView):
    """
    This class represents a model train within the database
    """

    model = ModelTrain

    template_name = 'manager/modeltrains.html'

    context_object_name = 'model_trains'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return ModelTrain.objects.filter(owner=self.request.user.id)

class ModelTrainDetail(LoginRequiredMixin, DetailView):
    """
    This is the view which displays the train's information
    """

    model = ModelTrain

    fields = ['name', 'manufacturer', 'model_class', 'traction', 'scale', 'era']

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class ModelTrainCreate(LoginRequiredMixin, CreateView):
    """
    This view creates a new model train
    """

    model = ModelTrain

    fields = ['name', 'manufacturer', 'model_class', 'traction', 'scale', 'era']

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)

class ModelTrainUpdate(LoginRequiredMixin, UpdateView):
    """
    This view updates a model train
    """

    model = ModelTrain

    success_url = reverse_lazy('model-trains')

    fields = ['name', 'manufacturer', 'model_class', 'traction', 'scale', 'era']

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class ModelTrainDelete(LoginRequiredMixin, DeleteView):
    """
    This view deletes a model train
    """

    model = ModelTrain

    success_url = reverse_lazy('model-trains')

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class Collections(LoginRequiredMixin, ListView):
    """
    This view represents a list of the user's collections
    """

    model = Collection

    template_name = 'manager/collections.html'

    context_object_name = 'collections'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)

class CollectionsDetail(LoginRequiredMixin, DetailView):
    """
    This is the view which displays a collections information
    """

    model = Collection

    fields = ['name', 'description', 'trains']

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class CollectionCreate(LoginRequiredMixin, CreateView):
    """
    This view creates a collection
    """

    model = Collection

    form_class = CollectionForm

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['user'] = self.request.user

        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)

class CollectionsUpdate(LoginRequiredMixin, UpdateView):
    """
    This view updates a collection
    """

    model = Collection

    form_class = CollectionForm

    success_url = reverse_lazy('collections')

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['user'] = self.request.user

        return kwargs

class CollectionsDelete(LoginRequiredMixin, DeleteView):
    """
    This view deletes a collection
    """

    model = Collection

    success_url = reverse_lazy('collections')

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class StatisticsView(LoginRequiredMixin, TemplateView):
    """
    This view lists the statistics
    """

    template_name = 'manager/statistics.html'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

class ManufacturerChartView(LoginRequiredMixin, TemplateView):
    """
    This view shows the manufacturer chart
    """

    template_name = 'manager/manufacturer_pie_chart.html'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            manufacturer_chart = ManufacturerChart(self.request.user)

            context['manufacturer_chart'] = manufacturer_chart

        return context

class TractionChartView(LoginRequiredMixin, TemplateView):
    """
    This view shows the traction chart
    """

    template_name = 'manager/traction_pie_chart.html'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            traction_chart = TractionChart(self.request.user)

            context['traction_chart'] = traction_chart

        return context

class ScaleChartView(LoginRequiredMixin, TemplateView):
    """
    This view shows the scale chart
    """

    template_name = 'manager/scale_pie_chart.html'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            scale_chart = ScaleChart(self.request.user)

            context['scale_chart'] = scale_chart

        return context

class CollectionChartView(LoginRequiredMixin, TemplateView):
    """
    This view shows the collection chart
    """

    template_name = 'manager/collection_bar_chart.html'

    login_url = '/login/'

    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            collection_chart = CollectionChart(self.request.user)

            context['collection_chart'] = collection_chart

        return context
