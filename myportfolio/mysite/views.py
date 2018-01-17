from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import *
from django.core.mail import send_mail


def index(request):
    main_about = About.objects.all()[:1].get()

    skills = Skill.objects.all()
    skills_for_main = []
    for skill in skills:
        if skill.is_on_main:
            skills_for_main.append(skill)

    recommendations = Recommendation.objects.all()

    template = loader.get_template('mysite/index.html')
    context = {
        'about': main_about,
        'skills': skills_for_main,
        'recommendations': recommendations,
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('mysite/contact.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def portfolio(request):
    projects = Project.objects.all()
    arts = Art.objects.all()
    articles = Article.objects.all()

    template = loader.get_template('mysite/portfolio.html')
    context = {
        'projects': projects,
        'arts': arts,
        'articles': articles,
    }
    return HttpResponse(template.render(context, request))


def project(request, project_id):
    project_obj = get_object_or_404(Project, pk=project_id)
    template = loader.get_template('mysite/project.html')
    context = {
        'project': project_obj,
    }
    return HttpResponse(template.render(context, request))


def art(request, art_id):
    art_obj = get_object_or_404(Art, pk=art_id)
    template = loader.get_template('mysite/art.html')
    context = {
        'art': art_obj,
    }
    return HttpResponse(template.render(context, request))


def send_email(request, name, msg, from_email):
    send_mail(
        'PORTFOLIO: You got message from ' + name,
        msg,
        from_email,
        ['tomasz.testowy.gosc@gmail.com'],
    )
    template = loader.get_template('mysite/contact.html')
    return HttpResponse(template.render(request))
