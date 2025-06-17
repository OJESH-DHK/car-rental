from django import forms
from app.models import ContactDetail, Blog


class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = ['phone', 'email', 'address', 'facebook', 'instagram', 'twitter']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
        }

from app.models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'position', 'testimonial', 'person_image']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title', 'content', 'image'
        ]
