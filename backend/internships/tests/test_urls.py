from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from ..models import Area, Company, Internship, InternshipField


class InternshipsURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.internship_field = InternshipField.objects.create(
            name='Тестовое направление стажировки 1',
            slug='test_internship_field_slug_1',
        )
        cls.area = Area.objects.create(
            name='Тестовая сфера деятельности 1',
            slug='test_area_slug_1',
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
            slug='test_company_slug_1',
            size='INDIE',
        )
        cls.company.areas.add(cls.area)
        cls.internship = Internship.objects.create(
            name='Тестовая стажировка 1',
            short_description='Тестовое короткое описание стажировки 1',
            start_date='2023-01-01',
            end_date='2023-07-01',
            company=cls.company,
            visibility='True',
        )
        cls.internship.fields.add(cls.internship_field)

    def setUp(self):
        self.reverse_names = (
            ('internships:index', None),
            ('internships:internships_field_list',
             (self.internship_field.slug,)),
        )

    def test_internships_namespaces_uses_correct_template(self):
        """Проверка шаблонов для namespaces приложения internships."""
        reverse_names_templates = (
            ('internships:index', None, 'internships/index.html'),
            ('internships:internships_field_list',
             (self.internship_field.slug,), 'internships/index.html')
        )
        for reverse_name, args, template in reverse_names_templates:
            with self.subTest(reverse_name=reverse_name):
                self.assertTemplateUsed(
                    self.client.get(reverse(reverse_name, args=args)),
                    template)

    def test_internships_namespaces_matches_correct_urls(self):
        """
        Проверка namespaces совпадают с hardcod urls приложения
        internships.
        """
        reverse_names_urls = (
            ('internships:index', None, '/internships/'),
            ('internships:internships_field_list',
             (self.internship_field.slug,),
             f'/internships/{self.internship_field.slug}/',)
        )
        for reverse_name, args, url in reverse_names_urls:
            with self.subTest(reverse_name=reverse_name):
                self.assertEqual(reverse(reverse_name, args=args), url)

    def test_internships_namespaces_exists_at_desired_location(self):
        """Проверка доступности страниц приложения internships."""
        for reverse_name, args in self.reverse_names:
            with self.subTest(reverse_name=reverse_name):
                self.assertEqual(
                    self.client.get(reverse(
                        reverse_name, args=args)).status_code,
                    HTTPStatus.OK.value)

    def test_404_page_available(self):
        """Проверка доступности страницы 404."""
        self.assertEqual(
            self.client.get('/internships/unexisting_page/').status_code,
            HTTPStatus.NOT_FOUND.value)
