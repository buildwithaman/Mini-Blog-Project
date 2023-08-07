from django import forms
from .models import ContactModel , PostModel
  

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"
        widgets = {
            "message":forms.Textarea(attrs={"rows":7,"class":"form-control mb-2 border border-primary"}),
        } 

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = "__all__"
        widgets = {
            "desc":forms.Textarea(attrs={"class":"form-control mb-2 border-primary"})
        }


