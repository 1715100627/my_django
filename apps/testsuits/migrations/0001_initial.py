# Generated by Django 3.1.2 on 2020-11-05 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0002_auto_20201105_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testsuits',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('id', models.AutoField(help_text='ID主键', primary_key=True, serialize=False, verbose_name='ID主键')),
                ('name', models.CharField(help_text='套件名称', max_length=200, unique=True, verbose_name='套件名称')),
                ('include', models.TextField(help_text='包含接口', null=True, verbose_name='包含接口')),
                ('project', models.ForeignKey(help_text='所属项目 ', on_delete=django.db.models.deletion.CASCADE, related_name='testsuits', to='projects.projects')),
            ],
            options={
                'verbose_name': '套件集',
                'verbose_name_plural': '套件集',
                'db_table': 'db_testsuits',
            },
        ),
    ]
