import csv
from tabulate import tabulate
import sys


def read_csv_file(filepath):
    """Читает csv-файл по указанному адресу
    Args:
        filepath: адрес файла"""
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла '{filepath}': {e}", file=sys.stderr)
        return None


def validate_file_structure(files_data):
    """Проверяет, что все файлы имеют одинаковые заголовки, если было считано несколько файлов
    Args:
        files_data: сырые, но объединённые данные"""
    if not files_data:
        return False

    first_headers = files_data[0][0] if files_data[0] else []

    for i, data in enumerate(files_data[1:], start=2):
        if not data:
            print(f"Ошибка: Файл {i} пустой или не удалось прочитать.", file=sys.stderr)
            return False
        if data[0] != first_headers:
            print(f"Ошибка: Заголовки файла {i} не совпадают с первым файлом.", file=sys.stderr)
            print(f"Ожидалось: {first_headers}", file=sys.stderr)
            print(f"Получено: {data[0]}", file=sys.stderr)
            return False

    return True


def try_convert_to_number(value):
    """Пытается преобразовать значение в число (int или float)
    Args:
        value: значение
    Returns:
        int, float или как есть, если не получилось конвертировать в число"""
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def data_combine(all_data):
    """Получает сырые данные, убирает в них заголовки
    Args:
        all_data: сырые данные
    Returns:
        list с извлечёнными заголовками и list с извлечёнными данными отдельно"""
    headers = [all_data[0][0]]

    combined_rows = []
    for data in all_data:
        rows_to_add = data[1:] if data else []
        combined_rows.extend(rows_to_add)
    return headers, combined_rows


def to_tabulate(data, headers):
    """Выводит в консоль в красивом формате данные
    Важно - заголовки и данные отдельными аргументами
    Args:
        data: list данных
        headers: list заголовков"""
    print(tabulate(data, headers=headers, tablefmt='grid'))
