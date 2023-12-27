# Generated by Django 4.0.4 on 2022-12-01 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0012_remove_class_module_module_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='department',
            field=models.ForeignKey(default='C001', on_delete=django.db.models.deletion.CASCADE, to='transcript_app.department', verbose_name='belongs to (department)'),
            preserve_default=False,
        ),
    ]
