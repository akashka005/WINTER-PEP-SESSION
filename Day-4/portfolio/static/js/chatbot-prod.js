'use strict';
class ChatSession {
    constructor() {
        this.sessionId = localStorage.getItem('chatSessionId') || 'session_' + Date.now();
        localStorage.setItem('chatSessionId', this.sessionId);
        this.messageCount = 0;
    }
}

const chatSession = new ChatSession();
const chatInput = document.getElementById('chatInput');
const sendBtn = document.getElementById('sendBtn');
const chatBox = document.getElementById('chatBox');

if (!chatInput || !sendBtn || !chatBox) {
    console.warn('Chat elements not found - chatbot may not function properly');
}
function sendMessage() {
    const message = chatInput?.value?.trim();
    
    if (!message) return;
    if (chatSession.messageCount > 100) {
        addMessage('Chat session limit reached. Please refresh the page.', 'bot-message');
        return;
    }
    addMessage(message, 'user-message');
    chatInput.value = '';
    if (sendBtn) {
        sendBtn.disabled = true;
        sendBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
    }

    sendMessageToBackend(message);
}
function sendMessageToBackend(message) {
    try {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || '';
        
        if (!csrfToken) {
            console.warn('CSRF token not found');
        }

        const payload = {
            message: message,
            session_id: chatSession.sessionId
        };

        fetch('/api/chatbot/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(payload)
        })
        .then(response => {
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return response.json();
        })
        .then(data => {
            if (data.success) {
                addMessage(data.response, 'bot-message');
                chatSession.messageCount++;
            } else {
                addMessage('Sorry, there was an error. Please try again.', 'bot-message');
            }
        })
        .catch(error => {
            console.error('Chatbot Error:', error);
            addMessage('Error communicating with server. Please check your connection.', 'bot-message');
        })
        .finally(() => {
            if (sendBtn) {
                sendBtn.disabled = false;
                sendBtn.innerHTML = '<i class="fas fa-paper-plane"></i>';
            }
            chatInput?.focus();
        });
    } catch (error) {
        console.error('Send Message Error:', error);
        addMessage('An unexpected error occurred.', 'bot-message');
    }
}

function addMessage(text, className) {
    if (!chatBox) return;
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${className}`;
    
    const p = document.createElement('p');
    p.textContent = text;
    messageDiv.appendChild(p);
    
    chatBox.appendChild(messageDiv);
    setTimeout(() => {
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 0);
}


if (sendBtn && chatInput) {
    sendBtn.addEventListener('click', sendMessage);
    
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    const chatContainer = document.querySelector('.chatbot-container') || document.querySelector('.chat-wrapper');
    if (chatContainer) {
        chatContainer.addEventListener('click', () => {
            chatInput.focus();
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('🤖 Chatbot initialized - Session:', chatSession.sessionId);
});