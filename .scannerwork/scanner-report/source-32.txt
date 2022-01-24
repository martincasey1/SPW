from django.contrib.auth import login
from django.db.models import fields
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment, Gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, galleryForm
from django.views.decorators.http import require_GET, require_POST, require_http_methods, require_safe
from .forms import ContactForm
from django.core.mail import message, send_mail, BadHeaderError
from web_project import settings




# Create your views here.
@require_POST
def like_view(request,pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user= get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        form.instance.name=self.request.user
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@require_safe
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def gallery_image_view(request):

    if request.method == 'POST':
        form = galleryForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = galleryForm()
    return render(request, 'blog/gallery.html', {'form' : form})

@require_GET
def display_gallery_images(request):
  
    if request.method == 'GET':
  
        # getting all the objects of gallery.
        gallery = Gallery.objects.all() 
        return render(request, 'blog/display_gallery_images.html',
                     {'gallery_image' : gallery}) 
@require_GET
def success(request):
    return HttpResponseRedirect(reverse('gallery_list')) 


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email_address'],
            'message':form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, body['email'], [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("blog-home")

    form = ContactForm()
    return render(request, "blog/contact.html", {'form':form})
 


