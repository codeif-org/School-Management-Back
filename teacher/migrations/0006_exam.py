# Generated by Django 3.2.8 on 2021-10-21 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('classSection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.classsection')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.teacher')),
            ],
        ),
    ]
