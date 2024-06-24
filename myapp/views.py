from django.shortcuts import render
from .form import PostForm


# Create your views here.
def createPost(request):
    context  = {
        "form": PostForm()
    }
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
        else:
            context = {'form': post_form}
            return render(request, 'myapp/post.html', context)    
    return render(request, 'myapp/post.html', context)