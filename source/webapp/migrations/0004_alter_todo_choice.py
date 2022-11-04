# Generated by Django 4.1.3 on 2022-11-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_todo_deadline_todo_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='choice',
            field=models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=20, verbose_name='Choice'),
        ),
    ]