from django.test import TestCase, Client
from django.urls import reverse
from actividad.models import actividad
from user.models import User,defaultUser
from actividad.forms import modificar,registrar

class TestUpdateActividad(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.actividad = actividad.objects.create(
            Nombre='Actividad de prueba',
            Autor=self.user,
            Clasificacion='General',
            Fecha='2024-07-02'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

    def test_update_actividad_get(self):
        response = self.client.get(reverse('update_actividad', args=[self.actividad.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_actividad.html')
        self.assertIsInstance(response.context['form'], modificar)

    def test_update_actividad_post(self):
        data = {
            'Nombre': 'Actividad Modificada',
            'Autor': self.user,
            'Clasificacion': 'Principal',
            'Fecha': '2024-07-02'
        }
        response = self.client.post(reverse('update_actividad', args=[self.actividad.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list_actividad'))
        self.actividad.refresh_from_db()
        self.assertEqual(self.actividad.Nombre, 'Actividad Modificada')
        self.assertEqual(self.actividad.Clasificacion, 'Principal')



class TestCreateActividad(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

    def test_create_actividad_get(self):
        response = self.client.get(reverse('create_actividad'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrar_actividad.html')
        self.assertIsInstance(response.context['form'], registrar)

    def test_create_actividad_post(self):
        data = {
            'Nombre': 'Nueva Actividad',
            'Autor': self.user.pk,
            'Clasificacion': 'General',
            'Fecha': '2024-07-02'
        }
        response = self.client.post(reverse('create_actividad'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list_actividad'))
        self.assertEqual(actividad.objects.count(), 1)
        self.assertTrue(actividad.objects.filter(Nombre='Nueva Actividad').exists())

class TestListActividad(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        self.actividad1 = actividad.objects.create(
            Nombre='Actividad 1',
            Autor=self.user,
            Clasificacion='General',
            Fecha='2024-07-02'
        )
        self.actividad2 = actividad.objects.create(
            Nombre='Actividad 2',
            Autor=self.user,
            Clasificacion='Principal',
            Fecha='2024-07-02'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

    def test_list_actividad(self):
        response = self.client.get(reverse('list_actividad'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Actividades.html')
        self.assertIn('act', response.context)
        self.assertEqual(len(response.context['act']), 2)
        self.assertIn(self.actividad1, response.context['act'])
        self.assertIn(self.actividad2, response.context['act'])
        