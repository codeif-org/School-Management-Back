# Generated by Django 3.2.8 on 2021-10-23 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0009_auto_20211021_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(max_length=200)),
                ('students', models.CharField(max_length=2000)),
                ('topic', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=2000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='teacher.teacher')),
            ],
        ),
    ]