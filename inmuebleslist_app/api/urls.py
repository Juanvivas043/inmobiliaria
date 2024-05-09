from django.urls import path
from inmuebleslist_app.api.views import EdificacionListAV, EdificacionDetailAV, EmpresaListAV, EmpresaDetailAV, ComentarioList, ComentarioDetail

urlpatterns = [
    path('list/', EdificacionListAV.as_view(), name='edificacion-list'),
    path('<int:pk>/', EdificacionDetailAV.as_view(), name='edificacion-detail'), 
    path('empresa/', EmpresaListAV.as_view(), name='empresa-list'),
    path('empresa/<int:pk>', EmpresaDetailAV.as_view(), name='empresa-detail'),
    path('comentario/', ComentarioList.as_view(), name='comentario-list'),
    path('comentario/<int:pk>', ComentarioDetail.as_view(), name='comentario-detail'),


]