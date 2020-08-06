from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView
from .form import EmailPostForm
from django.core.mail import send_mail


def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list,3) #3 post in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of result.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page':page,'posts':posts})


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/post/detail.html', {'post':post})

def post_share(request, pk):
    # Retrieve post by id
    #post = get_object_or_404(Post, id=pk, status='published')
    try:
        post = Post.objects.get(id=pk, status='published')
    except Post.DoesNotExist:
        post=None

    sent = False

    if request.method == 'POST':
        #Form was submitted
        form = EmailPostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_url(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'],cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{} comments:{}'.format(post.title, post.url, cd['name'],cd['email'])
            send_mail(subject, message, '050919@myblog.com', [cd['to']])
            sent = True

        else:
            form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post':post,
                                                        'form':form,
                                                        'sent':sent})
    else:
        return render(request, 'blog/post/share.html', {'post':post,
                                                        'sent':sent})