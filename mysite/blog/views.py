from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        #num_my_posts = Post.objects.filter(author=self.request.user).count()
        num_posts = Post.objects.all().count()
        num_authors = User.objects.annotate(post_count=Count('blog_posts')).filter(post_count__gt=0).count()
        num_views = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_views + 1

        #context['num_my_posts'] = num_my_posts
        context['num_posts'] = num_posts
        context['num_views'] = num_views
        context['num_authors'] = num_authors

        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'



# class AuthorPosts(LoginRequiredMixin, generic.ListView):
#     model = PostInstance
#     template_name = 'profile.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return PostInstance.objects.filter(user=self.request.user)

# class PostCreate(CreateView):
#     model = Post
#     fields = '__all__'
#
#
# class PostUpdate(UpdateView):
#     model = Post
#     fields = ['title', 'content', 'status']
#
#
# class PostDelete(DeleteView):
#     model = Post
#     success_url = reverse_lazy('authors')

