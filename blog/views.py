# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
#from django.http import HttpResponse
from django.http import *
#from django.template import RequestContext
#from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from .forms import *
from models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

def index(request):
    user = request.user
    #return HttpResponse("Hello, world. You're at the index page.")
    blog = Blog.objects.all().order_by('-pub_date')[:]
    query = request.GET.get("q")
    if query:
        blog = blog.filter(title__icontains = query)
    ff = request.GET.get("ff")
    if ff=="followers":
        follow = Follow.objects.filter(follower=user)
        blog = []
        for fol in follow:
            blog.extend(list(Blog.objects.filter(author=fol.followee).order_by('-pub_date')[:]))
    elif ff=="published":
        blog = blog.all().order_by('-pub_date')[:]
    return render(request, 'blog/home.html', {'blog':blog})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            firstname = userObj['firstname']
            lastname = userObj['lastname']
            email =  userObj['email']
            password =  userObj['password']
            r_password = userObj['repeat_password']
            if r_password != password:
                #return HttpResponseRedirect('/register/')
                raise Http404('Passwords do not match')
            if not (User.objects.filter(username=username).exists()\
               or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                user.last_name = lastname
                user.first_name = firstname
                user.save()
                login(request, user)
                profile = Profile(user=user,
                                  bio="This user hasn't edited their profile yet.",
                                  instagram="www.instagram.com",
                                  fb="www.facebook.com",
                                  twitter="www.twitter.com",
                                 )
                profile.save()
                return HttpResponseRedirect('/profile/' + str(user.id) + '/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})


def signin(request):
    logout(request)
    username = password = ''
    form = UserLoginForm(request.POST)
    if form.is_valid():
        userObj = form.cleaned_data
        username = userObj['username']
        password = userObj['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form' : form})

@login_required
def signout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

@login_required
def profile(request, profile_id):
    if request.user.is_authenticated():
        curr_user = request.user
        profile_user = User.objects.get(pk=profile_id)
        username = profile_user.id
        user_blog_list = Blog.objects.filter(author=username).order_by('-pub_date')[:]
        follow = Follow.objects.filter(follower=curr_user, followee=profile_user)
        profile = Profile.objects.get(user=profile_user)
        return render(request, 'blog/profile.html', {'user' : curr_user,\
                                                     'blogs': user_blog_list,\
                                                     'prof_user': profile_user,\
                                                     'follow': follow,\
                                                     'profile': profile})
    else:
        return HttpResponseRedirect('/')

@login_required
def edit_profile(request):
    if request.user.is_authenticated():
        user = request.user
    if request.method == 'POST':

        form = editProfileForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data.get('bio')
            ig = form.cleaned_data.get('instagram')
            fb = form.cleaned_data.get('fb')
            webpage = form.cleaned_data.get('website')
            twitter = form.cleaned_data.get('twitter')

            user.profile.bio = bio
            user.profile.instagram = ig
            user.profile.fb = fb
            user.profile.website = webpage
            user.profile.twitter = twitter
            user.profile.save()
            return HttpResponseRedirect('/profile/' + str(user.id) + '/')
    else:
        form = editProfileForm(initial = {'bio' : user.profile.bio,
                                          'instagram' : user.profile.instagram,
                                          'fb' : user.profile.fb,
                                          'twitter' : user.profile.twitter,
                                          'website' : user.profile.website,
                                          })
    return render(request, 'blog/edit_profile.html', {'form' : form})

@login_required
def new_blog(request):
    user = request.user
    if request.method == 'POST':
        form = newBlogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            info = form.cleaned_data.get('info')
            cover = form.cleaned_data.get('cover')
            pub_date = timezone.now()
            author = request.user


            b = Blog.objects.create(author = author,\
                                    title=title,\
                                    info=info,\
                                    pub_date=pub_date,\
                                    )
            b.cover = cover
            b.save()
            return HttpResponseRedirect('/profile/' + str(user.id) + '/')
        else:
            raise forms.ValidationError('Woops')
    else:
        form = newBlogForm()
    return render(request,  'blog/createBlog.html', {'form' : form})

@login_required
def blog_posts(request, blog_id):
    try:
        user = request.user
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Specific blog does not exist.")
    posts = Post.objects.filter(parent_blog = blog_id).order_by('-pub_date')[:]
    query = request.GET.get("q")
    if query:
        posts = posts.filter(title__icontains = query)
    fl = request.GET.get("fl")
    if fl == "Likes":
        posts = posts.order_by('-likes')[:]
    else:
        posts = posts.order_by('-pub_date')[:]
    context = {
        'user': user,
        'posts':posts,
        'blog_id':blog_id,
        'blog_author':blog.author,
        'blog':blog,
    }
    return render(request, 'blog/blog_posts.html', context)

@login_required
def single_post(request, post_id, blog_id):
    try:
        user = request.user
        post = Post.objects.get(pk=post_id)
        like = Like.objects.filter(user=user, post=post)

    except Post.DoesNotExist:
        raise Http404("Specific post does not exist.")
    context = {
        'user': user,
        'post': post,
        'blog_id': blog_id,
        'liked': like,
    }
    return render(request, 'blog/single_post.html', context)

@login_required
def new_post(request, blog_id):
    user = request.user
    galery = Images.objects.filter(user = user)
    if request.method == 'POST':
        form = newPostForm(request.POST)
        if form.is_valid():
            try:
                blog = Blog.objects.get(pk=blog_id)
            except Blog.DoesNotExist:
                raise Http404("Specific blog does not exist.")
            title = form.cleaned_data.get('title')
            info = form.cleaned_data.get('info')
            pub_date = timezone.now()
            b = Post.objects.create(parent_blog=blog,\
                                    title=title,\
                                    info=info,\
                                    pub_date=pub_date)
            b.save()
            return HttpResponseRedirect('/profile/' + str(user.id) +\
                                        '/')
        else:
            raise forms.ValidationError('Woops')
    else:
        form = newPostForm()
    return render(request,  'blog/createPost.html', {'form' : form, 'galery': galery})

@login_required
def post_like(request, blog_id, post_id):
        post = Post.objects.get(pk=post_id)
        user = request.user
        if user.is_authenticated():
            if Like.objects.filter(user=user, post=post).exists():
                post.likes = post.likes - 1
                #if post.likes < 0:
                #    post.likes = 0
                post.save()
                l = Like.objects.filter(user=user,\
                                        post=post)
                l.delete()
            else:
                post.likes = post.likes + 1
                post.save()
                l = Like.objects.create(user=user,\
                                        post=post)
                l.save()
        return HttpResponseRedirect('/blog/' + str(blog_id) +\
                                    '/blog_posts/' + str(post_id) +\
                                    '/post/')

@login_required
def follow(request, profile_id):
    follower = request.user
    followee = User.objects.get(pk=profile_id)
    follower_p = Profile.objects.get(user=follower)
    followee_p = Profile.objects.get(user=followee)
    if Follow.objects.filter(follower=follower, followee=followee).exists():
        follower_p.following = follower_p.following - 1
        followee_p.followers = followee_p.followers - 1
        f = Follow.objects.filter(follower=follower,\
                                  followee=followee)
        f.delete()
        followee_p.save()
        follower_p.save()
    else:
        follower_p.following = follower_p.following + 1
        followee_p.followers = followee_p.followers + 1
        f = Follow.objects.create(follower=follower,\
                                  followee=followee)
        f.save()
        followee_p.save()
        follower_p.save()
    return HttpResponseRedirect('/profile/' + str(profile_id))

@login_required
def galery(request, profile_id):
    user = request.user
    #profile_user = User.objects.get(pk=profile_id)
    galery = Images.objects.filter(user=user)
    context = {
        'user': user,
        'galery':galery,
    }
    return render(request, 'blog/galery.html', context)

@login_required
def add_to_galery(request, profile_id):
    user = request.user
    galery = Images.objects.filter(user=user)

    if request.method == 'POST':
        form = addToGaleryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            pub_date = timezone.now()
            b = Images.objects.create(user=user,\
                                    pub_date=pub_date)
            b.image = image
            b.save()
            return HttpResponseRedirect('/profile/' + str(user.id) + '/galery')
        else:
            raise forms.ValidationError('Woops')
    else:
        form = addToGaleryForm()

    context = {
        'user': user,
        'galery':galery,
        'form': form,
    }


    return render(request, 'blog/add2galery.html', context)
