from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView


#from internal application import

from blog.models import Post

# Create your views here.

def post_list(request):

    posts = Post.published.all() # custom objects manager published is used here.
    paginator = Paginator(posts, 2) # total posts in each page
    page = request.GET.get('page') # Getting the current page number

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:

        #if page is not integer, deliver the first page
        posts = paginator.page(1)

    except EmptyPage:
        # if page is out of range, delivr the last page
        posts = paginator.page(paginator.num_pages)

    context = {

        'posts':posts, 'page':page

    }

    return render(request, 'blog/post/list.html', context)

# this is class based view

'''
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'

'''
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
