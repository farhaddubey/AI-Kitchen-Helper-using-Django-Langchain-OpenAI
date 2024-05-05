from django.urls import path
from jarvischef.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home')
]
