# Generated by Django 3.0.4 on 2020-03-31 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("management", "0004_auto_20200330_1042"),
    ]

    operations = [
        migrations.AlterField(
            model_name="participant",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="related_participant",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]
