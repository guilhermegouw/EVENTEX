from django.test import TestCase

from subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription.objects.create(
            name="Henrique Bastos",
            cpf="12345678901",
            email="henrique@bastos.net",
            phone="21-99618-6180",
        )
        self.response = self.client.get(f"/inscricao/{self.obj.pk}/")

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "subscriptions/subscription_detail.html")

    def test_context(self):
        subscription = self.response.context["subscription"]
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (
            self.obj.name,
            self.obj.cpf,
            self.obj.email,
            self.obj.phone,
        )
        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get("/inscricao/0/")
        self.assertEqual(404, response.status_code)
