from collections import defaultdict
from basic import try_convert_to_number


reports = ('average-gdp', 'another')

def average_gdp(data):
    """Возвращает средний ВВП в каждой стране за все года
    Args:
        data: предобработанные данные
    Returns:
        list с заголовками результатов и list с данными результатов отдельно"""
    headers = data[0]
    grouped_data = defaultdict(list)

    if 'country' not in headers:
        raise ValueError("Колонка 'country' не найдена в данных")
    if 'gdp' not in headers:
        raise ValueError("Колонка 'gdp' не найдена в данных")

    group_by_idx = headers.index('country')
    numeric_idx = headers.index('gdp')

    for row in data[1:]:  # Пропускаем заголовки
        if len(row) > max(group_by_idx, numeric_idx):
            group_key = row[group_by_idx]
            numeric_value = try_convert_to_number(row[numeric_idx])

            if isinstance(numeric_value, (int, float)):
                grouped_data[group_key].append(numeric_value)

    result = []
    result_headers = ['country', 'avg_gdp']

    for group_key, values in sorted(grouped_data.items()):
        if values:
            average = sum(values) / len(values)
            if isinstance(average, float):
                average = round(average, 2)
            result.append([group_key, average])

    result.sort(key=lambda x: x[1], reverse=True)

    return result_headers, result
