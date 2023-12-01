from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@login_required(login_url='login')
@csrf_protect
def post(request):
    if request.POST:
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.name = request.user
            post.save()

        return redirect("view_post")

    user_posts= Post.objects.filter(name=request.user)
    form=PostForm()
    
    return render (request,'post.html',{'form':form,'user_posts':user_posts})


def view_post(request):
    
    all_posts = Post.objects.all().order_by('-date_added')
    # Filter posts based on category
    category = request.GET.get('category', '')

    if category:
        all_posts = all_posts.filter(Category=category).order_by('-date_added')
    
    p = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
    # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
    # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    
    # Filter admin posts based on the admin user
    admin_user = get_object_or_404(User, username='nandhu')
    admin_posts = Post.objects.filter(name=admin_user).order_by('-date_added').first()

    latest_Post = Post.objects.order_by('-date_added')[:2]
    context = {'page_obj': page_obj,'latest_posts':latest_Post,'admin_posts':admin_posts}

    return render(request, 'postshow.html', context)

def post_detail(request,id):

    post_detail=get_object_or_404(Post,id=id)

    return render(request, 'post_detail.html',{"post_detail":post_detail})

@login_required(login_url='login')
def delete_post(request, id):

    get_post = get_object_or_404(Post, pk=id)
    get_post.delete()

    return redirect("home")

@login_required(login_url='login')
@csrf_protect
def edit_post(request, id):
    selected_post = get_object_or_404(Post, pk=id)

    if request.POST:
        edit=PostForm(request.POST,request.FILES,instance=selected_post)
        if edit.is_valid():
            edit.save()
        return redirect('home')
    
    edit=PostForm(instance=selected_post)

    
    return render(request, 'update.html', {'edit': edit})

def about(request):

    return render(request,'about.html')


def error_404_view(request, exception):
   

    return render(request, '404.html')