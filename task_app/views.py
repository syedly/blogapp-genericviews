from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, RedirectView, UpdateView
from .forms import CustomUserCreationForm, BlogForm, CommentForm, FAQForm, replyForm
from django.urls import reverse_lazy
from .models import blog, comment, faq, reply
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View


def index(request):
    return render(request, 'index.html')

class HomeView(CreateView):
    form_class = BlogForm
    template_name = 'home.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = blog.objects.filter(user=self.request.user)
        return context

class DeleteBlogView(DeleteView):
    model = blog
    success_url = reverse_lazy('home')

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class Blog(LoginRequiredMixin,ListView):
    model = blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    
class BlogUpdate(UpdateView):
    model = blog
    template_name = 'blog_update.html'
    fields = ['title', 'image', 'content']
    success_url = reverse_lazy('home')

class BlogLikeView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        blog_post = get_object_or_404(blog, pk=pk)  
        
        if self.request.user in blog_post.like.all():
            blog_post.like.remove(self.request.user) 
        else:
            blog_post.like.add(self.request.user)  
        
        return reverse_lazy('read_blog', kwargs={'pk': pk})  
    
class ReadBlog(LoginRequiredMixin, DetailView):
    model = blog
    template_name = 'read_blog.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = comment.objects.filter(blog=self.object) 
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'read_blog.html'  
    success_url = reverse_lazy('read_blog')

    def form_valid(self, form):
        form.instance.blog = get_object_or_404(blog, pk=self.kwargs['pk'])  
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('read_blog', kwargs={'pk': self.kwargs['pk']}) 

class FAQView(CreateView):
    template_name = 'faq.html'
    form_class = FAQForm
    success_url = reverse_lazy('faq') 

    def form_valid(self, form):
        faq = form.save(commit=False)
        faq.user = self.request.user  
        faq.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = faq.objects.all()  
        context['replies'] = reply.objects.all()
        return context

class FAQReplyView(View):
    
    def post(self, request, *args, **kwargs):
        faq_id = kwargs.get('id') 
        faq_instance = get_object_or_404(faq, id=faq_id)
        reply_content = request.POST.get('reply') 
        if reply_content:
            Reply = reply.objects.create(user=request.user, question=faq_instance, reply=reply_content)
            Reply.save()
        return HttpResponseRedirect(reverse('faq'))
    
# class SearchBlog(DetailView):
#     model = blog
#     slug_field = 'title'
#     slug_url_kwarg = 'title'
#     template_name = 'searched_blog.html'

class SearchBlog(ListView):
    model = blog
    template_name = 'searched_blog.html' 
    context_object_name = 'blogs'  

    def get_queryset(self):
        query = self.request.GET.get('query')  
        if query:
            return blog.objects.filter(title__icontains=query)
        return blog.objects.all() 
