# Generated by Django 4.0.4 on 2023-02-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0040_remove_class_nta_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_module',
            name='class_module_id',
        ),
        migrations.AddField(
            model_name='class_module',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
