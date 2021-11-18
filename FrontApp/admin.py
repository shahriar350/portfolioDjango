from django.contrib import admin

# Register your models here.
from FrontApp.models import Profile, Education, Project, Research, SocialMedia, Training, MySkill, LearningMap, \
    BlogCategory, Blog, KeyFocus


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    fields = (
        'name',
        'profession',
        'image',
        'cv',
        'email',
        'phone_number',
        'profile',
        'address',
    )


@admin.register(Education)
class AdminEducation(admin.ModelAdmin):
    fields = (
        'type',
        'institute',
        'year',
        'major',
        'result',
    )


@admin.register(Project)
class AdminProjects(admin.ModelAdmin):
    fields = (
        'name',
        'image',
        'technology',
        'link',
        'description',
    )


@admin.register(Research)
class AdminResearch(admin.ModelAdmin):
    fields = (
        'name',
        'link',
        'year',
    )


@admin.register(SocialMedia)
class AdminSocialMedia(admin.ModelAdmin):
    fields = (
        'name',
        'link',
        'icon',
    )


@admin.register(Training)
class AdminTraining(admin.ModelAdmin):
    fields = (
        'name',
        'image',
        'topic',
        'organization',
        'year',
    )


@admin.register(MySkill)
class AdminMySkill(admin.ModelAdmin):
    fields = (
        'name',
        'icon',
        'description',

    )


@admin.register(LearningMap)
class AdminLearningMap(admin.ModelAdmin):
    fields = (
        'date',
        'technology',
        'description',

    )


@admin.register(BlogCategory)
class AdminBlogCategory(admin.ModelAdmin):
    fields = (
        'name',
    )


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    fields = (
        'title',
        'category',
        'description',
    )


@admin.register(KeyFocus)
class AdminKeyFocus(admin.ModelAdmin):
    fields = (
        'name',
    )
