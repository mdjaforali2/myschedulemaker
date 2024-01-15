# Generated by Django 4.2.7 on 2024-01-15 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_management_app', '0002_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Work', 'Work'), ('Study', 'Study'), ('Personal', 'Personal'), ('Workout', 'Workout'), ('Travel', 'Travel'), ('Appointment', 'Appointment'), ('Entertainment', 'Entertainment')], max_length=20),
        ),
    ]