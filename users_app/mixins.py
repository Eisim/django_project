from django.core.exceptions import PermissionDenied


class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        permission_ok = request.user.is_authenticated and request.user.username == obj.user.username
        if permission_ok:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied("У Вас нет прав на редактирование")
