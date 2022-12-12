from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguém em latim',
            data_lancamento = '2003-07-04',
            tipo='F',
            likes=2340,
            dislikes=40,
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifca_campos_serializados(self):
        '''Teste que verifca os campos que estão sendo serializados'''
        data = self.serializer.data

        self.assertSetEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_veritica_conteudo_dos_campos_serializados(self):
        '''Teste que verifica o conteudo dos campos serializados'''
        data = self.serializer.data

        self.assertAlmostEqual(data['titulo'], self.programa.titulo)
        self.assertAlmostEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertAlmostEqual(data['tipo'], self.programa.tipo)
        self.assertAlmostEqual(data['likes'], self.programa.likes)