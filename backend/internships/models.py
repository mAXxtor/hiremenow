from django.conf import settings
from django.db import models


class InternshipField(models.Model):
    """
    Направление стажировки.
    Attributes:
        name(str):
            Название направления стажировки. До 128 символов.
        slug(str):
            Slug направления стажировки. До 200 символов.
    """
    name = models.CharField(
        'Название направления стажировки',
        max_length=128,
        blank=False,
        db_index=True,
        help_text='Введите наименование направления стажировки',
    )
    slug = models.SlugField(
        'Slug направления стажировки',
        max_length=settings.MAX_LEN_MODEL_FIELD,
        unique=True,
        db_index=True,
        help_text='Введите Slug направления стажировки',
    )

    class Meta:
        verbose_name = 'Направление стажировки'
        verbose_name_plural = 'Направления стажировки'

    def __str__(self):
        return self.name


class Area(models.Model):
    """
    Сфера деятельности организации.
    Attributes:
        name(str):
            Название сферы деятельности организации. До 128 символов.
        slug(str):
            Slug сферы деятельности организации. До 200 символов.
    """
    name = models.CharField(
        'Название сферы деятельности',
        max_length=128,
        blank=False,
        db_index=True,
        help_text='Введите название сферы деятельности',
    )
    slug = models.SlugField(
        'Slug сферы деятельности',
        max_length=settings.MAX_LEN_MODEL_FIELD,
        unique=True,
        db_index=True,
        help_text='Введите Slug сферы деятельности',
    )

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'

    def __str__(self):
        return self.name


class Company(models.Model):
    """
    Организация.
    Attributes:
        name(str):
            Название организации на Русском языке.
        name_eng(str):
            Название организации на Английском языке.
        short_description(str):
            Короткое описание организации. До 256 символов.
        url_site(url):
            Ссылка на корпоративный сайт. До 200 символов (по умолчанию).
        url_vacancies(url):
            Ссылка на вакансии. До 200 символов (по умолчанию).
        url_internships(url):
            Ссылка на стажировки. До 200 символов (по умолчанию).
        url_tg_company(url):
            Ссылка на Telegram организации. До 200 символов (по умолчанию).
        url_tg_vacancies(url):
            Ссылка на Telegram вакансий организации.
            До 200 символов (по умолчанию).
        url_tg_internships(url):
            Ссылка на Telegram всех стажировок компании.
            До 200 символов (по умолчанию).
        logo(img):
            Логотип организации.
        slug(str):
            Slug организации. До 200 символов.
        size(str):
            Размер организации.
            Поле выбора из списка размеров организации SIZES:
                - инди-компания (до 10 человек в штате) `indie`
                - маленькие компании (от 10 до 99 человек в штате ) `little`
                - небольшие компании (от 100 до 250 человек в штате) `small`
                - средние компании (от 251 до 1000 человек в штате) `medium`
                - крупные компании (от 1000 до 5000 человек в штате) `big`
                - крупнейшие компании (от 5001 человек в штате) `giant`
        areas(int):
            Сфера деятельности организации.
            Связь ManyToMany с моделью Area.
        #TODO Это точно относится к компании? Стоит сделать отдельную модель?
        open_graph(int):
            og:title `og_title` (необязательное)
            og:description `og_description` (необязательное)
            og:image `og_image` (необязательное)
    """

    INDIE = 'indie'
    LITTLE = 'little'
    SMALL = 'small'
    MEDIUM = 'medium'
    BIG = 'big'
    GIANT = 'giant'
    SIZES = [
        (INDIE, 'Инди-компания'),
        (LITTLE, 'Маленькая компания'),
        (SMALL, 'Небольшая компания'),
        (MEDIUM, 'Средняя компания'),
        (BIG, 'Крупная компания'),
        (GIANT, 'Крупнейшая компания'),
    ]

    name = models.CharField(
        'Название организации на Русском языке',
        max_length=128,
        help_text='Введите название организации на Русском языке. '
                  'Не более 128 символов',
    )
    name_eng = models.CharField(
        'Название организации на Английском языке',
        max_length=128,
        help_text='Введите название организации на Английском языке. '
                  'Не более 128 символов',
    )
    short_description = models.TextField(
        'Короткое описание',
        max_length=256,
        help_text='Введите короткое описание организации. '
                  'Не более 256 символов',
    )
    url_site = models.URLField(
        'Ссылка на корпоративный сайт',
        help_text='Введите ссылку на корпоративный сайт'
    )
    url_vacancies = models.URLField(
        'Ссылка на вакансии',
        blank=True,
        help_text='Введите ссылку на вакансии'
    )
    url_internships = models.URLField(
        'Ссылка на стажировки',
        blank=True,
        help_text='Введите ссылку на стажировки'
    )
    url_tg_company = models.URLField(
        'Ссылка на Telegram организации',
        blank=True,
        help_text='Введите ссылку на Telegram организации'
    )
    url_tg_vacancies = models.URLField(
        'Ссылка на Telegram вакансий организации',
        blank=True,
        help_text='Введите ссылку на Telegram вакансий организации'
    )
    url_tg_internships = models.URLField(
        'Ссылка на Telegram всех стажировок компании',
        blank=True,
        help_text='Введите ссылку на Telegram всех стажировок компании'
    )
    logo = models.FileField(
        'Логотип организации',
        upload_to='company_logo/',
        blank=True,
        help_text='Выберите файл для загрузки логотипа организации',
    )
    slug = models.SlugField(
        'Slug организации',
        max_length=settings.MAX_LEN_MODEL_FIELD,
        db_index=True,
        unique=True,
        help_text='Введите slug организации',
    )
    size = models.CharField(
        'Размер организации',
        max_length=10,
        # TODO Разобраться как можно None
        blank=True,
        choices=SIZES,
        help_text='Выберите размер организации',
    )
    areas = models.ManyToManyField(
        to=Area,
        related_name='companies',
        verbose_name='Сфера деятельности организации',
        help_text='Выберите сферу деятельности организации',
    )

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name


