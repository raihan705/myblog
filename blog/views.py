from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView

from django.core.mail import send_mail


#from internal application import

from blog.models import Post, Comment
from blog.forms import EmailPostForm, CommentForm

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

    # list of active comments for the post
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            # cerate comment object but don;t save it to database
            new_comment = comment_form.save(commit= False)
            # assign the comment to post
            new_comment.post = post
            # save the comments to database
            new_comment.save()

    else:
        comment_form = CommentForm()
    context = {

        'post':post, 'comment_form': comment_form, 'comments': comments, 'new_comment': new_comment

    }

    return render(request, 'blog/post/detail.html', context)

def post_share(request, post_id):
    # Retrive post bt id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
                f"{post.title}"

            message = f"Read{post.title} at {post_url}\n\n " \
                f"{cd['name']}\ 's comments: {cd['comments']}"

            send_mail(subject, message, 'ruhan9419@gmail.com', [cd['receiver_email']])
            sent = True

    else:
        form = EmailPostForm()
    context = {
       'form':form, 'sent':sent, 'post':post
    }

    return render(request, 'blog/post/emailpostshare.html', context)
