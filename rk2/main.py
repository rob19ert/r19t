from collections import Counter

class Detail:
    def __init__(self, id, name, supplier_id):
        self.id = id
        self.name = name
        self.supplier_id = supplier_id

class Supplier:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department

class SupplierDetailLink:
    def __init__(self, supplier_id, detail_id):
        self.supplier_id = supplier_id
        self.detail_id = detail_id

def merge_one_to_many(details, suppliers):
    return [(supplier.name, detail.name, supplier.department)
            for detail in details
            for supplier in suppliers
            if detail.supplier_id == supplier.id]

def merge_many_to_many(suppliers, supplier_detail_links, details):
    many_to_many_temp = [(supplier.name, sdl.supplier_id, sdl.detail_id)
                         for supplier in suppliers
                         for sdl in supplier_detail_links
                         if supplier.id == sdl.supplier_id]

    many_to_many = [(supplier.id, detail.name)
                    for supplier in suppliers
                    for detail in details
                    if detail.supplier_id == supplier.id]

    return many_to_many_temp, many_to_many

def query_1_results(data):
    return sorted(data, key=lambda x: x[0])

def query_2_results(suppliers):
    department_counts = Counter(supplier.department for supplier in suppliers)
    return sorted(department_counts.items(), key=lambda x: x[1], reverse=True)

def query_3_results(suppliers):
    return [(supplier.name, supplier.department) for supplier in suppliers if supplier.name.endswith("ов")]

def main():
    """Main function"""

    details = [
        Detail(1, "Гвоздь", 1),
        Detail(2, "Пробка", 2),
        Detail(3, "Шуруп", 2),
        Detail(4, "Замок", 3),
        Detail(5, "Призма", 1)
    ]

    suppliers = [
        Supplier(1, "Иванов", "ПИЛАтос"),
        Supplier(2, "Петров", "Замок или замок?"),
        Supplier(3, "Сидоренко", "ГВОЗДИка"),
        Supplier(4, "Смирный", "ГВОЗДИка"),
        Supplier(5, "Козуб", "ПИЛАтос"),
    ]

    supplier_detail_links = [
        SupplierDetailLink(1, 1),
        SupplierDetailLink(2, 2),
        SupplierDetailLink(2, 3),
        SupplierDetailLink(4, 2),
        SupplierDetailLink(5, 1)
    ]

    # Query 1
    result_query_1 = query_1_results(merge_one_to_many(details, suppliers))
    print_query_results("Задание №1", result_query_1, "Поставщик: {item[0]}, Деталь: {item[1]}, Отдел: {item[2]}")

    # Query 2
    result_query_2 = query_2_results(suppliers)
    print_query_results("Задание №2", result_query_2, "Отдел: {item[0]}, Количество поставщиков: {item[1]}")

    # Query 3
    result_query_3 = query_3_results(suppliers)
    print_query_results("Задание №3", result_query_3, "Поставщик: {item[0]}, Отдел: {item[1]}")

def print_query_results(title, result, format_string):
    print(f"\n{title}:")
    for item in result:
        print(format_string.format(item=item))

if __name__ == "__main__":
    main()
