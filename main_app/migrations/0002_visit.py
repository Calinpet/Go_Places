# Generated by Django 4.1.2 on 2022-10-23 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('visited', models.CharField(choices=[('1', 'Visited'), ('2', 'Not Visited'), ('3', 'Planing To Visit')], default='1', max_length=1)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.place')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
