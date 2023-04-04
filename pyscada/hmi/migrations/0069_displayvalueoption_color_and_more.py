# Generated by Django 4.2rc1 on 2023-03-30 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0100_device_instrument_handler'),
        ('hmi', '0068_alter_displayvalueoption_timestamp_conversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='displayvalueoption',
            name='color',
            field=models.ForeignKey(blank=True, help_text='Default color if no level defined, can be null.<br>Color < or =< first level, if a level is defined.', null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.color'),
        ),
        migrations.AddField(
            model_name='displayvalueoption',
            name='color_only',
            field=models.BooleanField(default=False, help_text='If true, will not display the value.'),
        ),
        migrations.AddField(
            model_name='displayvalueoption',
            name='gradient',
            field=models.BooleanField(default=False, help_text='Need 1 color option to be defined.'),
        ),
        migrations.AddField(
            model_name='displayvalueoption',
            name='gradient_higher_level',
            field=models.FloatField(default=0, help_text='Color defined above will be used for this level.'),
        ),
        migrations.CreateModel(
            name='DisplayValueColorOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_level', models.FloatField()),
                ('color_level_type', models.PositiveSmallIntegerField(choices=[(0, 'color =< level'), (1, 'color < level')], default=0)),
                ('color', models.ForeignKey(blank=True, help_text='Let blank for no color below the selected level.', null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.color')),
                ('display_value_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hmi.displayvalueoption')),
            ],
            options={
                'ordering': ['color_level', '-color_level_type'],
            },
        ),
        migrations.AddConstraint(
            model_name='displayvaluecoloroption',
            constraint=models.UniqueConstraint(fields=('display_value_option', 'color_level', 'color_level_type'), name='unique_display_value_color_option'),
        ),
    ]