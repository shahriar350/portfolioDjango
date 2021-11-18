from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from FrontApp.models import Profile, Education, Research, Project, SocialMedia, Training, MySkill, LearningMap, Blog,KeyFocus


def indexPage(request):
    profile = Profile.objects.last()
    educations = Education.objects.all()
    researches = Research.objects.all()
    socialMedia = SocialMedia.objects.all()
    projects = Project.objects.all()
    trains = Training.objects.all()
    skills = MySkill.objects.all()
    keys = KeyFocus.objects.all()
    maps = LearningMap.objects.order_by('date')
    return render(request, 'index.html',
                  {'profile': profile, 'educations': educations,
                   'researches': researches, 'projects': projects, 'socialmedias': socialMedia, 'trainings': trains,
                   'skills': skills, 'maps': maps,'keys': keys})


class BlogPage(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        return render(request, 'all_blog.html', {'blogs': blogs})


def blog_single(request, id=None):
    if request.method == 'GET':
        if id is not None:
            blog = Blog.objects.get(pk=id)
            return render(request, 'single_blog.html', {'blog': blog})
