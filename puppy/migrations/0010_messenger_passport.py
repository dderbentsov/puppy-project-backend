# Generated by Django 3.2 on 2021-10-18 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('puppy', '0009_career_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('generalmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='puppy.generalmodel')),
                ('series', models.CharField(blank=True, max_length=10, null=True, verbose_name='Серия')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер')),
                ('issued_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('issued_by', models.CharField(blank=True, max_length=200, null=True, verbose_name='Кем выдан')),
                ('issued_by_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Код подразделения')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passport', to='puppy.person')),
            ],
            options={
                'verbose_name': 'Паспорт',
                'verbose_name_plural': 'Паспорта',
            },
            bases=('puppy.generalmodel',),
        ),
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('generalmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='puppy.generalmodel')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название')),
                ('is_active', models.BooleanField(verbose_name='Действующий')),
                ('uid', models.CharField(max_length=200, verbose_name='UID')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messenger', to='puppy.person')),
            ],
            options={
                'verbose_name': 'Мессенджер',
                'verbose_name_plural': 'Мессенджеры',
            },
            bases=('puppy.generalmodel',),
        ),
    ]