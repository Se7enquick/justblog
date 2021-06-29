from django.views.generic import TemplateView, DetailView

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