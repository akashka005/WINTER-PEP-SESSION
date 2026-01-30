from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.portfolio_home, name='home'),
    path('api/contact/', views.submit_contact_form, name='submit_contact'),
    path('api/chatbot/', views.chatbot_message, name='chatbot_message'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contacts/', views.contact_messages, name='contact_messages'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('chat-history/', views.chat_history, name='chat_history'),
    path('chat-history/<str:session_id>/', views.chat_session, name='chat_session'),
    
    path('edit-content/', views.edit_content, name='edit_content'),
    path('add-content/', views.add_content, name='add_content'),
    path('edit-content/<int:pk>/', views.update_content, name='update_content'),
    path('delete-content/<int:pk>/', views.delete_content, name='delete_content'),
]