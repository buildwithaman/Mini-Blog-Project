from django.contrib import admin
from .forms import ContactForm
from .models import ContactModel , PostModel

# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["id","name","gmail","message"]
admin.site.register(ContactModel , ContactModelAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id" , "title" , "desc"]
admin.site.register(PostModel , PostModelAdmin)