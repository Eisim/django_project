from django.core.exceptions import PermissionDenied


class TitleMixin:
    title: str = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.title:
            context["title"] = self.title
        return context


class StuffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied("Доступ только для сотрудников")
        return super().dispatch(request, *args, **kwargs)
