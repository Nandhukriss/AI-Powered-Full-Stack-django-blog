# Generated by Django 4.2.6 on 2023-11-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_post_content_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(),
        ),
    ]
