# Generated by Django 4.2.2 on 2023-07-04 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0002_favoritebook"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookauthor",
            options={
                "verbose_name": "writer and book",
                "verbose_name_plural": "writer and books",
            },
        ),
        migrations.RemoveField(
            model_name="favoritebook",
            name="book",
        ),
        migrations.AddField(
            model_name="favoritebook",
            name="books",
            field=models.ManyToManyField(to="app.book"),
        ),
        migrations.AlterField(
            model_name="favoritebook",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite_books",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]