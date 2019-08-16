# Generated by Django 2.2.4 on 2019-08-16 15:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assignment', '__first__'),
        ('teacher', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=10, unique=True)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, choices=[('', 'Select Year'), ('firstyear', 'First Year'), ('secondyear', 'Second Year'), ('thirdyear', 'Third Year'), ('fourthyear', 'Fourth Year')], default='', max_length=10, null=True)),
                ('branch', models.CharField(blank=True, choices=[('', 'Select Branch'), ('cse', 'Computer Engg.'), ('ee', 'Electrical Engg.'), ('ece', 'Electronics and Comm. Engg.'), ('me', 'Mechanical Engg.'), ('pie', 'Production and Industial Engg.'), ('ce', 'Civil Engg.')], default='', max_length=30, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('rollno', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 8', regex='^.{8}$')])),
                ('my_classes', models.ManyToManyField(blank=True, to='teacher.TeachersClassRoom')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_add_solution', 'can add solution to a assignment'), ('can_view_classroom', 'can view classroom page'), ('can_view_assignment', 'can view assignment')),
            },
        ),
        migrations.CreateModel(
            name='SolutionFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='submissions/')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Solution')),
            ],
        ),
        migrations.AddField(
            model_name='solution',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
