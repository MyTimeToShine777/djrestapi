from django.urls import path
from .import views

urlpatterns = [
    path('', views.StudentApiView.as_view(), name='test')
]
