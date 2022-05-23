from django.forms import ModelForm
from .models import Blog

#create_form


#submit_form

class SubmitForm(ModelForm):

    class Meta:
        model =Blog
        fields =['Author','blog_title','desc','blog_image','blog','Pen_name','tags']
        