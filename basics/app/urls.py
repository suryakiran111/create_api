from django.urls import path
from . import views
urlpatterns = [
    path('countries',views.home,name='countries'),
]
