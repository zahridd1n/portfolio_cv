from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from . import models


def home(request):
    home = models.Home.objects.last()
    aboutme = models.AboutMe.objects.last()
    social = models.SocialMedia.objects.all()
    context = {
        'home': home,
        'aboutme': aboutme,
        'social': social,
    }
    print(home.cv.name)
    return render(request, 'front/home.html', context)


def download_cv(request):
    try:
        home = models.Home.objects.last()
        if not home or not home.cv:
            raise Http404("CV file not found.")

        file_path = home.cv.path
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='CV.pdf')
        return response
    except FileNotFoundError:
        raise Http404("CV file not found.")


def aboutme(request):
    aboutme = models.AboutMe.objects.last()
    educations = models.Education.objects.all()
    experiences = models.Experience.objects.all()
    skills = models.Skills.objects.all()
    skills = list(skills)
    skills1, skills2 = [], []
    for index, skill in enumerate(skills):

        if index % 2 == 0:
            skills1.append(skill)
        else:
            skills2.append(skill)

    print(skills2)
    context = {
        'aboutme': aboutme,
        'educations': educations,
        'experiences': experiences,
        'skills1': skills1,
        'skills2': skills2,
    }
    return render(request, 'front/aboutme.html', context)


def service(request):
    services = models.Services.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'front/services.html', context)


def portfolio(request):
    portfolios = models.Portfolio.objects.all()
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'front/portfolio.html', context)


def blog(request):
    blogs = models.Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'front/blog.html', context)


def contact(request):
    aboutme = models.AboutMe.objects.last()
    context = {
        'aboutme': aboutme,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = models.Contact.objects.create(name=name, email=email, message=message)

    return render(request, 'front/contact.html', context)
