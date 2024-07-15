# Generated by Django 5.0.6 on 2024-07-15 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_uz',
            field=models.TextField(null=True),
        ),
    ]
