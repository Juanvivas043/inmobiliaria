from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

#validaciones fuera de la clase
def colum_longitud(value):
    if len(value) < 2:
        raise serializers.ValidationError('El valor es demasiado corta')

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField(validators=[colum_longitud])
    pais = serializers.CharField(validators=[colum_longitud])
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Inmueble.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.pais = validated_data.get('pais', instance.pais)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    #validaciones dentro de la clase 
    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError('La direccion y el pais deben ser distintas')
        else:
            return data
        
    #validaciones dentro de la clase para las propiedades especificas
    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError('La url de la imagen es muy corta')
        else:
            return data