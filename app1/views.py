from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.


def post(request):
    if request.POST:
        name = request.POST.get('name')
        title = request.POST.get('title')
        content = request.POST.get('content')

        form = Post(name=name, title=title, content=content)

        form.save()
        return redirect("view_post")

    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form})


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
    if request.POST:
        form = PostForm(request.POST, instance=selected_post)
        form.save()
        return redirect('view_post')

    form = PostForm(instance=selected_post)

    return render(request, 'update.html', {"form": form, "selected_post": selected_post})
