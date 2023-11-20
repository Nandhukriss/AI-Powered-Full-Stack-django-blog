from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# def post(request):
#     if request.POST:
#         name = request.POST.get('name')
#         title = request.POST.get('title')
#         content = request.POST.get('content')

#         form = Post(name=name, title=title, content=content)

#         form.save()
#         return redirect("view_post")
    
#     return render (request,'post.html')

def post(request):
    if request.POST:
        form =PostForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

        return redirect("view_post")

    form=PostForm()
    
    return render (request,'post.html',{'form':form})


def view_post(request):
    post = Post.objects.all()
    p = Paginator(post, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
    # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
    # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}

    return render(request, 'postshow.html', context)

def post_detail(request,id):

    post_detail=get_object_or_404(Post,id=id)

    return render(request, 'post_detail.html',{"post_detail":post_detail})


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
