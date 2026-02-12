import pytest
import csv
import os
import tempfile


@pytest.fixture
def sample_csv_data():
    """Фикстура с примерами данных для тестов"""
    return [
        ['country', 'gdp'],
        ['United States', '25462'],
        ['China', '17963'],
        ['Germany', '4086'],
        ['United States', '23315'],
        ['China', '17734'],
        ['Germany', '4072']
    ]


@pytest.fixture
def extra_sample_csv_data():
    """Фикстура с примерами дополнительных данных для тестов"""
    return [
        ['country', 'gdp'],
        ['United States', '22994'],
        ['China', '17734'],
        ['Germany', '4257']
    ]


@pytest.fixture
def sample_wrong_csv_data():
    """Фикстура с примерами косячных данных для тестов"""
    return [
        ['country', 'gdp'],
        ['United States', '25462'],
        ['China', 'abc'],
        ['Germany', '4086'],
        ['United States', '23315'],
        ['China', '17734'],
        ['Germany', '4072']
    ]


@pytest.fixture
def temp_csv_file():
    """Создает временный CSV файл и удаляет его после теста"""
    temp_files = []

    def _create_temp_csv(data, filename="test.csv"):
        temp_dir = tempfile.mkdtemp()
        filepath = os.path.join(temp_dir, filename)

        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)

        temp_files.append(filepath)
        return filepath

    yield _create_temp_csv

    for filepath in temp_files:
        try:
            os.remove(filepath)
            os.rmdir(os.path.dirname(filepath))
        except OSError:
            pass
