'use strict';

class ContactForm {
    constructor() {
        this.form = document.getElementById('contactForm');
        this.formMessage = document.getElementById('formMessage');
        this.isSubmitting = false;
        this.init();
    }

    init() {
        if (!this.form) {
            console.warn('Contact form not found');
            return;
        }
        
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    }

    async handleSubmit(e) {
        e.preventDefault();

        if (this.isSubmitting) return;
        if (!this.form.reportValidity()) {
            this.showMessage('Please fill in all required fields.', 'error');
            return;
        }
        const formData = {
            name: this.getFieldValue('name'),
            email: this.getFieldValue('email'),
            phone: this.getFieldValue('phone'),
            subject: this.getFieldValue('subject'),
            message: this.getFieldValue('message')
        };

        if (!this.isValidEmail(formData.email)) {
            this.showMessage('Please enter a valid email address.', 'error');
            return;
        }

        this.isSubmitting = true;
        this.setSubmitButtonState(true);

        try {
            const response = await this.submitForm(formData);
            const data = await response.json();

            if (response.ok && data.success) {
                this.showMessage(data.message || 'Message sent successfully! 🎉', 'success');
                this.form.reset();
            } else {
                this.showMessage(data.message || 'Failed to send message. Please try again.', 'error');
            }
        } catch (error) {
            console.error('Form Submission Error:', error);
            this.showMessage('Network error. Please check your connection and try again.', 'error');
        } finally {
            this.isSubmitting = false;
            this.setSubmitButtonState(false);
        }
    }

    submitForm(formData) {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || '';
        
        return fetch('/api/contact/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(formData)
        });
    }

    getFieldValue(fieldName) {
        const field = document.getElementById(fieldName);
        return field ? field.value.trim() : '';
    }

    isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    showMessage(message, type) {
        if (!this.formMessage) return;

        this.formMessage.textContent = message;
        this.formMessage.className = `form-message ${type}`;
        this.formMessage.style.display = 'block';
        if (type === 'success') {
            setTimeout(() => {
                this.formMessage.style.display = 'none';
            }, 5000);
        }
    }

    setSubmitButtonState(isDisabled) {
        const submitBtn = this.form?.querySelector('button[type="submit"]');
        if (!submitBtn) return;

        submitBtn.disabled = isDisabled;
        
        if (isDisabled) {
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        } else {
            submitBtn.innerHTML = '<span>Send Message</span><i class="fas fa-arrow-right"></i>';
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new ContactForm();
    console.log('📝 Contact form initialized');
});