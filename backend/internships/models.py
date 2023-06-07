from django.conf import settings
from django.db import models


class InternshipField(models.Model):
    name = models.CharField(
        'Направление стажировки',
        max_length=128,
        blank=False,
        help_text='Введите наименование стажировки',
        db_index=True,
    )
    slug = models.SlugField(
        'Slug направления стажировки',
        max_length=settings.MAX_LEN_MODEL_FIELD,
        db_index=True,
        unique=True,
    )

    class Meta:
        verbose_name = 'Направление стажировки'
        verbose_name_plural = 'Направления стажировки'

    def __str__(self):
        return self.name


class Internship(models.Model):
    """
    Стажировка.
    Attributes:
        name(str):
            Название.
        short_description(str):
            Короткое описание программ стажировок (до 256 символов).
        start_date(date):
            Дата начала подачи заявки на стажировку.
        end_date(date):
            Дата окончания подачи заявки на стажировку.
        is_permanent(bool):
            Чекбокс “постоянный набор”.
        direction(multiple_choice):
            Направление стажировки.
        pub_date(date):
            Дата публикации.
Дописать всю хуйню

    """
    name = models.CharField(
        'Название стажировки',
        max_length=128,
        help_text='Введите наименование стажировки. Не более 128 символов.',
        db_index=True,
    )
    short_description = models.TextField(
        'Короткое описание',
        help_text='Введите короткое описание стажировки. '
                  'Не более 256 символов.',
        max_length=256,
    )
    start_date = models.DateField(
        'Старт подачи заявок',
    )
    end_date = models.DateField(
        'Окончание приёма',
    )
    is_permanent = models.BooleanField(
        'Набор на стажировку ведётся постоянно',
    )
    fields = models.ManyToManyField(
        verbose_name='Направление стажировки',
        related_name='internships',
        to=InternshipField,
        # through='InternshipsFields',
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
    visibility = models.BooleanField('Стажировка опубликована')

    class Meta:
        ordering = ('-updated_at',)
        verbose_name = 'Стажировка'
        verbose_name_plural = 'Стажировки'

    def __str__(self):
        return self.name[:15]


# правильный термин - Internship Fields вместо DirectionOfInternship

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
