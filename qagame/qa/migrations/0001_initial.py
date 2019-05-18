# Generated by Django 2.2 on 2019-05-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('no_Q', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('no_remove', models.IntegerField(default=0)),
                ('no_hint', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_id', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=10)),
                ('topic', models.CharField(max_length=500)),
                ('optionA', models.CharField(max_length=500)),
                ('optionB', models.CharField(max_length=500)),
                ('optionC', models.CharField(max_length=500)),
                ('optionD', models.CharField(max_length=500)),
                ('Answer', models.CharField(max_length=500)),
                ('hint', models.CharField(max_length=500)),
                ('remove', models.CharField(max_length=10)),
            ],
        ),
    ]
