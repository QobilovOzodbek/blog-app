from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Ismingiz'}),
            'text': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Izohingiz', 'rows': 4}),
        }
