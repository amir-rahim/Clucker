from django.contrib import admin
from .models import User, Post


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    listDisplay = [
        'username', 'first_name', 'last_name', 'email', 'is_active',
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'created_at')
    list_filter = ("author",)


admin.site.register(Post, PostAdmin)
