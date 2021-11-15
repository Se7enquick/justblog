from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, CreateView
from django.core.paginator import Paginator

from .models import Post, Comment


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        posts = Post.objects.all().order_by('created')
        return {
            'posts': posts
        }


class PostDetails(DetailView):
    template_name = 'post_details.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_comments = Comment.objects.filter(post=self.object.id)
        paginator = Paginator(post_comments, 5)
        page = self.request.GET.get('page')
        context['comments'] = paginator.get_page(page)
        return context


class CreatePostView(CreateView):
    template_name = 'create_post.html'
    model = Post
    fields = ('title', 'post_text', 'tags')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('/')


class CreateCommentView(CreateView):
    template_name = 'create_comment.html'
    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = Post.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect(f'../../post/{self.kwargs["pk"]}')