# Generated by Django 3.2.5 on 2021-11-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontApp', '0009_alter_blog_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyFocus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
