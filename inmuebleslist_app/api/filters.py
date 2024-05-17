from django_filters import FilterSet, CharFilter, BooleanFilter
from inmuebleslist_app.models import Comentario

class ComentarioFilter(FilterSet):
    comentario_user__username = CharFilter(lookup_expr='icontains')
    active = BooleanFilter()
    
    class Meta:
        model = Comentario
        fields = ['comentario_user__username', 'active']


