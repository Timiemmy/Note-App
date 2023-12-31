# Generated by Django 4.2.6 on 2023-10-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True,
                default="img/default-profile-picture1.jpg",
                null=True,
                upload_to="profile_pics",
            ),
        ),
    ]
