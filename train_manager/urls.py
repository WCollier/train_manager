"""train_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import include, path

urlpatterns = [
    path('', include('manager.urls')),
    path('', include('django.contrib.auth.urls')),
    path('sign-up', CreateView.as_view(
        template_name='registration/sign_up.html',
        form_class=UserCreationForm,
        success_url='/'), name='sign-up'),

    path('admin/', admin.site.urls)
]
