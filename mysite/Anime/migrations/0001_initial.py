# Generated by Django 2.2.6 on 2019-10-17 19:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Summary', models.TextField(help_text='introdusca una breve descripcion del Anime', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AnimInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Id para el el anime en particular con los demas', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('anim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Anime.Anim')),
            ],
        ),
        migrations.AddField(
            model_name='anim',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Anime.Author'),
        ),
        migrations.AddField(
            model_name='anim',
            name='genre',
            field=models.ManyToManyField(to='Anime.Genre'),
        ),
    ]
