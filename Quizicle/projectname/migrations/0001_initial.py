# Generated by Django 5.1.5 on 2025-02-24 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
                ('PointsForQuestion', models.IntegerField()),
                ('AdditionalImage', models.ImageField(blank=True, null=True, upload_to='question_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuizName', models.CharField(max_length=150)),
                ('QuizMaximumPoints', models.IntegerField()),
                ('QuestionCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer', models.CharField(max_length=255)),
                ('Correct', models.BooleanField(default=False)),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectname.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='Quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectname.quiz'),
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=150)),
                ('Result', models.IntegerField()),
                ('Quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectname.quiz')),
            ],
        ),
    ]
