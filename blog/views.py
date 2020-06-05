from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Druzyna
from .models import Miejscowosc
from .models import Pilkarz
from .models import Mecz
from .models import Granie

from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    context = {

        "posts": posts,

    }
    return render(request, 'blog/post_list.html',  context)


def meczyki(request):

    spotkanie = Mecz.objects.all()
    context = {
        "objects_list": spotkanie,

    }
    return render(request, 'blog/mecze.html',  context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})