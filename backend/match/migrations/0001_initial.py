# Generated by Django 5.1.6 on 2025-02-16 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_user1', to='user_profile.userprofile')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_user2', to='user_profile.userprofile')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('user1', 'user2')},
            },
        ),
    ]
