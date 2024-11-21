# Generated by Django 3.2.3 on 2021-06-15 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_degree_expertise_expertisekeyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferences',
            name='backfire_risk',
            field=models.FloatField(default=0.0, help_text='Resilience to backfiring risks', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='backfire_risk_enabled',
            field=models.BooleanField(default=False, help_text='backfire_risk given for ratings'),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='better_habits',
            field=models.FloatField(default=0.0, help_text='Encourages better habits', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='better_habits_enabled',
            field=models.BooleanField(default=False, help_text='better_habits given for ratings'),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='diversity_inclusion',
            field=models.FloatField(default=0.0, help_text='Diversity and Inclusion', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='diversity_inclusion_enabled',
            field=models.BooleanField(default=False, help_text='diversity_inclusion given for ratings'),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='engaging',
            field=models.FloatField(default=0.0, help_text='Engaging and thought-provoking', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='engaging_enabled',
            field=models.BooleanField(default=False, help_text='engaging given for ratings'),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='entertaining_relaxing',
            field=models.FloatField(default=0.0, help_text='Entertaining and relaxing', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='entertaining_relaxing_enabled',
            field=models.BooleanField(default=False, help_text='entertaining_relaxing given for ratings'),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='importance',
            field=models.FloatField(default=0.0, help_text='Important and actionable', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='importance_enabled',
            field=models.BooleanField(default=False, help_text='importance given for ratings'),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='largely_recommended',
            field=models.FloatField(default=0.0, help_text='Should be largely recommended', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='largely_recommended_enabled',
            field=models.BooleanField(default=True, help_text='largely_recommended given for ratings'),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='layman_friendly',
            field=models.FloatField(default=0.0, help_text='Layman-friendly', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='layman_friendly_enabled',
            field=models.BooleanField(default=False, help_text='layman_friendly given for ratings'),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='pedagogy',
            field=models.FloatField(default=0.0, help_text='Clear and pedagogical', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='pedagogy_enabled',
            field=models.BooleanField(default=False, help_text='pedagogy given for ratings'),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='reliability',
            field=models.FloatField(default=0.0, help_text='Reliable and not misleading', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='reliability_enabled',
            field=models.BooleanField(default=False, help_text='reliability given for ratings'),
        ),
    ]