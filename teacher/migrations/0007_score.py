# Generated by Django 3.2.8 on 2021-10-21 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_username'),
        ('teacher', '0006_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.exam')),
                ('stu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.student')),
            ],
        ),
    ]
