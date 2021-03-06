# Generated by Django 3.2 on 2022-06-21 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new', '0006_alter_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likes', to='new.new', verbose_name='Post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Post')),
            ],
            options={
                'verbose_name': 'yoqimli',
                'verbose_name_plural': 'Yoqimlilar',
            },
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dislikes', to='new.new', verbose_name='Post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dislikes', to=settings.AUTH_USER_MODEL, verbose_name='Post')),
            ],
            options={
                'verbose_name': 'yoqimsiz',
                'verbose_name_plural': 'Yoqimsizlar',
            },
        ),
    ]
