from django.shortcuts import render_to_response
from blog.models import Post, Users
from django.http import Http404

def index(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	u = Users.objects.all()
	return render_to_response('blog/index.html', {'latest_post_list': latest_post_list,
												   'user_info': u})

def archive(request, post_id):
	try:
		p = Post.objects.get(pk=post_id)
		u = Users.objects.get(pk=p.author_id)
	except Post.DoesNotExist:
		raise Http404
	return render_to_response('blog/archive.html', {'post': p, 'author': u })

def profile(request, users_id):
	try:
		user_info = Users.objects.get(pk=users_id)
	except:
		raise Http404
	return render_to_response('blog/profile.html', {'user_info': user_info})

def pageviews(request, file_name):
	return render_to_response('blog/' + file_name + '.html')
