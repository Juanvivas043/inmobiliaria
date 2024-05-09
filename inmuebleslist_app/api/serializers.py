from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Empresa, Comentario

#Serializers usando ModelSerializer}

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    #longitud_direccion = serializers.SerializerMethodField()
    
    class Meta:
        model = Edificacion
        fields = "__all__"
        read_only_fields = ['fecha_creado', 'id']
        #fields = ['direccion', 'longitud_direccion' ,'pais', 'descripcion', 'imagen', 'fecha_creado', 'active']
        #exclude = ['id']
        
    # def get_longitud_direccion(self, object):
    #     catnidad_caracteres = len(object.direccion)
    #     return catnidad_caracteres



class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    edificacionlist = EdificacionSerializer(many=True, read_only=True)
    #edificacionlist = serializers.StringRelatedField(many=True)
    #edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #edificacionlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='edificacion-detalle')
    
    class Meta:
        model = Empresa
        fields = "__all__"
        read_only_fields = ['id', 'fecha_creado']






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