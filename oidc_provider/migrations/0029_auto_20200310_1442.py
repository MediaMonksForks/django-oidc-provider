# Generated by Django 2.0.9 on 2020-03-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0028_jwttoken_jti'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jwttoken',
            options={'verbose_name': 'JWT Token', 'verbose_name_plural': 'JWT Tokens'},
        ),
        migrations.AddField(
            model_name='jwttoken',
            name='id_token_str',
            field=models.TextField(default=None, max_length=65000, verbose_name='ID Token Str'),
            preserve_default=False,
        ),
    ]
