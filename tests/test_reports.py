import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
from reports import average_gdp


class TestAverageGdp:
    """Тесты для функции average_gdp"""

    def test_average_gdp(self, sample_csv_data):
        headers, results = average_gdp(sample_csv_data)

        assert headers == ['country', 'avg_gdp']
        assert len(results) == 3

        result_dict = dict(results)
        assert result_dict['United States'] == 24388.5
        assert result_dict['China'] == 17848.5
        assert result_dict['Germany'] == 4079.0

    def test_average_gdp_wrong_data(self, sample_wrong_csv_data):
        headers, results = average_gdp(sample_wrong_csv_data)

        assert headers == ['country', 'avg_gdp']
        assert len(results) == 3

        result_dict = dict(results)
        assert result_dict['United States'] == 24388.5
        assert result_dict['China'] == 17734.0
        assert result_dict['Germany'] == 4079.0