import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src')) # вот тут вообще не понял, зачем почему
from basic import try_convert_to_number, read_csv_file, data_combine # хоть и тестики работают


class TestTryConvertToNumber:
    """Тест для функции try_convert_to_number"""

    @pytest.mark.parametrize("input_value,expected", [
        ("123", 123),
        ("-456", -456),
        ("0", 0),
        ("123.456", 123.456),
        ("-78.90", -78.90),
        (".5", 0.5),
        ("Abc", "Abc"),
        ("Abc123", "Abc123"),
        ("123Abc", "123Abc")
    ])
    def test_mixed_types(self, input_value, expected):
        assert try_convert_to_number(input_value) == expected


class TestReadCSVFile:
    """Тесты для функции read_csv_file"""

    def test_read_valid_csv(self, temp_csv_file, sample_csv_data):
        filepath = temp_csv_file(sample_csv_data)
        result = read_csv_file(filepath)

        assert result == sample_csv_data
        assert len(result) == 7
        assert result[0] == ['country', 'gdp']

    def test_empty_csv(self, temp_csv_file):
        filepath = temp_csv_file([])
        result = read_csv_file(filepath)
        assert result == []


class TestDataCombine:
    """Тесты для функции data_combine"""

    def test_combine_single_file(self, sample_csv_data):
        headers, data = data_combine([sample_csv_data])
        assert headers[0] == ['country', 'gdp']
        assert len(data) == 6

    def test_combine_multiple_files(self, sample_csv_data, extra_sample_csv_data):
        files_data = [sample_csv_data, extra_sample_csv_data]
        headers, data = data_combine(files_data)
        assert headers[0] == ['country', 'gdp']
        assert len(data) == 6 + 3
