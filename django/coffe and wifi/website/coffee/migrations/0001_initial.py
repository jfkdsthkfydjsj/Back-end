# Generated by Django 4.2.1 on 2023-05-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CafeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.URLField()),
                ('opens', models.TimeField()),
                ('closes', models.TimeField()),
                ('coffee', models.CharField(choices=[(1, '☕️'), (2, '☕️☕️'), (3, '☕️☕️☕️'), (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️')], default='✘', max_length=5)),
                ('wifi', models.CharField(choices=[(1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪')], default='✘', max_length=5)),
                ('power', models.CharField(choices=[(1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')], default='✘', max_length=5)),
            ],
        ),
    ]
