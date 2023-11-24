from django.shortcuts import render,get_object_or_404
from .models import Post


def post_list(request):
    # getting all published post
    all_post = Post.published_manager.all()
    return render(
        request,
        'Blog/post/post_list.xhtml',
        {'posts':all_post}
    )

def post_detail(request,post_id):
    # post = Post.published_manager.get(id==post_id)
    post = get_object_or_404(Post,id=post_id,status=Post.Status.published)
    return render(
        request,
        'Blog/post/post_detail.xhtml',
        {'post':post}
    )