from django.urls import path, include
from inmuebleslist_app.api.views import (EdificacionListAV, EdificacionDetailAV, #EmpresaListAV, EmpresaDetailAV,
                                          ComentarioList, ComentarioDetail, ComentarioCreate, EmpresaVS)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('empresa', EmpresaVS, basename = 'empresa')

urlpatterns = [
    path('edificacion/', EdificacionListAV.as_view(), name='edificacion-list'),
    path('edificacion/<int:pk>/', EdificacionDetailAV.as_view(), name='edificacion-detail'), 
    
    path('', include(router.urls)),
    # path('empresa/', EmpresaListAV.as_view(), name='empresa-list'),
    # path('empresa/<int:pk>', EmpresaDetailAV.as_view(), name='empresa-detail'),
    
    path('edificacion/<int:pk>/comentario-create/', ComentarioCreate.as_view(), name='comentario-create'),
    path('edificacion/<int:pk>/comentario/', ComentarioList.as_view(), name='comentario-list'),
    path('edificacion/comentario/<int:pk>/', ComentarioDetail.as_view(), name='comentario-detail'),

]