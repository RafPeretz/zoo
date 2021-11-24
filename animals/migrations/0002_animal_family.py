# Generated by Django 3.2.9 on 2021-11-23 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='family',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='family.family'),
            preserve_default=False,
        ),
    ]
