# Generated by Django 2.2.5 on 2019-10-07 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interactable',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    default='DEFAULT INTERACTABLE', max_length=50)),
                ('description', models.CharField(
                    default='DEFAULT DESCRIPTION', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT ITEM', max_length=50)),
                ('description', models.CharField(
                    default='DEFAULT DESCRIPTION', max_length=500)),
                ('item_type', models.CharField(
                    default='DEFAULT TYPE', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='DEFAULT TITLE', max_length=50)),
                ('description', models.CharField(
                    default='DEFAULT DESCRIPTION', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('currentRoom', models.IntegerField(default=0)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='DEFAULT TITLE', max_length=50)),
                ('description', models.CharField(
                    default='DEFAULT DESCRIPTION', max_length=500)),
                ('description_b', models.CharField(default='', max_length=500)),
                ('planet', models.IntegerField(default=0)),
                ('coord_x', models.IntegerField(default=0)),
                ('coord_y', models.IntegerField(default=0)),
                ('north', models.IntegerField(default=0)),
                ('south', models.IntegerField(default=0)),
                ('east', models.IntegerField(default=0)),
                ('west', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RoomItem',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('last_taken', models.DateTimeField(null=True)),
                ('respawn', models.DurationField(null=True)),
                ('item', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='adventure.Item')),
                ('room', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='adventure.Room')),
            ],
        ),
        migrations.CreateModel(
            name='RoomInteractable',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='DEFAULT STATUS', max_length=50)),
                ('interactable', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='adventure.Interactable')),
                ('room', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='adventure.Room')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerVisited',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='adventure.Player')),
                ('room', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='adventure.Room')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerItem',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('item', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='adventure.Item')),
                ('player', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='adventure.Player')),
            ],
        ),
    ]
