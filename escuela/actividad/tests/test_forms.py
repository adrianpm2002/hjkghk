from django.test import TestCase
from actividad.forms import modificar,registrar
from actividad.models import actividad
from django.contrib.auth.models import User


class TestModificarForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_modificar_form_valid_data(self):
        form_data = {
            'Nombre': 'Actividad Modificada',
            'Autor': self.user,
            'Clasificacion': 'General'
        }
        form = modificar(data=form_data)
        self.assertFalse(form.is_valid())

    def test_modificar_form_empty_name(self):
        form_data = {
            'Nombre': '',
            'Autor': self.user,
            'Clasificacion': 'General'
        }
        form = modificar(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Nombre', form.errors)

    def test_modificar_form_invalid_clasificacion(self):
        form_data = {
            'Nombre': 'Actividad Modificada',
            'Autor': self.user.id,
            'Clasificacion': 'Invalid'
        }
        form = modificar(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Clasificacion', form.errors)


class TestRegistrarForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_registrar_form_valid_data(self):
        form_data = {
            'Nombre': 'Nueva Actividad',
            'Autor': self.user,
            'Clasificacion': 'General',
            'Fecha': '2024-07-02'
        }
        form = registrar(data=form_data)
        self.assertFalse(form.is_valid())

    def test_registrar_form_empty_name(self):
        form_data = {
            'Nombre': '',
            'Autor': self.user,
            'Clasificacion': 'General',
            'Fecha': '2024-07-02'
        }
        form = registrar(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Nombre', form.errors)

    def test_registrar_form_invalid_clasificacion(self):
        form_data = {
            'Nombre': 'Nueva Actividad',
            'Autor': self.user,
            'Clasificacion': 'Invalid',
            'Fecha': '2024-07-02'
        }
        form = registrar(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Clasificacion', form.errors)

    def test_registrar_form_invalid_date(self):
        form_data = {
            'Nombre': 'Nueva Actividad',
            'Autor': self.user,
            'Clasificacion': 'General',
            'Fecha': '2024-13-32'
        }
        form = registrar(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Fecha', form.errors)