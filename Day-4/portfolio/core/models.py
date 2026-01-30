from django.db import models
from django.utils import timezone

class ContactSubmission(models.Model):
    """Model to store contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


class ChatMessage(models.Model):
    """Model to store chatbot conversations"""
    SENDER_CHOICES = (
        ('user', 'User'),
        ('bot', 'Bot'),
    )
    
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, default='default')

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender.capitalize()}: {self.message[:50]}"


class PortfolioContent(models.Model):
    """Model to store editable portfolio content"""
    CONTENT_TYPES = (
        ('about', 'About Section'),
        ('skill', 'Skill Item'),
        ('project', 'Project'),
        ('social', 'Social Link'),
    )
    
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    additional_data = models.JSONField(default=dict, blank=True)  # For extra fields
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.get_content_type_display()} - {self.title}"
