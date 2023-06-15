# Generated by Django 4.2 on 2023-06-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': 'Сфера деятельности', 'verbose_name_plural': 'Сферы деятельности'},
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(help_text='Выберите файл для загрузки логотипа организации.', upload_to='company_logo/', verbose_name='Логотип организации'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(help_text='Введите название организации на Русском языке. Не более 128 символов.', max_length=128, verbose_name='Название организации на Русском языке'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name_eng',
            field=models.CharField(help_text='Введите название организации на Английском языке. Не более 128 символов.', max_length=128, verbose_name='Название организации на Английском языке'),
        ),
        migrations.AlterField(
            model_name='company',
            name='short_description',
            field=models.TextField(help_text='Введите короткое описание организации. Не более 256 символов.', max_length=256, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='company',
            name='size',
            field=models.CharField(choices=[('indie', 'Инди-компания'), ('little', 'Маленькая компания'), ('small', 'Небольшая компания'), ('medium', 'Средняя компания'), ('big', 'Крупная компания'), ('giant', 'Крупнейшая компания')], default=None, max_length=10, verbose_name='Размер организации'),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Slug организации'),
        ),
        migrations.AlterField(
            model_name='company',
            name='url_internships',
            field=models.URLField(blank=True, help_text='Введите ссылку на стажировки.', verbose_name='Ссылка на стажировки'),
        ),
        migrations.AlterField(
            model_name='company',
            name='url_site',
            field=models.URLField(help_text='Введите ссылку на корпоративный сайт.', verbose_name='Ссылка на корпоративный сайт'),
        ),
        migrations.AlterField(
            model_name='company',
            name='url_tg_company',
            field=models.URLField(blank=True, help_text='Введите ссылку на Telegram организации.', verbose_name='Ссылка на Telegram организации'),
        ),
        migrations.AlterField(
            model_name='company',
            name='url_tg_internships',
            field=models.URLField(blank=True, help_text='Введите ссылку на Telegram всех стажировок компании.', verbose_name='Ссылка на Telegram всех стажировок компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='url_tg_vacancies',
            field=models.URLField(blank=True, help_text='Введите ссылку на Telegram вакансий организации.', verbose_name='Ссылка на Telegram вакансий организации'),
        ),
        migrations.AlterField(
            model_name='company',
            name='url_vacancies',
            field=models.URLField(blank=True, help_text='Введите ссылку на вакансии.', verbose_name='Ссылка на вакансии'),
        ),
    ]