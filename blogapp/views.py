from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import SignupForm, PostForm, EditForm
from .models import Post, Category

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "list.html"
    ordering = ['-post_date']
    # ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = ('title', 'body')


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "add_category.html"
    fields = '__all__'
    # fields = ('title', 'body')


class UpdateView(UpdateView):
    model = Post
    template_name = "update.html"
    form_class = EditForm
    # fields = ['title', 'title_tag', 'body']


class DeleteView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy('list')


def signupfunc(request):
    form = SignupForm(request.POST)
    if request.method == "POST":
        username = form.data['username']
        password = form.data['password']
        if form.is_valid():
            try:
                user = User.objects.create_user(username, '', password)
            except IntegrityError:
                return render(request, "signup.html", {'error': '※このユーザーは登録されています', 'form': form})
            return render(request, 'success.html', {})
    return render(request, "signup.html", {'form': form})


def successfunc(request):
    return render(request, 'success.html', {})
