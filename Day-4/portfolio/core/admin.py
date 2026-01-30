from django.contrib import admin
from .models import ContactSubmission, ChatMessage, PortfolioContent


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Contact Info', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'session_id', 'message', 'timestamp')
    list_filter = ('sender', 'session_id', 'timestamp')
    search_fields = ('message', 'session_id')
    readonly_fields = ('timestamp',)


@admin.register(PortfolioContent)
class PortfolioContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'is_active', 'updated_at')
    list_filter = ('content_type', 'is_active', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Content', {
            'fields': ('content_type', 'title', 'description')
        }),
        ('Additional Data', {
            'fields': ('additional_data',),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )
