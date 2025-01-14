
from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):

    def test_create_user_with_email(self):
        # test creating a normal user
        email="test@test.com"
        password="asdasd123123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalize(self):
        # test new user has email normalized

        sample_emails = [
            ["test1@TEST.com", "test1@test.com"],
            ["I_EAT_peOple@test.COM", "I_EAT_peOple@test.com"]
        ]

        for email , expected  in sample_emails:
            user = get_user_model().objects.create_user(email, "samplePassword1231231")
            self.assertEqual(user.email, expected)


