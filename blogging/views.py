
from django.shortcuts import render
from blogging.models import Blog
from user.models import Profile
from blogging.models import Tags
# Create your views here.
def Home(request):
  tag= Tags.objects.all()
  work=Blog.objects.order_by('-upload')[:6]
  params={'work':work,'tag':tag}
  return render(request,"main.html", params)

# view for author
def authors(request):
    author=Profile.objects.all()
    tag=Tags.objects.all()
    a_pms={'author':author,'tag':tag}
    return render(request, "author.html",a_pms)

#view for signin page
def signin(request):
    return render(request,"newsignin.html")

#view for signin page
def signup(request):
    return render(request,"signup.html")

def Read(request,pk):
    post=Blog.objects.filter(id=pk).first()
    other =Blog.objects.filter(Author_id=request.user.id).first()
    read={'post':post,'other':other}
    return render(request,"read.html",read)