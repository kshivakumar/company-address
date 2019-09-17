"""CompanyAddress URL Configuration"""

from django.urls import path, include

urlpatterns = [
    path('address/', include('address.urls'))
]
