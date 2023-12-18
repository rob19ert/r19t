import unittest
from main import Detail, Supplier, SupplierDetailLink, merge_one_to_many, query_2_results, query_3_results

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        self.details = [
            Detail(1, "Гвоздь", 1),
            Detail(2, "Пробка", 2),
            Detail(3, "Шуруп", 2),
            Detail(4, "Замок", 3),
            Detail(5, "Призма", 1)
        ]

        self.suppliers = [
            Supplier(1, "Иванов", "ПИЛАтос"),
            Supplier(2, "Петров", "Замок или замок?"),
            Supplier(3, "Сидоренко", "ГВОЗДИка"),
            Supplier(4, "Смирный", "ГВОЗДИка"),
            Supplier(5, "Козуб", "ПИЛАтос"),
        ]

        self.supplier_detail_links = [
            SupplierDetailLink(1, 1),
            SupplierDetailLink(2, 2),
            SupplierDetailLink(2, 3),
            SupplierDetailLink(4, 2),
            SupplierDetailLink(5, 1)
        ]

    def test_merge_one_to_many(self):
        result = merge_one_to_many(self.details, self.suppliers)
        expected_result = [
            ('Иванов', 'Гвоздь', 'ПИЛАтос'),
            ('Петров', 'Пробка', 'Замок или замок?'),
            ('Петров', 'Шуруп', 'Замок или замок?'),
            ('Смирный', 'Пробка', 'ГВОЗДИка'),
            ('Козуб', 'Гвоздь', 'ПИЛАтос')
        ]
        self.assertEqual(result, expected_result)

    def test_query_2_results(self):
        result = query_2_results(self.suppliers)
        expected_result = [('ГВОЗДИка', 2), ('Замок или замок?', 2), ('ПИЛАтос', 2)]
        self.assertEqual(result, expected_result)

    def test_query_3_results(self):
        result = query_3_results(self.suppliers)
        expected_result = [('Иванов', 'ПИЛАтос'), ('Смирный', 'ГВОЗДИка'), ('Козуб', 'ПИЛАтос')]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
