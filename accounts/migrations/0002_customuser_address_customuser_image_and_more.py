# Generated by Django 4.2.6 on 2023-10-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pics"),
        ),
        migrations.AddField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="date_joined",
            field=models.DateField(auto_now_add=True),
        ),
    ]
