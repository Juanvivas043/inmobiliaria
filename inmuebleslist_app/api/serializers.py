from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Empresa, Comentario

#Serializers usando ModelSerializer

class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comentario
        fields = ['id', 'calificacion', 'texto', 'edificacion', 'active', 'fecha_creado', 'fecha_actualizado', 'comentario_user']
        extra_kwargs = {
            'id': {'read_only':True}, 
            'edificacion': {'read_only':True}, 
            'fecha_creado': {'read_only':True}, 
            'fecha_actualizado': {'read_only':True}, 
            'comentario_user': {'read_only':True}
        }

class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    #longitud_direccion = serializers.SerializerMethodField()
    empresa = serializers.StringRelatedField(read_only=True)
    empresa_nombre = serializers.CharField(source='empresa.nombre')
    
    class Meta:
        model = Edificacion
        fields = ['id' ,'direccion', 'pais', 'descripcion', 'fecha_creado', 'active', 'empresa', 'empresa_nombre','comentarios', 'avg_calificacion', 'number_calificacion']
        extra_kwargs = {
            'id': {'read_only':True}, 
            'fecha_creado': {'read_only':True}, 
            'comentarios': {'read_only':True},
            'avg_calificacion': {'read_only':True},
            'number_calificacion': {'read_only':True},
        }
        
        #fields = ['direccion', 'longitud_direccion' ,'pais', 'descripcion', 'imagen', 'fecha_creado', 'active']
        #exclude = ['id']
        
    # def get_longitud_direccion(self, object):
    #     catnidad_caracteres = len(object.direccion)
    #     return catnidad_caracteres

class EmpresaSerializer(serializers.ModelSerializer):
    edificacionlist = EdificacionSerializer(many=True, read_only=True)
    #edificacionlist = serializers.StringRelatedField(many=True)
    #edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #edificacionlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='edificacion-detalle')
    
    class Meta:
        model = Empresa
        fields = ['id', 'nombre', 'website', 'fecha_creado', 'active', 'edificacionlist']
        extra_kwargs = {
            'id': {'read_only':True}, 
            'fecha_creado': {'read_only':True}, 
            'edificacionlist': {'read_only':True}
        }
        
#Serializers usando modulo serializers

#validaciones fuera de la clase
# def colum_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('El valor es demasiado corta')

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[colum_longitud])
#     pais = serializers.CharField(validators=[colum_longitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     fecha_creado = serializers.DateTimeField(read_only=True)
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     #validaciones dentro de la clase 
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError('La direccion y el pais deben ser distintas')
#         else:
#             return data
        
#     #validaciones dentro de la clase para las propiedades especificas
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError('La url de la imagen es muy corta')
#         else:
#             return data