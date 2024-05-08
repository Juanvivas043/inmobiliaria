from django.urls import path
from inmuebleslist_app.api.views import InmuebleListAV, InmuebleDetailAV

urlpatterns = [
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'),
    path('<int:pk>/', InmuebleDetailAV.as_view(), name='inmueble-detalle'), 

]