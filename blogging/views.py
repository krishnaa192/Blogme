
from django.shortcuts import render,redirect
from blogging.models import Blog
from user.models import Profile
from blogging.models import Tags
from django.contrib.auth.decorators import login_required
from .forms import SubmitForm
# Create your views here.

def Home(request):
  tag= Tags.objects.all()
  work=Blog.objects.order_by('-upload')[:6]
  params={'work':work,'tag':tag}
  return render(request,"main.html", params)

# view for author
@login_required(login_url="login")
def authors(request):
    author=Profile.objects.all()
    tag=Tags.objects.all()
    a_pms={'author':author,'tag':tag}
    return render(request, "author.html",a_pms)

#view for signin page
@login_required(login_url="login")
def Read(request,pk):
    post=Blog.objects.filter(id=pk).first()
    other =Blog.objects.filter(Author_id=request.user.id).first()
    read={'post':post,'other':other}
    return render(request,"read.html",read)

def Submit_Form(request):
  form=SubmitForm()
  if request.method=='POST':
    form=SubmitForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('Home')
  context ={'form':form}
  return render(request,"submitform.html",context)

def update_blog(request,pk):
  blog=Blog.objects.get(id=pk)
  form=SubmitForm(instance=blog)
  if request.method=='POST':
    form=SubmitForm(request.POST,instance=blog)
    if form.is_valid():
      form.save()
      return redirect('Home')
  context ={'form':form}
  return render(request,"submitform.html",context)

def delete_blog(request,pk):
 blog=Blog.objects.get(id=pk)
 if request.method == 'POST':
    blog.delete()
    return redirect('Home')
 context={'blog':blog}
 return render(request,"blog_delete.html",context)
