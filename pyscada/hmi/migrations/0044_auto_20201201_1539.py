# Generated by Django 2.2.8 on 2020-12-01 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0043_auto_20201201_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='x_axis_var',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='x_axis_var', to='pyscada.Variable'),
        ),
    ]