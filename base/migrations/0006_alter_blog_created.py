# Generated by Django 4.2.3 on 2023-09-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0005_alter_comment_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="created",
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
