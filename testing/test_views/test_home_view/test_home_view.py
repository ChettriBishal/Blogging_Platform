import pytest
from src.views.home import Home


class TestHomeView:
    @pytest.fixture
    def mock_signup(self, mocker):
        return mocker.patch('src.views.home.signup', return_value=True)

    @pytest.fixture
    def mock_signin(self, mocker):
        return mocker.patch('src.views.home.signin', return_value=True)

    @pytest.mark.parametrize("options", [('1', '2', '3')])
    def test_home_menu(self, options, monkeypatch, mock_signup, mock_signin):
        option = iter(options)
        monkeypatch.setattr('builtins.input', lambda _: next(option))

        # mock_signin.assert_called()
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            Home.home_menu()

        assert pytest_wrapped_e.type == SystemExit

    @pytest.mark.parametrize('options', [
        ('4', '3',)
    ])
    def test_home_menu_invalid(self, capsys, options, monkeypatch):
        option = iter(options)
        monkeypatch.setattr('builtins.input', lambda _: next(option))

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            Home.home_menu()

        capsys.readouterr()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 0
