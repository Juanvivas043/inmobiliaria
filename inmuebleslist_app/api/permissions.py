from rest_framework import permissions

#permiso personalizado para el viewset de empresa, si el metodo es get va a mostar, si es post, put o delete, tiene que ser administrador para que se muestre
class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
       if request.method == 'GET':
           return True
       staff_permission = bool(request.user and request.user.is_staff)
       return staff_permission
   
   
   #permiso personalizado para la clase de ComentarioDetailAV, si el metodo es get lo deja listar, si es put o delete no se muestra a menos que sea el usuario que realizo el comentario
class IsComentarioUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.comentario_user ==  request.user or request.user.is_staff