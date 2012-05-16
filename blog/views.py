from django.shortcuts import render_to_response
from blog.models import Post
from django.http import Http404

def index(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	return render_to_response('blog/index.html', {'latest_post_list': latest_post_list})

def archive(request, post_id):
	try:
		p = Post.objects.get(pk=post_id)
		u = Users.objects.get(pk=users_id)
	except Post.DoesNotExist:
		raise Http404
	return render_to_response('blog/archive.html', {'post': p, 'author': u })

