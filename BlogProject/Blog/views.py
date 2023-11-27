from django.shortcuts import render,get_object_or_404
from .models import Post

# adding paginator to blog --> using built-in Djnago modules
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def post_list(request):
    # getting all published post
    all_post = Post.published_manager.all()

    # adding paginator --> pagination with 5 posts per page
    num_post_per_page = 1
    paginator = Paginator(all_post,num_post_per_page)
    # getting the requested page number --> This parameter contains the requested page number. If the page parameter is not in the GET
    #                                       parameters of the request, we use the default value 1 to load the first page of results.
    page_number = request.GET.get('page_number',1)
    print(request.GET)
    
    try:
        print('try')
        all_post = paginator.page(page_number)
    except EmptyPage:
        print('exceept')
        # Raises EmptyPage if the given page number doesn’t exist.
        # if your page number is out of range , then you see the last existing page
        all_post = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # Raises PageNotAnInteger if the number cannot be converted to an integer by calling int(). 
        # if your page number is out of range , then you see the last existing page
        all_post = paginator.page(paginator.num_pages)
    ##################

    return render(
        request,
        'Blog/post/post_list.xhtml',
        {'posts':all_post}
    )

def post_detail(request,post_year,post_month,post_day,post_slug):
    # post = Post.published_manager.get(id==post_id)
    post = get_object_or_404(Post,
                            status=Post.Status.published,
                            slug=post_slug,
                            publish__year=post_year,
                            publish__month=post_month,
                            publish__day=post_day)
    return render(
        request,
        'Blog/post/post_detail.xhtml',
        {'post':post}
    )