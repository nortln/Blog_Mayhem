from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator



from .models import Blog, Comment, Category
from .forms import AddComment

def home(request):
    blogs = Blog.objects.order_by("-created")
    recent = Blog.objects.order_by("-created")[:5]
    page = request.GET.get("page")
    categories = Category.objects.all()
    paginator = Paginator(blogs, 5)
    page_obj = paginator.get_page(page)
   
   
    context = {
        "blogs": page_obj,
        "categories": categories,
        "recent": recent,
    }
    return render(request, "blog.html", context)



def page(request, page=1):
    blogs = Blog.objects.order_by("-created")
    paginator = Paginator(blogs, 5)  # Show 10 blogs per page
    page_obj = paginator.get_page(page)
    recent = Blog.objects.order_by("-created")[:5]
    categories = Category.objects.all()

    context = {
        "blogs": page_obj,
        "categories": categories,
        "recent": recent,
    }
    return render(request, "blog.html", context)


def search(request):
    search_query = request.GET.get("search")
    blogs = Blog.objects.filter(title__icontains=search_query)
    recent = Blog.objects.order_by("-created")[:5]
    categories = Category.objects.all()
   
    context = {
        "blogs": blogs,
        "categories": categories,
        "recent": recent,
    }
    return render(request, "blog.html", context)


def details(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comment_set.all()
    comment_length = len(comments)
    context = {
        "blog": blog,
        "comments": comments,
        "comment_length": comment_length,
    
    }
    return render(request, "details.html", context)


def add_blog(request):
    blog = Blog()

    if request.method == "POST":
        id = request.POST["category"]
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.FILES["image"]

        category = Category.objects.get(pk=id)

        blog.category = category
        blog.title = title
        blog.description = description
        blog.image = image
        blog.user = request.user
        blog.save()
    referrer_url = request.META.get("HTTP_REFERER")
    return HttpResponseRedirect(redirect_to=referrer_url)


def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        comment = request.POST["comment"]
        comment = Comment(text=comment, blog=blog, user=request.user)
        comment.save()
    referrer_url = request.META.get("HTTP_REFERER")
    return HttpResponseRedirect(redirect_to=referrer_url)

def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        users = User.objects.all()
        if username not in users:
            if password != confirm_password:
                messages.info(request, "Password does not match!")
                return render(request, "sign-up.html")
            else:
                user = User()
                user.username = username
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect("home")
        else:
            messages.info(request, "User already Exists")
            return render(request, "sign-up.html")




    return render(request, "sign-up.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error_message = "Incorrect Login Credentials"
            return render(request, "sign-in.html", {"error_message": error_message})
    return render(request, "sign-in.html")



def logout_user(request):
    logout(request)
    referrer_url = request.META.get("HTTP_REFERER")
    if referrer_url is not None:
        return HttpResponseRedirect(redirect_to=referrer_url)
    else:
        return HttpResponseRedirect("/")


def delete_blog(request, pk):
    if request.method == "POST":
        blog = Blog.objects.get(pk=pk)
        blog.delete()
    referrer_url = request.META.get("HTTP_REFERER")
    return HttpResponseRedirect(redirect_to=referrer_url)

def profile(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "profile.html", context)




