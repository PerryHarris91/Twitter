from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import Postform


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        # If the form is vaild
        if form.is_valid():
           # Yes, Save
           form.save()
           # Redirect to Home
           return HttpResponseRedirect('/')
        else:
           # No, Show Error
           return HttpResponseRedirect(form.errors.as_json()) 

    # Get all post, limit = 20
    posts = Post.objects.all()[:20]

    # Show
    return render(request, 'posts.html', {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    # If the method is POST
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES, instance=post)
        # If the form is vaild
        if form.is_valid():
           # Yes, Save
           form.save()
           # Redirect to Home
           return HttpResponseRedirect('/')
        else:
           # No, Show Error
           return HttpResponseRedirect(form.errors.as_json()) 


    # Show
    return render(request, 'edit.html', {'post': post})



def likes(request, post_id):
    post = Post.objects.get(id = post_id)
    post.like +=1
    post.save()
    return HttpResponseRedirect('/')