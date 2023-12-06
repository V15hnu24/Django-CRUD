from django.urls import path
from . import views

urlpatterns = [
    path('getLocations', views.getLocations),
    path('addLocation/', views.addLocation),
    path('deleteLocation/<int:pk>', views.deleteLocation),
    path('updateLocation/<int:pk>', views.updateLocation),

]
