document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                subject: document.getElementById('subject').value,
                message: document.getElementById('message').value
            };

            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

            fetch('/api/contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                formMessage.className = 'form-message success';
                formMessage.textContent = data.message;
                contactForm.reset();

                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;

                setTimeout(() => {
                    formMessage.className = 'form-message';
                }, 5000);
            })
            .catch(error => {
                formMessage.className = 'form-message error';
                formMessage.textContent = 'Error sending message. Please try again.';
                console.error('Error:', error);

                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
            });
        });
    }
});