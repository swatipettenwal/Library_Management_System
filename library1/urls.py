from django.urls import path
from . import views

app_name = 'library1'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
