# Generated by Django 4.0.4 on 2022-12-01 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0013_module_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.course', verbose_name='course'),
        ),
        migrations.AlterField(
            model_name='hod',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.department', verbose_name='department name'),
        ),
        migrations.AlterField(
            model_name='semester_student_result',
            name='academic_year',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='semester_student_result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.student', verbose_name='student name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.course', verbose_name='course'),
        ),
    ]
