import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings, TestCase

from ..models import Area, Company, Internship, InternshipField

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


class InternshipFieldModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.internship_field = InternshipField.objects.create(
            name='Тестовое направление стажировки 1',
            slug='test_internship_field_slug_1',
        )

    def test_internshipfield_model_have_correct_object_names(self):
        """Проверка корректной работы __str__ модели InternshipField."""
        self.assertEqual(str(self.internship_field),
                         self.internship_field.name)

    def test_internshipfield_model_verbose_name(self):
        """
        verbose_name в полях модели InternshipField совпадает с ожидаемым.
        """
        field_verboses = {
            'name': 'Название направления стажировки',
            'slug': 'Slug направления стажировки',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.internship_field._meta.get_field(field).verbose_name,
                    expected_value)

    def test_internshipfield_model_help_text(self):
        """help_text в полях модели InernshipField совпадает с ожидаемым."""
        field_help_texts = {
            'name': 'Введите наименование направления стажировки',
            'slug': 'Введите Slug направления стажировки',
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.internship_field._meta.get_field(field).help_text,
                    expected_value)


class AreaModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.area = Area.objects.create(
            name='Сфера деятельности 1',
            slug='test_area_slug_1',
        )

    def test_area_model_have_correct_object_names(self):
        """Проверка корректной работы __str__ модели Area."""
        self.assertEqual(str(self.area),
                         self.area.name)

    def test_area_model_verbose_name(self):
        """
        verbose_name в полях модели Area совпадает с ожидаемым.
        """
        field_verboses = {
            'name': 'Название сферы деятельности',
            'slug': 'Slug сферы деятельности',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.area._meta.get_field(field).verbose_name,
                    expected_value)

    def test_area_model_help_text(self):
        """help_text в полях модели Area совпадает с ожидаемым."""
        field_help_texts = {
            'name': 'Введите название сферы деятельности',
            'slug': 'Введите Slug сферы деятельности',
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.area._meta.get_field(field).help_text,
                    expected_value)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class CompanyModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.area = Area.objects.create(
            name='Сфера деятельности 1',
            slug='test_area_slug_1',
        )
        test_logo = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00'
            b'\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00'
            b'\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile(
            name='test_logo.gif',
            content=test_logo,
            content_type='image/gif'
        )
        cls.company = Company.objects.create(
            name='Тестовая организация 1',
            name_eng='test_company_1',
            short_description='Тестовое короткое описание организации 1',
            url_site='http://urlsite.test',
            url_vacancies='http://urlvacancies.test',
            url_internships='http://urlinternships.test',
            url_tg_company='http://urltgcompany.test',
            url_tg_vacancies='http://urltgvacancies.test',
            url_tg_internships='http://urltginternships.test',
            logo=uploaded,
            slug='test_company_slug_1',
            size='INDIE',
        )
        cls.company.areas.add(cls.area)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_company_model_have_correct_object_names(self):
        """Проверка корректной работы __str__ модели Company."""
        self.assertEqual(str(self.company),
                         self.company.name)

    def test_company_model_verbose_name(self):
        """
        verbose_name в полях модели Company совпадает с ожидаемым.
        """
        field_verboses = {
            'name': 'Название организации на Русском языке',
            'name_eng': 'Название организации на Английском языке',
            'short_description': 'Короткое описание',
            'url_site': 'Ссылка на корпоративный сайт',
            'url_vacancies': 'Ссылка на вакансии',
            'url_internships': 'Ссылка на стажировки',
            'url_tg_company': 'Ссылка на Telegram организации',
            'url_tg_vacancies': 'Ссылка на Telegram вакансий организации',
            'url_tg_internships':
                'Ссылка на Telegram всех стажировок компании',
            'logo': 'Логотип организации',
            'slug': 'Slug организации',
            'size': 'Размер организации',
            'areas': 'Сфера деятельности организации',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.company._meta.get_field(field).verbose_name,
                    expected_value)

    def test_company_model_help_text(self):
        """help_text в полях модели Company совпадает с ожидаемым."""
        field_help_texts = {
            'name': 'Введите название организации на Русском языке. '
                    'Не более 128 символов',
            'name_eng': 'Введите название организации на Английском языке. '
                        'Не более 128 символов',
            'short_description': 'Введите короткое описание организации. '
                                 'Не более 256 символов',
            'url_site': 'Введите ссылку на корпоративный сайт',
            'url_vacancies': 'Введите ссылку на вакансии',
            'url_internships': 'Введите ссылку на стажировки',
            'url_tg_company': 'Введите ссылку на Telegram организации',
            'url_tg_vacancies':
                'Введите ссылку на Telegram вакансий организации',
            'url_tg_internships':
                'Введите ссылку на Telegram всех стажировок компании',
            'logo': 'Выберите файл для загрузки логотипа организации',
            'slug': 'Введите slug организации',
            'size': 'Выберите размер организации',
            'areas': 'Выберите сферу деятельности организации',
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.company._meta.get_field(field).help_text,
                    expected_value)
