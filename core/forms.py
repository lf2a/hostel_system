# django
from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your name here'
    }))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'your.email@here.com'
    }))
    message = forms.CharField(label='Message', max_length=800, widget=forms.Textarea(attrs={
        'rows': 6,
        'class': 'form-control',
        'placeholder': 'Your message here...'
    }), )

    def send_mail(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]

        content = f'{email}     {name} sent a message: {message}'
        mail = EmailMessage(
            subject='Contact: help, info, etc...',
            body=content,
            from_email='contact@admin.com',
            to=['contact@admin.com', ],
            headers={'Reply-To': email}
        )
        mail.content_subtype = 'html'
        mail.send()
