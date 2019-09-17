"""URLs"""

from django.urls import path

from . import views


urlpatterns = [
    path('', views.AddressList.as_view()),
    path('<int:pk>/', views.AddressDetail.as_view()),
    path('company/<str:company>/', views.get_addresses_of_company),
    path('city/<str:city>/', views.get_companies_in_city),
    path('getPostalCodes', views.get_postal_codes),
]
