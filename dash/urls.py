from django.urls import path

from .views import IndexView

urlpatterns = [
    path('dash', IndexView.as_view(), name='dash'),
]
