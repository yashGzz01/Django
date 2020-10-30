from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.core.paginator import Paginator
from main.models import Post
from main.models import Contact
from main.forms import ContactForm

# from django.core.email import EmailMessage
# from django.conf import settings as conf_settings

from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    posts = Post.objects.all().order_by('-posted_date')
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'main/blog.html', context)

def post(request, post_id=None):
    post = get_object_or_404(Post, id=post_id)
    context = {'post':post}
    return render(request, 'main/post.html', context)

def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        name = instance.name
        email = instance.email
        message = instance.message

        # EmailMessage(
        #     'New message from %s', %name,
        #     'Hi admin, This is my message from this email address: %s\n\n Message: %s', %(email, message),
        #     conf_settings.EMAIL_HOST_USER,
        #     ['tejashvigoyal2910@gmail.com'],
        # ).send()

        form.save()

        messages.success(request, 'Your message has been sent!')

        return redirect('contact')
    context = {'form':form}
    return render(request, 'main/contact.html', context)
