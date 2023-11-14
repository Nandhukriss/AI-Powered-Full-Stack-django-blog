from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post(request):
    if request.POST:
        name = request.POST.get('name')
        title = request.POST.get('title')
        content = request.POST.get('content')

        form = Post(name=name, title=title, content=content)

        form.save()
        return redirect("view_post")
    
    return render (request,'post.html')


def view_post(request):
    post = Post.objects.all()
    context = {
        "posts": post
    }

    return render(request, 'postshow.html', context)


def delete_post(request, id):

    get_post = get_object_or_404(Post, pk=id)
    get_post.delete()

    return redirect("view_post")


def edit_post(request, id):
    selected_post = get_object_or_404(Post, pk=id)

    if request.method == 'POST':
        
        name = request.POST.get('name')
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Update the selected post with the new data
        selected_post.title = title
        selected_post.name = name
        selected_post.content = content
        selected_post.save()

        return redirect('view_post')

    
    return render(request, 'update.html', {'selected_post': selected_post})
