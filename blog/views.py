from django.shortcuts import render_to_response
from blog.models import Post

def index(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	return render_to_response('blog/index.html', {'latest_post_list': latest_post_list})
