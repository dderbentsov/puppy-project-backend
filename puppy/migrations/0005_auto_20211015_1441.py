# Generated by Django 3.2 on 2021-10-15 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('puppy', '0004_auto_20210930_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('generalmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='puppy.generalmodel')),
                ('address_plain', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Адрес')),
                ('is_active', models.BooleanField(verbose_name='Действующий')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
            bases=('puppy.generalmodel',),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='person',
            name='insurance_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SNILS'),
        ),
        migrations.AlterField(
            model_name='person',
            name='second_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Second Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='tax_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='INN'),
        ),
    ]