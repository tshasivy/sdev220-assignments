from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def post_list(request):
    return render(request, 'blog/post_list.html', {})
