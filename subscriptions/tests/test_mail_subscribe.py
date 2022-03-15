from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        self.data = dict(
            name="Henrique Bastos",
            cpf="12345678901",
            email="henrique@bastos.net",
            phone="21-99618-6180",
        )
        self.client.post("/inscricao/", self.data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect_subject = "Confirmação de inscrição"

        self.assertEqual(expect_subject, self.email.subject)

    def test_subscription_email_from(self):
        expect_from = "guilherme.gouw@gmail.com"

        self.assertEqual(expect_from, self.email.from_email)

    def test_subscription_email_to(self):
        expect_to = ["guilherme.gouw@gmail.com", "henrique@bastos.net"]

        self.assertEqual(expect_to, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            "Henrique Bastos",
            "12345678901",
            "henrique@bastos.net",
            "21-99618-6180",
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
