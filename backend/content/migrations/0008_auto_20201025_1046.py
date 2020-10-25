# Generated by Django 2.2.16 on 2020-10-25 13:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_atividade'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventoAgendado',
            fields=[
                ('id_evento', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField(blank=True, null=True)),
                ('titulo', models.CharField(max_length=200)),
                ('local', models.CharField(max_length=200)),
                ('link', models.URLField(default=' ')),
            ],
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='local',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='data_final',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='data_inicial',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='link',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='titulo',
        ),
        migrations.AddField(
            model_name='evento',
            name='descricao',
            field=models.TextField(default=' '),
        ),
    ]
