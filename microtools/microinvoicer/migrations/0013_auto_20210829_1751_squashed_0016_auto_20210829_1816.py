# Generated by Django 3.2.6 on 2021-08-29 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('microinvoicer', '0013_auto_20210829_1751'), ('microinvoicer', '0014_timeinvoice'), ('microinvoicer', '0015_auto_20210829_1806'), ('microinvoicer', '0016_auto_20210829_1816')]

    dependencies = [
        ('microinvoicer', '0012_import_contracts_from_datastore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicecontract',
            old_name='invoice_currency',
            new_name='invoicing_currency',
        ),
        migrations.AddField(
            model_name='servicecontract',
            name='invoicing_description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TimeInvoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('series', models.CharField(max_length=16)),
                ('number', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published'), (2, 'Storno')])),
                ('description', models.CharField(max_length=255)),
                ('issue_date', models.DateField()),
                ('currency', models.CharField(choices=[('eur', 'Euros'), ('usd', 'US Dollars'), ('ron', 'Lei')], max_length=3)),
                ('unit', models.CharField(choices=[('mo', 'Month'), ('hr', 'Hour')], max_length=2)),
                ('unit_rate', models.DecimalField(decimal_places=2, max_digits=16)),
                ('quantity', models.IntegerField()),
                ('conversion_rate', models.DecimalField(decimal_places=4, max_digits=16, null=True)),
                ('buyer', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='microinvoicer.fiscalentity')),
                ('registry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='microinvoicer.microregistry')),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='microinvoicer.fiscalentity')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='microinvoicer.servicecontract')),
            ],
        ),
    ]
