from django.urls import path
from iris_app.views import home

urlpatterns = [
    path('', home)
]