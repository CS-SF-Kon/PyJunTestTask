import argparse
import sys
from basic import data_combine,read_csv_file,validate_file_structure,to_tabulate
from reports import reports, average_gdp


def main():
    parser = argparse.ArgumentParser(
        description='Объединение CSV файлов с одинаковой структурой',
        epilog="""Примеры использования:
        python script.py --files data1.csv data2.csv --report average-gdp
        python script.py --files *.csv --report average-gdp
                
        Доступные отчеты:
            average-gdp  - средний ВВП по странам"""
    )

    parser.add_argument(
        '--files',
        nargs='+',  # Один или несколько аргументов
        required=True,
        help='Список CSV файлов для объединения (через пробел)'
    )

    parser.add_argument(
        '--report',
        required=True,
        help='Название требуемого отчёта'
    )

    args = parser.parse_args()

    all_data = []
    for filepath in args.files:
        data = read_csv_file(filepath)
        if data is None:
            sys.exit(1)
        all_data.append(data)

    if not validate_file_structure(all_data):
        sys.exit(1)

    if not all_data:
        print("Нет данных для отображения.", file=sys.stderr)
        sys.exit(1)

    headers, combined_rows = data_combine(all_data)
    total_data = headers
    total_data.extend(combined_rows)

    if args.report not in reports:
        print(f"Ошибка: Вид отчёта не распознан '{args.report}'", file=sys.stderr)
        print("Пример: --report 'average-gdp'", file=sys.stderr)
        sys.exit(1)

    match args.report:
        case 'average-gdp':
            report_headers, report_data = average_gdp(total_data)
            to_tabulate(report_data, report_headers)
        case 'another':
            print('Отчёт another не реализован')
        case _:
            print("Ошибка: Вид отчёта всё равно не распознан", file=sys.stderr)
            parser.print_help()
            sys.exit(1)


if __name__ == '__main__':
    main()
