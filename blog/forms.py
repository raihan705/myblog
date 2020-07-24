from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    sender_email = forms.EmailField()
    receiver_email = forms.EmailField()
    comments = forms.CharField(required = False, widget = forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(
                attrs= {
                    'class': 'form-control'
        }
            ),

           'email': forms.TextInput(
                attrs= {
                    'class': 'form-control'
        }
            ),

            'body': forms.Textarea(
                attrs= {
                    'class': 'form-control', 'rows': 6
        }
            ),
        }
