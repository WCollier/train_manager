from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('models/', views.ModelTrains.as_view(), name='model-trains'),
    path('models/add/', views.ModelTrainCreate.as_view(), name='model-train-add'),
    path('models/<slug:pk>/', views.ModelTrainDetail.as_view(), name='model-train-detail'),
    path('models/<int:pk>/update/', views.ModelTrainUpdate.as_view(), name='model-train-update'),
    path('models/<int:pk>/delete/', views.ModelTrainDelete.as_view(), name='model-train-delete'),
]