class Internship(models.Model):
    """
    Стажировка.
    Attributes:
        name(str):
            Название стажировки.
        short_description(str):
            Короткое описание программ стажировок. До 256 символов.
        start_date(date):
            Дата начала подачи заявки на стажировку.
        end_date(date):
            Дата окончания подачи заявки на стажировку.
        is_permanent(bool):
            Открыт постоянный набор на стажировку.
        fields(int):
            Направление стажировки.
            Связь ManyToMany с моделью InternshipField.
        company(int):
            Организация, проводящая стажировку.
            Связь ManyToOne с моделью Company через ForeignKey.
        created_at(date):
            Дата создания стажировки.
        updated_at(date):
            Дата обновления стажировки.
        published_at(date):
            Дата публикации стажировки.
        visibility(bool):
            Публикация стажировки.
    """
    name = models.CharField(
        'Название стажировки',
        max_length=128,
        db_index=True,
        help_text='Введите наименование стажировки. Не более 128 символов',
    )
    short_description = models.TextField(
        'Короткое описание',
        max_length=256,
        help_text='Введите короткое описание стажировки. '
                  'Не более 256 символов',
    )
    start_date = models.DateField(
        'Начало подачи заявок',
        help_text='Введите дату начала подачи заявок',
    )
    end_date = models.DateField(
        'Окончание приёма заявок',
        help_text='Введите дату окончания подачи заявок',
    )
    is_permanent = models.BooleanField(
        'Набор на стажировку ведётся постоянно',
        default=False,
        help_text='Выберите для постоянного набора на стажировку',
    )
    fields = models.ManyToManyField(
        to=InternshipField,
        related_name='internships',
        verbose_name='Направление стажировки',
        help_text='Выберите направление стажировки'
    )
    company = models.ForeignKey(
        to=Company,
        on_delete=models.CASCADE,
        related_name='internships',
        verbose_name='Организация',
        help_text='Выберите организацию',
    )
    created_at = models.DateTimeField(
        'Дата создания стажировки',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'Дата обновления стажировки',
        auto_now=True,
    )
    published_at = models.DateTimeField(
        'Дата публикации стажировки',
        auto_now=True,
    )
    visibility = models.BooleanField(
        'Стажировка опубликована',
        default=False,
        help_text='Выберите для публикации стажировки',
    )

    class Meta:
        ordering = ('-updated_at',)
        verbose_name = 'Стажировка'
        verbose_name_plural = 'Стажировки'
        constraints = [models.UniqueConstraint(fields=[
            'name', 'company'], name='unique_internship_for_company')
        ]

    def __str__(self):
        return self.name[:15]


# TODO Убрать если оставим без связующей модели
# class InternshipsFields(models.Model):
#     """ Связующая модель Direction и Internship.

#     Attributes:
#         directions(int):
#             Направление стажировки.
#             Связь ForeignKey с моделью Internship.
#         internships(int):
#             Стажировки.
#             Связь ForeignKey с моделью Direction.
#     """
#     field = models.ForeignKey(
#         verbose_name='Направления стажировки',
#         related_name='internship',
#         to=InternshipField,
#         on_delete=models.CASCADE,
#     )
#     internship = models.ForeignKey(
#         verbose_name='Стажировки направления',
#         related_name='field',
#         to=Internship,
#         on_delete=models.CASCADE,
#     )

#     class Meta:
#         verbose_name = 'Направление стажировок'
#         verbose_name_plural = 'Направления стажировок'
#         ordering = ('-id', )
#         constraints = [models.UniqueConstraint(fields=[
#             'field', 'internship'],
#             name='unique_field_of_internship')
#         ]

#     def __str__(self):
#         return f'{self.internship} относится к {self.field}'
