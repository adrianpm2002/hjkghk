from django.test import TestCase,Client
from actividad.models import actividad
#from user.models import User
from django.contrib.auth.models import User
from datetime import date


class actModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        #Configurar objetos no modificados utilizados por todos los métodos de prueba
        actividad.objects.create(Nombre="Miguel", Autor=cls.user, Clasificacion="General", Fecha = "2024-07-02")

    def test_first_name_label(self):
        act=actividad.objects.get(id=1)
        field_label = act._meta.get_field('Nombre').verbose_name
        self.assertEqual(field_label,'Nombre')


    def test_nombre_max_length(self):
        act=actividad.objects.get(id=1)
        max_length = act._meta.get_field('Nombre').max_length
        self.assertEqual(max_length, 10)

    def test_clasificacion_choices(self):
        act=actividad.objects.get(id=1)
        choices = act._meta.get_field('Clasificacion').choices
        self.assertEqual(choices, [('General', 'General'), ('Principal', 'Principal')])

    def test_fecha_default(self):
        act=actividad.objects.get(id=1)
        self.assertEqual(act.Fecha, date(2024, 7, 2))

    def test_str_method(self):
        act=actividad.objects.get(id=1)
        self.assertEqual(str(act), "Miguel")

    def test_autor_relationship(self):
        act=actividad.objects.get(id=1)
        self.assertEqual(act.Autor, self.user)

    def test_nombre_field(self):
        # Verificar que el campo Nombre es requerido
        with self.assertRaises(ValueError):
            actividad.objects.create(Nombre='', Autor=self.user, Clasificacion="General", Fecha="2024-07-02")

        # Verificar que el campo Nombre tiene una longitud máxima de 10 caracteres
        with self.assertRaises(ValueError):
            actividad.objects.create(Nombre="Esta actividad tiene más de 10 caracteres", Autor=self.user, Clasificacion="General", Fecha="2024-07-02")

    def test_clasificacion_field(self):
        # Verificar que el campo Clasificacion solo acepta valores válidos
        with self.assertRaises(ValueError):
            actividad.objects.create(Nombre="Actividad", Autor=self.user, Clasificacion="Invalido", Fecha="2024-07-02")

    def test_fecha_field(self):
        # Verificar que el campo Fecha acepta solo fechas válidas
        with self.assertRaises(ValueError):
            actividad.objects.create(Nombre="Actividad", Autor=self.user, Clasificacion="General", Fecha="2024-03-29")