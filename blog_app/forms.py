from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'name',
            'email',
            'title',
            'content',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }