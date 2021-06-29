from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, CreateView

from blog.models import Post


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.all().order_by('created')[:10]
        return {
            'posts': posts
        }


class PostDetails(DetailView):
    template_name = 'post_details.html'
    model = Post


class CreatePostView(CreateView):
    template_name = 'create_post.html'
    model = Post
    fields = ('title', 'post_text', 'tags')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('/')

