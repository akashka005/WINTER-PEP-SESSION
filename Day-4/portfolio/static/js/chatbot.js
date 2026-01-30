let sessionId = localStorage.getItem('chatSessionId') || 'session_' + Date.now();
localStorage.setItem('chatSessionId', sessionId);

const chatInput = document.getElementById('chatInput');
const sendBtn = document.getElementById('sendBtn');
const chatBox = document.getElementById('chatBox');

function sendMessage() {
    const message = chatInput.value.trim();
    
    if (message === '') return;
    addMessage(message, 'user-message');
    chatInput.value = '';
    sendMessageToBackend(message);
}

function sendMessageToBackend(message) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || '';
    
    fetch('/api/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            message: message,
            session_id: sessionId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            addMessage(data.response, 'bot-message');
        } else {
            addMessage('Sorry, there was an error processing your message.', 'bot-message');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        addMessage('Error communicating with the server.', 'bot-message');
    });
}

function addMessage(text, className) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${className}`;
    messageDiv.innerHTML = `<p>${text}</p>`;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
function getBotResponse(userMessage) {
    const lowerMessage = userMessage.toLowerCase().trim();
    
    const chatbotResponses = {
        'hello': 'Hey there! 👋 How can I help you?',
        'hi': 'Hello! 😊 Feel free to ask me anything about Akash or his projects!',
        'what is your name': 'I\'m Akash\'s AI assistant here on this portfolio!',
        'who is akash': 'Akash is a talented CSE AI/ML student with expertise in Python, Machine Learning, and Full Stack Development!',
        'skills': 'Akash specializes in: Python, C++, Java, HTML, CSS, JavaScript, React, Django, and advanced ML libraries!',
        'projects': 'Akash has completed Credit Card Fraud Detection, Quant Analyzer, and AI Resume Analyzer. Currently working on Brain Tumor Detection!',
        'contact': 'You can reach Akash at: Email: akashka688@gmail.com | Phone: +91 9600205581',
        'email': 'akashka688@gmail.com',
        'phone': '+91 9600205581',
        'github': 'github.com/akashka005',
        'linkedin': 'linkedin.com/in/akashka005',
        'leetcode': 'leetcode.com/akashka005',
        'thanks': 'You\'re welcome! 😊',
        'thank you': 'Happy to help! 🙌',
        'bye': 'Goodbye! 👋',
    };
    
    for (const key in chatbotResponses) {
        if (lowerMessage.includes(key)) {
            return chatbotResponses[key];
        }
    }
    
    return 'That\'s interesting! 🤔 Feel free to ask about Akash\'s skills, projects, or how to contact him!';
}
sendBtn.addEventListener('click', sendMessage);

chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

chatInput.focus();

console.log('🤖 Chatbot initialized successfully!');