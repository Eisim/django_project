from django.contrib import admin

from users_app.models import Profile


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'social_link')
    list_filter = ('id',)
    search_fields = ('user',)
    readonly_fields = ('user', 'bio', 'social_link')
