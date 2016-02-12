# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 17:13
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', core.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_like_at', models.DateTimeField(blank=True, null=True)),
                ('last_dislike_at', models.DateTimeField(blank=True, null=True)),
                ('liked', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TitledImage',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('subscription_id', models.IntegerField()),
                ('object_id', models.CharField(blank=True, max_length=180, null=True)),
                ('subscription_object', models.CharField(blank=True, max_length=180, null=True)),
                ('media_username', models.CharField(blank=True, max_length=180, null=True)),
                ('media_profile_picture', models.CharField(blank=True, max_length=180, null=True)),
                ('media_user_id', models.CharField(blank=True, max_length=180, null=True)),
                ('media_standard_resolution_url', models.CharField(blank=True, max_length=180, null=True)),
                ('media_like_count', models.IntegerField(blank=True, null=True)),
                ('media_id', models.CharField(blank=True, max_length=180, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='titledimage',
            unique_together=set([('id', 'subscription_id')]),
        ),
        migrations.AddField(
            model_name='like',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estimated_images', to='core.TitledImage'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
