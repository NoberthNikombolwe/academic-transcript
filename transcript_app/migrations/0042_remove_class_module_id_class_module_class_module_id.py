# Generated by Django 4.0.4 on 2023-02-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0041_remove_class_module_class_module_id_class_module_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_module',
            name='id',
        ),
        migrations.AddField(
            model_name='class_module',
            name='class_module_id',
            field=models.CharField(default=1, max_length=20, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
