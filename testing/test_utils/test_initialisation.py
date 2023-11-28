from unittest.mock import patch
from src.utils.initialisation import Database, initialize


class TestInitialisation:
    def test_initialize(self):
        with patch.object(Database, 'single_query') as mock_single_query:
            mock_single_query.return_value = True
            result = initialize()

            assert result

            mock_single_query.assert_called()
