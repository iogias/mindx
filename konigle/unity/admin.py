from django.contrib import admin
from .models import UnityEmail


@admin.register(UnityEmail)
class UnityEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'created', 'updated', 'is_active', 'status')
    list_filter = ('created', 'is_active', 'status')
