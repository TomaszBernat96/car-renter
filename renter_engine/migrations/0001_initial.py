# Generated by Django 2.2.7 on 2019-12-08 10:21

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie duże lub małe litery. Ich minimalna ilosć to 3.', regex='^[a-zA-Z]{3,}$')], verbose_name='Ulica')),
                ('house_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie litery i cyfry. Ich minimalna ilość to 3.', regex='^\\w{3,}$')], verbose_name='Numer domu')),
                ('apartment_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie litery i cyfry. Ich minimalna ilość to 3.', regex='^\\w{3,}$')], verbose_name='Numer mieszkania')),
                ('postal_code', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Podany kod pocztowy jest nieprawidłowy. Należy wprowadzić kod pocztowy w następującej formie 00-000.', regex='^\\d{2}\\-\\d{3}$')], verbose_name='Kod pocztowy')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name='Data utworzenia adresu')),
            ],
            options={
                'verbose_name': 'Adres',
                'verbose_name_plural': 'Adresy',
                'ordering': ['city', 'street', '-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie duże lub małe litery. Ich minimalna ilosć to 3.', regex='^[a-zA-Z]{3,}$')], verbose_name='Marka')),
                ('type', models.CharField(choices=[('sedan', 'Sedan'), ('hatchback', 'Hatchback'), ('suv', 'suv'), ('kombi', 'kombi'), ('smart', 'smart')], max_length=9, verbose_name='Typ')),
                ('model', models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie litery i cyfry. Ich minimalna ilość to 3.', regex='^\\w{3,}$')], verbose_name='Model')),
                ('boot_capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(1500)], verbose_name='Pojemność bagażnika')),
                ('person_capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(5)], verbose_name='Ilośc miejsc')),
                ('fuel_type', models.CharField(choices=[('gasoline', 'Benzyna'), ('lpg', 'Lpg'), ('electricity', 'Elektryczność')], max_length=11)),
                ('average_burning', models.FloatField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(16)], verbose_name='Średnie spalanie')),
                ('gearbox_type', models.CharField(choices=[('manual', 'Manualna'), ('auto', 'Automatyczna')], max_length=6, verbose_name='Skrzynia biegów')),
                ('color', models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie duże lub małe litery. Ich minimalna ilosć to 3.', regex='^[a-zA-Z]{3,}$')], verbose_name='Kolor')),
                ('creation_date', models.DateField(verbose_name='Rok produkcji')),
                ('car_add_date', models.DateField(default=datetime.date.today, verbose_name='Data dodania pojazdu do systemu')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Pojazd',
                'verbose_name_plural': 'Pojazdy',
                'ordering': ['creation_date', 'brand', 'model'],
                'unique_together': {('brand', 'type', 'model', 'creation_date', 'fuel_type', 'boot_capacity', 'person_capacity', 'average_burning', 'gearbox_type', 'color')},
            },
        ),
        migrations.CreateModel(
            name='CarDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie litery i cyfry. Ich minimalna ilość to 3.', regex='^\\w{1,3}\\-\\w{2,4}$')], verbose_name='Numer rejestracyjny')),
                ('mileage', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)], verbose_name='Średnie spalanie')),
                ('status', models.CharField(choices=[('available', 'Dostępny'), ('rented', 'Wynajęty'), ('mechanic', 'Przerw techniczna')], max_length=9, verbose_name='Status pojazdu')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('last_geo_lat', models.DecimalField(decimal_places=7, max_digits=10)),
                ('last_geo_lon', models.DecimalField(decimal_places=7, max_digits=10)),
                ('last_update_date', models.DateField(default=datetime.date.today, verbose_name='Data ostatniej aktualizacji')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='renter_engine.Car', verbose_name='Pojazd')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car_details', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Szczegóły pojazdu',
                'verbose_name_plural': 'Szczegóły pojazdów',
                'ordering': ['car', '-last_update_date'],
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('running', 'Trwająca'), ('outdated', 'Przedawniona')], max_length=8, verbose_name='Status oferty')),
                ('value_per_minute', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.05), django.core.validators.MaxValueValidator(0.8)], verbose_name='Należność za minutę wypożyczenia')),
                ('add_date', models.DateField(default=datetime.date.today, verbose_name='Data dodania')),
                ('car_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='renter_engine.CarDetails', verbose_name='Pojazd')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offers', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Oferty',
                'ordering': ['car_details', '-status', '-add_date'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie duże lub małe litery. Ich minimalna ilosć to 3.', regex='^[a-zA-Z]{3,}$')], verbose_name='Imię')),
                ('last_name', models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie duże lub małe litery. Ich minimalna ilosć to 3.', regex='^[a-zA-Z]{3,}$')], verbose_name='Nazwisko')),
                ('email', models.EmailField(max_length=254, verbose_name='Adres e-mail')),
                ('phone_number', models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(message='Podany numer telefonu jest nieprawidłowy. Numer musi zostać wprowadzony w następującej formie 000-000 000', regex='^\\d{3}\\-\\d{3}\\-\\d{3}$')], verbose_name='Numer telefonu')),
                ('registration_date', models.DateField(default=datetime.date.today, verbose_name='Data utworzenia klienta')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='renter_engine.Address', verbose_name='Adres')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Klient',
                'verbose_name_plural': 'Klienci',
                'ordering': ['-registration_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, unique=True, validators=[django.core.validators.RegexValidator(message='Podana nazwa jest nieprawidłowa. Nazwa może zawierać wyłącznie duże lub małe litery. Ich minimalna ilosć to 3.', regex='^[a-zA-Z]{3,}$')], verbose_name='Nazwa miasta')),
                ('add_date', models.DateField(default=datetime.date.today, verbose_name='Data dodania miasta')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Miasto',
                'verbose_name_plural': 'Miasta',
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='CarRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_geo_lat', models.DecimalField(decimal_places=7, max_digits=10)),
                ('start_geo_lon', models.DecimalField(decimal_places=7, max_digits=10)),
                ('stop_geo_lat', models.DecimalField(decimal_places=7, max_digits=10)),
                ('stop_geo_lon', models.DecimalField(decimal_places=7, max_digits=10)),
                ('start_ts', models.DateTimeField(verbose_name='Moment rozpoczęcia')),
                ('stop_ts', models.DateTimeField(verbose_name='Planowany moment zakończenia')),
                ('true_stop_ts', models.DateTimeField(blank=True, null=True, verbose_name='Moment zakończenia')),
                ('has_paid', models.BooleanField(default=False, verbose_name='Czy wpłynęła opłata')),
                ('payment_timestamp', models.DateTimeField(blank=True, null=True, verbose_name='Moment otrzymania wpłaty')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='renter_engine.Client', verbose_name='Klient')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='renter_engine.Offer', verbose_name='Oferta')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rents', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Wypożyczenie',
                'verbose_name_plural': 'Wypożyczenia',
                'ordering': ['offer', '-has_paid', '-start_ts'],
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addresses', to='renter_engine.City', verbose_name='Miasto'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('city', 'street', 'house_number', 'apartment_number', 'postal_code')},
        ),
    ]