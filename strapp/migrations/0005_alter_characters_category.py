# Generated by Django 4.0 on 2023-11-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strapp', '0004_alter_characters_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='category',
            field=models.CharField(choices=[('millennium', 'ミレニアム'), ('trinity', 'トリニティ'), ('gehenna', 'ゲヘナ'), ('abydos', 'アビドス'), ('hyakki', '百鬼夜行'), ('redwinter', 'レッドウィンター'), ('valkyrie', 'ヴァルキューレ'), ('srt', 'SRT'), ('sengaikyo', '山海経'), ('arius', 'アリウス')], max_length=50, verbose_name='学園'),
        ),
    ]
