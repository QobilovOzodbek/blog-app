from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import *

tags = None # placeholder
def home(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home.html', {"posts": posts, "tags": tags})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post.get_absolute_url())  # sahifani yangilash
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'tag_detail.html', {"tag": tag, "posts": posts})

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Bu yerda siz xabarni saqlash yoki email yuborish kodini qo'shishingiz mumkin
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')