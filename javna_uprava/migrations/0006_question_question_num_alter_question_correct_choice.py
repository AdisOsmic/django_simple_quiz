# Generated by Django 4.0.6 on 2022-07-12 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('javna_uprava', '0005_rename_correct_choice_correct_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_choice',
            field=models.IntegerField(default=0),
        ),
    ]
