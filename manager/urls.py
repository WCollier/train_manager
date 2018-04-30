from django.urls import path

from jchart.views import ChartView

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('collections/', views.Collections.as_view(), name='collections'),
    path('collections/new/', views.CollectionCreate.as_view(), name='collection-create'),
    path('collections/<slug:pk>/', views.CollectionsDetail.as_view(), name='collection-detail'),
    path('collections/<int:pk>/update/', views.CollectionsUpdate.as_view(), name='collections-update'),
    path('collections/<int:pk>/delete/', views.CollectionsDelete.as_view(), name='collections-delete'),

    path('models/', views.ModelTrains.as_view(), name='model-trains'),
    path('models/new/', views.ModelTrainCreate.as_view(), name='model-train-create'),
    path('models/<slug:pk>/', views.ModelTrainDetail.as_view(), name='model-train-detail'),
    path('models/<int:pk>/update/', views.ModelTrainUpdate.as_view(), name='model-train-update'),
    path('models/<int:pk>/delete/', views.ModelTrainDelete.as_view(), name='model-train-delete'),

    path('statistics/', views.StatisticsView.as_view(), name='statistics'),
    path('statistics/manufacturer-pie-chart/', views.ManufacturerChartView.as_view(), name='statistics-manufacturer-chart'),
    path('statistics/traction-pie-chart/', views.TractionChartView.as_view(), name='statistics-traction-chart'),
    path('statistics/scale-pie-chart/', views.ScaleChartView.as_view(), name='statistics-scale-chart'),
    path('statistics/collection-bar-chart/', views.CollectionChartView.as_view(), name='statistics-collection-chart'),
]
