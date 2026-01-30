from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import json
import logging

from .models import ContactSubmission, ChatMessage, PortfolioContent
from .forms import ContactForm, PortfolioContentForm

logger = logging.getLogger(__name__)

def portfolio_home(request):
    try:
        context = {
            'portfolio_content': PortfolioContent.objects.filter(is_active=True)
        }
        return render(request, 'index.html', context)
    except Exception as e:
        logger.error(f"Error loading portfolio home: {str(e)}")
        return render(request, 'index.html', {'error': 'Error loading portfolio'}, status=500)


@require_http_methods(["POST"])
def submit_contact_form(request):
    try:
        data = json.loads(request.body)
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field, '').strip():
                return JsonResponse({
                    'success': False,
                    'message': f'{field.capitalize()} is required'
                }, status=400)
    
        email = data.get('email', '').strip()
        if not email or '@' not in email:
            return JsonResponse({
                'success': False,
                'message': 'Please provide a valid email'
            }, status=400)
        
        contact = ContactSubmission.objects.create(
            name=data.get('name', '').strip()[:100],
            email=email,
            phone=data.get('phone', '').strip()[:15],
            subject=data.get('subject', '').strip()[:200],
            message=data.get('message', '').strip()
        )
        
        logger.info(f"New contact submission from {contact.email}")
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you! I will get back to you soon.'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid request format'
        }, status=400)
    except IntegrityError as e:
        logger.error(f"Database error: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': 'Database error occurred'
        }, status=500)
    except Exception as e:
        logger.error(f"Contact form error: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }, status=500)


@require_http_methods(["POST"])
def chatbot_message(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')

        if not user_message or len(user_message) > 1000:
            return JsonResponse({
                'success': False,
                'message': 'Invalid message'
            }, status=400)
        
        if not session_id or len(session_id) > 100:
            return JsonResponse({
                'success': False,
                'message': 'Invalid session'
            }, status=400)
        message_count = ChatMessage.objects.filter(session_id=session_id).count()
        if message_count > 200:
            return JsonResponse({
                'success': False,
                'message': 'Session message limit reached'
            }, status=400)
        
        ChatMessage.objects.create(
            sender='user',
            message=user_message,
            session_id=session_id
        )
        
        bot_response = get_bot_response(user_message)
        ChatMessage.objects.create(
            sender='bot',
            message=bot_response,
            session_id=session_id
        )
        
        logger.info(f"Chat message saved - Session: {session_id}")
        
        return JsonResponse({
            'success': True,
            'response': bot_response
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid request format'
        }, status=400)
    except Exception as e:
        logger.error(f"Chatbot error: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': 'Error processing message'
        }, status=500)


def get_bot_response(message):
    message_lower = message.lower().strip()
    
    chatbot_responses = {
        'hello': 'Hey there! 👋 How can I help you?',
        'hi': 'Hello! 😊 Feel free to ask me anything about Akash or his projects!',
        'hey': 'Hi there! What would you like to know?',
        'what is your name': "I'm Akash's AI assistant here on this portfolio!",
        'who is akash': 'Akash is a talented CSE AI/ML student with expertise in Python, Machine Learning, and Full Stack Development!',
        'skills': 'Akash specializes in: Python, C++, Java, HTML, CSS, JavaScript, React, Django, and advanced ML libraries!',
        'projects': 'Akash has completed Credit Card Fraud Detection, Quant Analyzer, and AI Resume Analyzer. Currently working on Brain Tumor Detection!',
        'contact': 'You can reach Akash at: Email: akashka688@gmail.com | Phone: +91 9600205581',
        'email': 'Email: akashka688@gmail.com',
        'phone': 'Phone: +91 9600205581',
        'github': 'GitHub: github.com/akashka005',
        'linkedin': 'LinkedIn: linkedin.com/in/akashka005',
        'leetcode': 'LeetCode: leetcode.com/akashka005',
        'thanks': "You're welcome! 😊",
        'thank you': 'Happy to help! 🙌',
        'bye': 'Goodbye! 👋 Have a great day!',
        'experience': 'Akash has hands-on experience with ML projects, web development, and data analysis!',
        'machine learning': 'Akash specializes in TensorFlow, PyTorch, CNN, Deep Learning, and NLP!',
        'python': 'Python is Akash\'s primary language for ML and data science projects!',
    }
    
    for key, response in chatbot_responses.items():
        if key in message_lower:
            return response
    return 'That\'s interesting! 🤔 Feel free to ask about Akash\'s skills, projects, experience, or how to contact him!'

def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        if not username or not password:
            return render(request, 'login.html', {'error': 'Username and password required'})
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            logger.info(f"User {username} logged in")
            return redirect('core:dashboard')
        else:
            logger.warning(f"Failed login attempt for {username}")
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logger.info(f"User {request.user.username} logged out")
    logout(request)
    return redirect('core:home')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')
        
        if not username or not email or not password:
            return render(request, 'register.html', {'error': 'All fields are required'})
        
        if len(username) < 3:
            return render(request, 'register.html', {'error': 'Username must be at least 3 characters'})
        
        if len(password) < 6:
            return render(request, 'register.html', {'error': 'Password must be at least 6 characters'})
        
        if password != password_confirm:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            logger.info(f"New user registered: {username}")
            return redirect('core:dashboard')
        except Exception as e:
            logger.error(f"Registration error: {str(e)}")
            return render(request, 'register.html', {'error': 'Registration failed. Please try again.'})
    
    return render(request, 'register.html')

@login_required(login_url='core:login')
def dashboard(request):
    try:
        context = {
            'contacts_count': ContactSubmission.objects.count(),
            'unread_contacts': ContactSubmission.objects.filter(is_read=False).count(),
            'total_messages': ChatMessage.objects.count(),
            'content_items': PortfolioContent.objects.count(),
            'active_sessions': ChatMessage.objects.values('session_id').distinct().count(),
            'recent_contacts': ContactSubmission.objects.all()[:5],
        }
        return render(request, 'dashboard.html', context)
    except Exception as e:
        logger.error(f"Dashboard error: {str(e)}")
        return render(request, 'dashboard.html', {'error': 'Error loading dashboard'}, status=500)


@login_required(login_url='core:login')
def contact_messages(request):
    try:
        filter_type = request.GET.get('filter', 'all')
        
        if filter_type == 'unread':
            contacts = ContactSubmission.objects.filter(is_read=False)
        else:
            contacts = ContactSubmission.objects.all()
        
        context = {
            'contacts': contacts,
            'filter': filter_type
        }
        return render(request, 'contact_messages.html', context)
    except Exception as e:
        logger.error(f"Contact messages error: {str(e)}")
        return render(request, 'contact_messages.html', {'error': 'Error loading messages'}, status=500)


@login_required(login_url='core:login')
def contact_detail(request, pk):
    try:
        contact = get_object_or_404(ContactSubmission, pk=pk)
        contact.is_read = True
        contact.save()
        return render(request, 'contact_detail.html', {'contact': contact})
    except Exception as e:
        logger.error(f"Contact detail error: {str(e)}")
        return render(request, 'contact_detail.html', {'error': 'Contact not found'}, status=404)


@login_required(login_url='core:login')
def chat_history(request):
    try:
        sessions = ChatMessage.objects.values('session_id').annotate(
            message_count=Count('id')
        ).order_by('-id')
        context = {'sessions': sessions}
        return render(request, 'chat_history.html', context)
    except Exception as e:
        logger.error(f"Chat history error: {str(e)}")
        return render(request, 'chat_history.html', {'error': 'Error loading chat history'}, status=500)


@login_required(login_url='core:login')
def chat_session(request, session_id):
    try:
        messages = ChatMessage.objects.filter(session_id=session_id)
        if not messages.exists():
            messages = []
        
        context = {
            'session_id': session_id,
            'messages': messages
        }
        return render(request, 'chat_session.html', context)
    except Exception as e:
        logger.error(f"Chat session error: {str(e)}")
        return render(request, 'chat_session.html', {'error': 'Session not found'}, status=404)


@login_required(login_url='core:login')
def edit_content(request):
    try:
        contents = PortfolioContent.objects.all()
        context = {'contents': contents}
        return render(request, 'edit_content.html', context)
    except Exception as e:
        logger.error(f"Edit content error: {str(e)}")
        return render(request, 'edit_content.html', {'error': 'Error loading content'}, status=500)


@login_required(login_url='core:login')
def add_content(request):
    try:
        if request.method == 'POST':
            form = PortfolioContentForm(request.POST)
            if form.is_valid():
                form.save()
                logger.info(f"New content added: {form.cleaned_data.get('title')}")
                return redirect('core:edit_content')
        else:
            form = PortfolioContentForm()
        
        context = {'form': form, 'action': 'Add'}
        return render(request, 'content_form.html', context)
    except Exception as e:
        logger.error(f"Add content error: {str(e)}")
        return render(request, 'content_form.html', {'error': 'Error adding content'}, status=500)


@login_required(login_url='core:login')
def update_content(request, pk):
    try:
        content = get_object_or_404(PortfolioContent, pk=pk)
        
        if request.method == 'POST':
            form = PortfolioContentForm(request.POST, instance=content)
            if form.is_valid():
                form.save()
                logger.info(f"Content updated: {content.title}")
                return redirect('core:edit_content')
        else:
            form = PortfolioContentForm(instance=content)
        
        context = {'form': form, 'action': 'Edit', 'content': content}
        return render(request, 'content_form.html', context)
    except Exception as e:
        logger.error(f"Update content error: {str(e)}")
        return render(request, 'content_form.html', {'error': 'Error updating content'}, status=500)


@login_required(login_url='core:login')
def delete_content(request, pk):
    try:
        content = get_object_or_404(PortfolioContent, pk=pk)
        
        if request.method == 'POST':
            content.delete()
            logger.info(f"Content deleted: {content.title}")
            return redirect('core:edit_content')
        
        context = {'content': content}
        return render(request, 'confirm_delete.html', context)
    except Exception as e:
        logger.error(f"Delete content error: {str(e)}")
        return render(request, 'confirm_delete.html', {'error': 'Error deleting content'}, status=500)