import unittest
from app import create_app

app = create_app()


class TestClass(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_find_distance_1(self):
        # тест на проверку расстояние до "красногорск, посёлок Новый, с3"
        response = self.client.get('/distance/красногорск, посёлок Новый, с3')
        resp_str = response.data.decode('utf-8')
        self.assertIn('5.58', resp_str)

    def test_find_distance_2(self):
        # тест на проверку координат внутри МКАД"
        response = self.client.get('/distance/3-я Фрунзенская улица, 24')
        resp_str = response.data.decode('utf-8')
        self.assertEqual('Точка находится в пределах МКАД', resp_str)

    def test_find_distance_3(self):
        # тест на проверку нераспознанного адреса"
        response = self.client.get('/distance/xxx, xxx')
        resp_str = response.data.decode('utf-8')
        self.assertEqual('Адрес не распознан', resp_str)
        



if __name__ == '__main__':
    unittest.main()