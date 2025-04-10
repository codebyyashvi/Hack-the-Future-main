# Generated by Django 5.1.7 on 2025-03-30 06:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0003_flashcard_alter_wordmatchquestion_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SignTypingGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('time_taken', models.FloatField()),
                ('date_played', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='game_type',
            field=models.CharField(choices=[('quiz', 'Quiz'), ('word_match', 'Word Match'), ('flashcard', 'Flashcard')], default='quiz', max_length=20),
        ),
        migrations.CreateModel(
            name='FlashcardScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
