# Create your views here.
from django.views.generic import DetailView, ListView, TemplateView, UpdateView, View
from .models import Blog, BlogPost


class BlogPostList(ListView):
    template_name = "planet/planet_entries.html"
    paginate_by = 25
    model = BlogPost
    context_object_name = 'blogposts'

    def get_queryset(self):
        query = super(BlogPostList, self).get_queryset()
        return query.select_related("blog").order_by("-creation_date")

    def get_context_data(self, **kwargs):
        get = self.request.GET.get
        context = super(BlogPostList, self).get_context_data(**kwargs)
        context['page_title'] = "Planet"
        context['topic'] = 'planet'
        context['limit'] = get('limit', '')
        context['q'] = get('q', '')
        context['sort'] = get('sort', '')
        context['blogs'] = Blog.objects.all().order_by("-list_order")
        return context
