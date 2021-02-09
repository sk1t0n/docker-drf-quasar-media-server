from django.contrib import admin

from media_server.models import Video, Genre


class GenreInline(admin.TabularInline):
    model = Genre.videos.through
    verbose_name_plural = 'Relationship of videos and genres'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'release_date', 'runtime', 'url'
    )
    list_display_links = ('title',)
    fieldsets = (
        ('Main fields', {
            'fields': (
                'title', 'description', 'release_date', 'runtime', 'url'
            )
        }),
        ('Additional fields', {
            'fields': ('slug',)
        })
    )
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = (GenreInline,)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    fieldsets = (
        ('Main fields', {
            'fields': ('name',)
        }),
        ('Additional fields', {
            'fields': ('slug',)
        })
    )
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = (GenreInline,)


admin.site.site_title = 'Media Server'
admin.site.site_header = 'Media Server'
