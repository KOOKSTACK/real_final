# Generated by Django 4.1.7 on 2023-05-24 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_merge_20230524_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionhistory',
            name='question',
        ),
        migrations.DeleteModel(
            name='AnswerHistory',
        ),
        migrations.DeleteModel(
            name='QuestionHistory',
        ),
    ]
