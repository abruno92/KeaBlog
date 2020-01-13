from django.contrib import admin
from .models import Post, PostInstance


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


@admin.register(PostInstance)
class PostInstanceAdmin(admin.ModelAdmin):
    list_display = ('status', 'id', 'post')
