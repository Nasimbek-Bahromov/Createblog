# blog create
# blog update
# blog delete
from main import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='index')
def blog_create(request):
    if request.method == 'POST':
        models.Blog.objects.create(
            author = request.user,
            title = request.POST['title'],
            body = request.POST['body'],
            image = request.FILES['image']
        )
        return redirect('index')
    return render(request, 'dashboard/create-blog.html')


@login_required
def blog_update(request, id):
    blog = get_object_or_404(models.Blog, id=id)
    
    if request.method == 'POST':
        new_title = request.POST.get('title', '')
        new_body = request.POST.get('body', '')
        new_image = request.FILES.get('image')

        blog.title = new_title if new_title else blog.title
        blog.body = new_body if new_body else blog.body

        if new_image:
            blog.image = new_image
        
        blog.save()
        
        return redirect('index') 
    
    return render(request, 'dashboard/update-blog.html', {'blog': blog})


@login_required
def blog_delete(request, id):
    models.Blog.objects.get(id=id).delete()
    return redirect('index')


@login_required
def my_blogs(request):
    blogs = models.Blog.objects.filter(author = request.user)
    return render(request, 'dashboard/list-blogs.html', {'blogs':blogs})