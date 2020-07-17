from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    sender_email = forms.EmailField()
    receiver_email = forms.EmailField()
    comments = forms.CharField(required = False, widget = forms.Textarea)
