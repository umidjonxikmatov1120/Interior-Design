from django.shortcuts import render, redirect

from pages.forms import ContactModelForms
from pages.models import AboutModel, ImagesModel, ServiceModel, BlogModel, ContactModel


def home_page_view(request):
    about = AboutModel.objects.all().order_by('-created_at')[:3]
    image = ImagesModel.objects.all().order_by('-created_at')[:6]
    services = ServiceModel.objects.all().order_by('-created_at')[:6]
    blogs = BlogModel.objects.all().order_by('-created_at')[:3]
    context = {
        "abouts": about,
        "images": image,
        "services": services,
        "blogs": blogs,

    }
    return render(request, template_name='home.html', context=context)


def contact_page_view(request):
    if request.method == "POST":
        form = ContactModelForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pages:contact")
    else:
        return render(request, template_name='home.html')


def blog_page_view(request):
    blog = BlogModel.objects.all().order_by('-created_at')[:1]
    blogs = BlogModel.objects.all().order_by('-created_at')[:4]
    context = {
        "blogs": blog,
        "blog": blogs,
    }
    return render(request, template_name='blog.html', context=context)
