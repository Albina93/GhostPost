from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import Post
from .forms import AddPost
import random
import string


def index(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'index.html', {'posts': posts})


def createpost_view(request):
    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            secret_key = "".join(random.choices(
                string.ascii_letters + string.digits, k=6))
            post = Post.objects.create(
                is_roast=data.get('is_roast'),
                content=data.get('content'),
                sec_key=secret_key
            )
            return render(request, 'createpost.html', {'post': post})
    form = AddPost()
    return render(request, 'createpost.html', {'form': form})


def roast_view(request):
    posts = Post.objects.filter(is_roast='True').order_by('-date_created')
    return render(request, 'roast.html', {'posts': posts})


def boast_view(request):
    posts = Post.objects.filter(is_roast='False').order_by('-date_created')
    return render(request, 'boast.html', {'posts': posts})


def sorted_view(request):
    posts = Post.objects.all()
    posts = list(posts)
    posts = sorted(posts, key=lambda x: x.total_votes, reverse=True)
    return render(request, 'sorted.html', {'posts': posts})


def upvote_view(request, upvote_id):
    # print(upvote_id)
    post = Post.objects.get(id=upvote_id)
    post.upvote = post.upvote + 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote_view(request, downvote_id):
    # print(downvote_id)
    post = Post.objects.get(id=downvote_id)
    post.downvote = post.downvote - 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def detail_view(request, sec_key):
    post = Post.objects.get(sec_key=sec_key)
    return render(request, 'detail.html', {'post': post})


def delete_view(request, post_id):
    removed = Post.objects.filter(id=post_id).delete()
    return render(request, 'detail.html', {'removed': removed})
