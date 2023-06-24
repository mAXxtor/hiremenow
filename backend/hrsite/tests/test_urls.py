from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class HrsiteURLTests(TestCase):
    def test_hrsite_namespaces_uses_correct_template(self):
        """Проверка шаблонов для namespaces приложения hrsite."""
        reverse_names_templates = (
            ('hrsite:index', 'hrsite/index.html'),
        )
        for reverse_name, template in reverse_names_templates:
            with self.subTest(reverse_name=reverse_name):
                self.assertTemplateUsed(
                    self.client.get(reverse(reverse_name)), template)

    def test_hrsite_namespaces_matches_correct_urls(self):
        """Проверка namespaces совпадают с hardcod urls приложения hrsite."""
        reverse_names_urls = (
            ('hrsite:index', '/'),
        )
        for reverse_name, url in reverse_names_urls:
            with self.subTest(reverse_name=reverse_name):
                self.assertEqual(reverse(reverse_name), url)

    def test_hrsite_namespaces_exists_at_desired_location(self):
        """Проверка доступности страниц приложения hrsite."""
        reverse_names = (
            ('hrsite:index', None),
        )
        for reverse_name, args in reverse_names:
            with self.subTest(reverse_name=reverse_name):
                self.assertEqual(
                    self.client.get(reverse(
                        reverse_name, args=args)).status_code,
                    HTTPStatus.OK.value)

    def test_404_page_available(self):
        """Проверка доступности страницы 404."""
        self.assertEqual(
            self.client.get('unexisting_page/').status_code,
            HTTPStatus.NOT_FOUND.value)
