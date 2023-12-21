from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def index(request):
	return render(request, 'blog/index.html')

def loginform(request):
	return render(request, 'blog/index.html')

@login_required
def home(request):
	current_user = request.user
	user_id = current_user.id
	print(user_id)
	context = {'user_id': user_id}
	return render(request, 'blog/home.html', context)


def registerform(request):
	return render(request, 'blog/register.html')


class RegisterView(SuccessMessageMixin, CreateView):
	model = User
	fields = ['username','email', 'password' ]
	template_name = 'blog/register.html'
	success_url = reverse_lazy('registerform')
	success_message = "Account was created successfull"

	def form_valid(self, form):
		form.instance.password = make_password(form.instance.password)
		return super().form_valid(form)


from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve, reverse
from django.http import HttpResponseRedirect
from logreg import settings

class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings by setting a tuple of routes to ignore
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), """
        The Login Required middleware needs to be after AuthenticationMiddleware.
        Also make sure to include the template context_processor:
        'django.contrib.auth.context_processors.auth'."""

        if not request.user.is_authenticated:
            current_route_name = resolve(request.path_info).url_name

            if not current_route_name in settings.AUTH_EXEMPT_ROUTES:
                return HttpResponseRedirect(reverse(settings.AUTH_LOGIN_ROUTE))


