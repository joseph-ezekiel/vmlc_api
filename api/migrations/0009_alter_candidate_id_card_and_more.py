# Generated by Django 5.2.4 on 2025-07-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_leaderboardsnapshot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="id_card",
            field=models.ImageField(
                blank=True, null=True, upload_to="candidate_id_cards/"
            ),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="profile_photo",
            field=models.ImageField(
                blank=True,
                default="candidate_profile_photos/default.png",
                null=True,
                upload_to="candidate_profile_photos/",
            ),
        ),
        migrations.AlterField(
            model_name="staff",
            name="profile_photo",
            field=models.ImageField(
                blank=True,
                default="staff_profile_photos/default.png",
                null=True,
                upload_to="staff_profile_photos/",
            ),
        ),
    ]
