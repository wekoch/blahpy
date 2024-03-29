from django.template import Context, loader
from blog.models import Post
from django.http import HttpResponse

def index(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('blog/index.html')
	c = Context({
        'latest_post_list': latest_post_list,
	})
	return HttpResponse(t.render(c))
