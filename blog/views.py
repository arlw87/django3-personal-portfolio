from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):

        #grabs all the objects from the database
    blogs = Blog.objects.all()
    num = len(blogs)
    #blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'count':num})

def blog(request, blog_id):
    #get the data object making the id of blog_id
    #blog = Blog.objects.get(id=blog_id)
    #this is better as it returns a 404 if there is now mantching blog # IDEA:
    #pk standing for primary key, so the primary key for this get is equal to blog_id
    blog = get_object_or_404(Blog, pk=blog_id)
    return render (request, 'blog/detail.html', {'blog':blog})
