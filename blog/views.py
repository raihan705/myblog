from django.shortcuts import render,get_object_or_404


#from internal application import

from blog.models import Post

# Create your views here.

def post_list(request):

    #posts = Post.published.all() # custom objects manager published is used here.
    #context = {

        #'posts':posts

   # }

    return render(request, 'blog/post/list.html')


def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post,
    status='published',
    publish__year = year,
    publish__month = month,
    publish__day = day
    )
    context = {

        'post':post

    }

    return render(request, 'blog/post/detail.html', context)
