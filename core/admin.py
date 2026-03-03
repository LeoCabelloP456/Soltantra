from django.contrib import admin
from .models import Video
from .models import Staff

# Register your models here.
admin.site.register(Video)
admin.site.register(Staff)

class VideoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "precio", "recomendado", "created_at")
    prepopulated_fields = {"slug":("titulo", )}

class StaffAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cargo", "activo")
    prepopulated_fields = {"slug": {"nombre",}}
    search_fields = ("nombre", "cargo")
    list_filter = ("activo",)