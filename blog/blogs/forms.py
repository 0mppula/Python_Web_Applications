from django import forms


from .models import BlogPost

class BlogPost(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Blog Title:', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'placeholder': 'blog content...', 
        'cols': 50}), }
        