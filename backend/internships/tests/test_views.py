import shutil
import tempfile
from http import HTTPStatus

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings, TestCase
from django.urls import reverse

from ..models import Area, Company, Internship, InternshipField

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class InternshipsViewTests(TestCase):
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
        cls.internship_field = InternshipField.objects.create(
            name='Тестовое направление стажировки 1',
            slug='test_internship_field_slug_1',
        )
        cls.internship = Internship.objects.create(
            name='Тестовая стажировка 1',
            short_description='Тестовое короткое описание стажировки 1',
            start_date='2023-01-01',
            end_date='2023-07-01',
            is_permanent='False',
            company=cls.company,
            visibility='True',
        )
        cls.internship.fields.add(cls.internship_field)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def internship_view_test(self, request):
        """Проверка контекста шаблона."""
        context = request.context['internships'][0]
        context_fields = {
            context.name: self.internship.name,
            context.short_description: self.internship.short_description,
            str(context.start_date): self.internship.start_date,
            str(context.end_date): self.internship.end_date,
            str(context.is_permanent): self.internship.is_permanent,
            context.company: self.internship.company,
            str(context.visibility): self.internship.visibility,
        }
        for value, expected in context_fields.items():
            with self.subTest(value=value):
                self.assertEqual(value, expected)

    def test_index_page_show_correct_context(self):
        """Шаблон index сформирован с правильным контекстом."""
        # Проверка количества стажировок в базе
        self.assertEqual(Internship.objects.count(), 1)
        response = self.client.get(reverse('internships:index'))
        # Проверка вывода стажировок на страницу index
        self.assertEqual(len(response.context['internships']), 1)
        # Проверка контекста шаблона
        self.internship_view_test(response)

    def test_internships_field_list_page_show_correct_context(self):
        """
        Шаблон internships_field_list сформирован с правильным контекстом.
        """
        # Проверка количества постов в базе
        self.assertEqual(Internship.objects.count(), 1)
        response = self.client.get(
            reverse('internships:internships_field_list',
                    args=(self.internship_field.slug,))
        )
        # Проверка контекста шаблона internships_field_list
        self.internship_view_test(response)
        # Проверка вывода необходимого направления стажировки
        self.assertEqual(response.context['field'], self.internship_field.slug)
        # Проверка вывода стажировок на страницу internships_field_list
        self.assertEqual(len(response.context['internships']), 1)
        # Проверка на получение страницы 404 при переходе на несуществующее направление стажировки # noqa E501
        response_test_slug = self.client.get(
            reverse('internships:internships_field_list',
                    args=('nonexistent_slug',))
        )
        self.assertEqual(response_test_slug.status_code,
                         HTTPStatus.NOT_FOUND.value)
        # Стажировка не выводится на страницу с другим направлением
        internship_field_2 = InternshipField.objects.create(
            name='Тестовое направление стажировки 2',
            slug='test_internship_field_slug_2',
        )
        response_test_field = self.client.get(
            reverse('internships:internships_field_list',
                    args=(internship_field_2.slug,))
        )
        self.assertEqual(response_test_field.status_code,
                         HTTPStatus.NOT_FOUND.value)
