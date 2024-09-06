from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserAuthTests(TestCase):

    def setUp(self):
        # Создаем тестового пользователя для тестирования входа и профиля
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_register_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'newuser@example.com'
        })

        # Вывод ошибок формы, если они есть
        if response.status_code == 200:
            print(response.context['form'].errors)

        self.assertEqual(response.status_code, 302)  # Проверяем, что происходит редирект
        self.assertTrue(User.objects.filter(username='newuser').exists())  # Проверяем, что пользователь был создан

    def test_login_user(self):
        # Тестирование процесса входа пользователя
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password',
        })
        self.assertEqual(response.status_code, 302)  # Проверяем, что происходит редирект
        self.assertTrue(response.wsgi_request.user.is_authenticated)  # Проверяем, что пользователь аутентифицирован

    def test_login_with_wrong_password(self):
        # Тестирование входа с неправильным паролем
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)  # Проверяем, что редиректа не происходит
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # Проверяем, что пользователь не аутентифицирован

    def test_profile_update(self):
        # Логинимся как тестовый пользователь
        self.client.login(username='testuser', password='password')
        # Тестирование обновления профиля пользователя
        response = self.client.post(reverse('profile'), {
            'username': 'testuser',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updateduser@example.com',
        })
        self.assertEqual(response.status_code, 302)  # Проверяем, что происходит редирект
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')  # Проверяем, что данные пользователя обновились
        self.assertEqual(self.user.email, 'updateduser@example.com')  # Проверяем email
