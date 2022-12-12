from django.test import TestCase

from aluraflix.models import Programa


class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguém em latim',
            data_lancamento = '2003-07-04',
        )

    def test_verifica_atributos_do_programa(self):
        '''Test que verifica os atributos de um programa com valores default'''
        self.assertAlmostEqual(self.programa.titulo, 'Procurando ninguém em latim')
        self.assertAlmostEqual(self.programa.tipo, 'F')
        self.assertAlmostEqual(self.programa.data_lancamento, '2003-07-04')
        self.assertAlmostEqual(self.programa.likes, 0)
        self.assertAlmostEqual(self.programa.dislikes, 0)
