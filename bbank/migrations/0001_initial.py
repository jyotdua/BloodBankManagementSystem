# Generated by Django 2.2.2 on 2019-11-13 19:15

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(default='country', max_length=2)),
                ('h_doc', models.CharField(max_length=200)),
                ('contact_no', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('type_req', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=200)),
                ('age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200)),
                ('LastDonated', models.DateTimeField(default=None)),
                ('Email', models.EmailField(max_length=254)),
                ('City', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(default='country', max_length=2)),
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('contact_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('date', models.DateTimeField()),
                ('bloodbank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='bbank.Blood_Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Bloodtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.FloatField()),
                ('A_mi', models.FloatField()),
                ('B', models.FloatField()),
                ('B_mi', models.FloatField()),
                ('O', models.FloatField()),
                ('O_mi', models.FloatField()),
                ('AB', models.FloatField()),
                ('AB_mi', models.FloatField()),
                ('bloodbank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank.Blood_Bank')),
            ],
        ),
    ]