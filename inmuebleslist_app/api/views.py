from inmuebleslist_app.models import Edificacion, Empresa, Comentario
from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer, ComentarioSerializer
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from inmuebleslist_app.api.permissions import AdminOrReadOnly, ComentarioUserOrReadOnly





#Clases con Modelviewset

class EmpresaVS(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

# Clases con ViewSets

# class EmpresaVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Empresa.objects.all()
#         serializer = EmpresaSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK) 
    
#     def create(self, request):
#         deserializer = EmpresaSerializer(data=request.data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return Response(deserializer.data, status=status.HTTP_201_CREATED)
#         else: 
#             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Empresa.objects.all()
#         edificacionlist = get_object_or_404(queryset, pk=pk)
#         serializer = EmpresaSerializer(edificacionlist)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'Error':'La empresa no existe'})
        
#         deserializer = EmpresaSerializer(empresa, data=request.data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return Response(deserializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def destroy(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'Error':'La empresa no existe'},status=status.HTTP_404_NOT_FOUND)
        
#         empresa.delete()
#         return Response({'Success':'La empresa se ha eliminado'},status=status.HTTP_204_NO_CONTENT)

                
#Clases con generics views

class ComentarioList(generics.ListAPIView):
    # queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comentario.objects.filter(edificacion=pk)

class ComentarioCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer
    
    def get_queryset(self):
        return Comentario.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        edificacion = Edificacion.objects.get(pk=pk)
        
        user = self.request.user
        comentario_queryset =Comentario.objects.filter(edificacion=edificacion, comentario_user=user)
        if comentario_queryset.exists():
            raise ValidationError('El usuario ya escribio un comentario para este inmueble')
        
        
        if edificacion.number_calificacion == 0:
            edificacion.avg_calificacion = serializer.validated_data['calificacion'] 
        else: 
            edificacion.avg_calificacion = (serializer.validated_data['calificacion']  + edificacion.avg_calificacion)/2
        
        edificacion.number_calificacion = edificacion.number_calificacion + 1
        edificacion.save()
        
        serializer.save(edificacion=edificacion, comentario_user=user)

        
class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ComentarioUserOrReadOnly]
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    
#Clases con Api Views

# class EmpresaListAV(APIView):
#     def get(self, request):
#         empresa = Empresa.objects.all()
#         #serializer = EmpresaSerializer(empresa, many=True, context={'request':request})
#         serializer = EmpresaSerializer(empresa, many=True, context={'request':request})

#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         deserializer = EmpresaSerializer(data=request.data)
#         if deserializer.is_valid(): 
#             deserializer.save()
#             return Response(deserializer.data, status=status.HTTP_201_CREATED)
#         else: 
#             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EmpresaDetailAV(APIView): 

#     def get(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'Error':'No existe la empresa'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = EmpresaSerializer(empresa, context={'request':request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'Error':'La empresa no existe'}, status=status.HTTP_404_NOT_FOUND)
#         deserializer = EmpresaSerializer(empresa, data=request.data, context={'request':request})
#         if deserializer.is_valid():
#             deserializer.save()
#             return Response(deserializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'Error':'La empresa no existe'}, status=status.HTTP_404_NOT_FOUND)
#         empresa.delete()
#         return Response({'Success':'Se ha eliminado la empresa correctamente'}, status=status.HTTP_204_NO_CONTENT)

class EdificacionListAV(APIView):

    def get(self, request):
        edificacion = Edificacion.objects.all() 
        serializer = EdificacionSerializer(edificacion, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        deserializer = EdificacionSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EdificacionDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error':'No existe la edificacion'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EdificacionSerializer(edificacion)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error':'No existe la edificacion'}, status=status.HTTP_404_NOT_FOUND)
        
        deserializer = EdificacionSerializer(edificacion, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data, status=status.HTTP_200_OK)
        else:
            return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error':'La edificacion no se puede eliminar el inmueble'}, status=status.HTTP_400_BAD_REQUEST)
        
        edificacion.delete()
        return Response({'Success':'La edificacion se ha eliminado'}, status=status.HTTP_204_NO_CONTENT)

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