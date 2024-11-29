from django import forms
from django.contrib.auth.models import User #Import the default User model for authentication
from .models import Article

#Contact form for user input
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your message")

#A model-based Registration form
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        clean_data = super().clean() # Call the parent class's clean method
        if clean_data.get('password') != clean_data.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match!!")
        return clean_data
    
# A model-based form for creating or editing articles
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author']