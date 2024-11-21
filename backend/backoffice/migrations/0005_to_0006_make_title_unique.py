# Generated by Django 4.1.9 on 2023-06-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("backoffice", "0005_make_title_unique"),
        ("backoffice", "0006_remove_talkentry_private_talkentry_public"),
    ]

    dependencies = [
        ("backoffice", "0004_to_0005_title_required"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talkentry",
            name="name",
            field=models.SlugField(
                blank=True,
                help_text="Used as an URL slug. Leave it blank to automatically build it from the title.",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="talkentry",
            name="title",
            field=models.CharField(
                help_text="The title of the Talk.", max_length=255, unique=True
            ),
        ),
        migrations.RemoveField(
            model_name="talkentry",
            name="private",
        ),
        migrations.AddField(
            model_name="talkentry",
            name="public",
            field=models.BooleanField(
                default=False, help_text="If False, the Talk should not be returned by the API."
            ),
        ),
    ]