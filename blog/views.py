#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
#from django_modalview.generic.base import ModalTemplateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils import timezone
from django.forms.formsets import formset_factory
from django.forms import inlineformset_factory
#from PIL import Image as PILImg
#from PIL import ImageEnhance as PILImageEnhance
from django.conf import settings
from .models import Post, Comment, Document
from .forms import PostForm, CommentForm, DocumentForm

def set_if_not_none(mapping, key, value):
    if value is not None:
        mapping[key] = value

def get(request):
    sort_pub_date = request.GET.get('published_date')
    sort_group = request.GET.get('grupa')
    sort_params = {}
    set_if_not_none(sort_params, 'published_date_lte', sort_pub_date)
    set_if_not_none(sort_params, 'group', sort_group)

    return Post.objects.filter(**sort_params)

def post_list(request):
    grupa = request.GET.get('grupa')
    #posts_list = Post.objects.filter(**filterargs).order_by('-published_date')
    if grupa == '1':
        posts_list = Post.objects.filter(published_date__lte=timezone.now(), grop_1 = True).order_by('-published_date')
    elif grupa == '2':
        posts_list = Post.objects.filter(published_date__lte=timezone.now(), grop_2 = True).order_by('-published_date')
    elif grupa == '3':
        posts_list = Post.objects.filter(published_date__lte=timezone.now(), grop_3 = True).order_by('-published_date')
    elif grupa == '4':
        posts_list = Post.objects.filter(published_date__lte=timezone.now(), grop_4 = True).order_by('-published_date')
    else:
        posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts_list, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts':posts})

def post_list_rev(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:5]
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})

def post_about(request):
    return render(request, 'blog/about.html')

def post_zapisy(request):
    return render(request, 'blog/zapisy.html')


@login_required
def post_new(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
#    if user is not None:
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect('post_list')
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author=request.user
            if 'send' in request.POST:
                post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect('post_detail', pk=post.pk)
        form = PostForm(request.POST)
        if form.is_valid():
            #post = form.save(commit = False)
            post.text = request.POST['text']
            post.title = request.POST['title']
            if 'grop_0' in request.POST:
                post.grop_0 = request.POST['grop_0']
            else:
                post.grop_0 = False
            if 'grop_1' in request.POST:
                post.grop_1 = request.POST['grop_1']
            else:
                post.grop_1 = False
            if 'grop_2' in request.POST:
                post.grop_2 = request.POST['grop_2']
            else:
                post.grop_2 = False
            if 'grop_2' in request.POST:
                post.grop_3 = request.POST['grop_3']
            else:
                post.grop_3 = False
            if 'grop_4' in request.POST:
                post.grop_4 = request.POST['grop_4']
            else:
                post.grop_4 = False
            if 'grop_5' in request.POST:
                post.grop_5 = request.POST['grop_5']
            else:
                post.grop_5 = False
            post.author= request.user
            if 'send' in request.POST:
                post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

@login_required
def publish(self):
    self.published_date = timezone.now()
    self.save()

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect('post_detail')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author= request.user
            if 'send' in request.POST:
                comment.approve()
            comment.save()
            return redirect('blog.views.post_detail', pk = post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect('blog.views.post_detail', pk = post.pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.text = request.POST['text']
            comment.author= request.user
            # if 'send' in request.POST:
            #    comment.approved_comment = True
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/add_comment_to_post.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)

@login_required
def add_document_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect('blog.views.post_detail', pk = post.pk)
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #document = Document(docfile = request.FILES['docfile'], title=request.POST['name'])
            document = Document(docfile = request.FILES['docfile'])
            #document = form.save(commit=False)
            #file_content = ContentFile(request.FILES['docfile'].read())
            #document.docfile.save(request.FILES['docfile'].name, file_content)
            document.post = post
            #document.docfile = request.FILES['docfile']
            #print request.FILES.get('docfile')
            #document.docfile= Document(docfile = request.FILES['docfile'])
            document.save()
            return redirect('blog.views.post_detail', pk = post.pk)
    else:
        form = DocumentForm()
    return render(request, 'blog/document_edit.html', {'form': form})

@login_required
def document_remove(request, pk):
    document = get_object_or_404(Document, pk=pk)
    post_pk = document.post.pk
    document.delete()
    return redirect('blog.views.post_detail', pk=post_pk)

def index(request):
    """Strona główna aplikacji."""
    return render(request, 'blog/index.html')

def login_user(request):
    """Logowanie użytkownika"""
    from django.contrib.auth.forms import AuthenticationForm
    next_page = request.GET.get('next_page')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, u"Zostałeś zalogowany!")
            return HttpResponseRedirect(next_page)
            # return redirect(reverse('post_list'))

    kontekst = {'form': AuthenticationForm()}
    # return render(request, 'blog/login.html', { 'next_page':next_page }, content_type="application/xhtml+xml" , kontekst)
    return render(request, 'blog/login.html', kontekst)


@login_required
def logout_user(request):
    """Wylogowanie użytkownika"""
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    if request.GET.get('next_page'):
        return HttpResponseRedirect(request.GET.get('next_page'))
    return redirect(reverse('post_list'))

#    if request.method == "POST":
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user = authenticate(username=username, password=password)
#        if user is not None:
#            if user.is_active:
#                login(request, user)
#                state = "You're successfully logged in!"
#                return redirect('/')
#            else:
#                state = "Your account is not active, please contact the site admin."
#        else:
#            state = "Your username and/or password were incorrect."
#    return render(request, 'blog/login.html', {'state':state, 'user':user})
