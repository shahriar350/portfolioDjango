# Generated by Django 3.2.5 on 2021-11-18 09:44

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontApp', '0008_blog_blogcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
