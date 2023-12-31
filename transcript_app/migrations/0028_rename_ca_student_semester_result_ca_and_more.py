# Generated by Django 4.0.4 on 2023-02-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0027_rename_overall_result_overallresult_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_semester_result',
            old_name='CA',
            new_name='ca',
        ),
        migrations.RenameField(
            model_name='student_semester_result',
            old_name='FE',
            new_name='fe',
        ),
        migrations.AddField(
            model_name='student_semester_result',
            name='grade',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='student_semester_result',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
