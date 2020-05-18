from django.shortcuts import render, redirect 
from .models import Post
import datetime

def index_defined_in_view (request):
    posts= Post.objects.all()
    count_movie=0
    count_drama=0
    count_entertainment=0
    for post in posts:
        if post.genre== 'movie':
           count_movie+=1
        elif post.genre == 'drama':
            count_drama+=1
        else:
             count_entertainment+=1
    return render (request, 'index.html',{'count_movie_in_html':count_movie, 'count_drama_in_html':count_drama,'count_entertainment_in_html':count_entertainment})

def new_defined_in_view(request):
    if request.method== 'POST':
        print(request.POST)
        new_post = Post.objects.create(
            genre = request.POST['genre'],
            title = request.POST['title'],
            content =request.POST['content'],
            time = datetime.datetime.now()
        )
        return redirect('detail_i_will_use_in_html',primary_key_of_the_post_that_i_clicked= new_post.pk)

    else:
        return render(request, 'new.html')

def detail_defined_in_view(request,primary_key_of_the_post_that_i_clicked):
    post=Post.objects.get(pk=primary_key_of_the_post_that_i_clicked)
    return render(request,'detail.html',{'a_post_i_will_use_in_html':post})

    
def movie_defined_in_view(request):
    movie_posts=Post.objects.filter(genre='movie')
    return render(request,'detail.html',{'movie_posts_i_will_use_in_html':movie_posts})

def drama_defined_in_view(request):
    drama_posts=Post.objects.filter(genre='drama')
    return render(request,'detail.html',{'drama_posts_i_will_use_in_html':drama_posts})

def entertainment_defined_in_view(request):
    entertainment_posts=Post.objects.filter(genre='entertainment')
    return render(request,'detail.html',{'entertainment_posts_i_will_use_in_html':entertainment_posts})
# Create your views here.
