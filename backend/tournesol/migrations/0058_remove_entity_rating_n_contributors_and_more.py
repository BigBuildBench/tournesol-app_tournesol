# Generated by Django 4.2.7 on 2023-11-30 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tournesol", "0057_entitycontext_entitycontextlocale"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="entity",
            name="rating_n_contributors",
        ),
        migrations.RemoveField(
            model_name="entity",
            name="rating_n_ratings",
        ),
    ]
