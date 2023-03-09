# Generated by Django 4.1.4 on 2023-01-15 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('funcionario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tem_almoco', models.BooleanField()),
                ('tem_jantar', models.BooleanField()),
                ('data', models.DateField()),
                ('funciona', models.BooleanField()),
                ('almoco', models.ManyToManyField(blank=True, related_name='tarde', to='refeicao.componente')),
                ('funcionario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('jantar', models.ManyToManyField(blank=True, related_name='noite', to='refeicao.componente')),
            ],
        ),
    ]