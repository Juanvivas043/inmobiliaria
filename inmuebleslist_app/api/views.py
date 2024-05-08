from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


#Clases con Api Views

class InmuebleListAV(APIView):

    def get(self, request):
        inmueble = Inmueble.objects.all() 
        serializer = InmuebleSerializer(inmueble, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        deserializer = InmuebleSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InmuebleDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist():
            return Response({'Error':'No existe el inmueble'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = InmuebleSerializer(inmueble)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist():
            return Response({'Error':'No existe el inmueble'}, status=status.HTTP_404_NOT_FOUND)
        
        deserializer = InmuebleSerializer(inmueble, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data, status=status.HTTP_200_OK)
        else:
            return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist():
            return Response({'Error':'El inmueble no se puede eliminar el inmueble'}, status=status.HTTP_400_BAD_REQUEST)
        
        inmueble.delete()
        return Response({'Success':'El inmueble se ha eliminado'}, status=status.HTTP_204_NO_CONTENT)
        





# Decorators Api Views
""" @api_view(['GET', 'POST'])
def inmueble_list(request):
    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        deserializer = InmuebleSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
            return Response(deserializer.errors)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def inmueble_detalle(request, pk):
    if request.method == 'GET':
        try:
            inmueble = Inmueble.objects.get(pk=pk)
            serializer = InmuebleSerializer(inmueble)
            return Response(serializer.data)
        except Inmueble.DoesNotExist:
            return Response({'Error':'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        inmueble = Inmueble.objects.get(pk=pk)
        deserializer = InmuebleSerializer(inmueble, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
            return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        try:
            inmueble = Inmueble.objects.get(pk=pk)
            inmueble.delete()
            return Response({'Success':'El inmueble fue eliminado'}, status=status.HTTP_204_NO_CONTENT)
        except Inmueble.DoesNotExist:
            return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND) """