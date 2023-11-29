import pytest
from src.utils import take_input


class TestInput:

    @pytest.fixture
    def mocker_validation(self, mocker):
        return mocker.patch('src.utils.take_input.validation')

    def test_get_user_details(self, monkeypatch, mocker):
        input_details = iter(['test_username', 'test_email'])
        monkeypatch.setattr('builtins.input', lambda _: next(input_details))
        mocker.patch('pwinput.pwinput', return_value='test_password')
        monkeypatch.setattr('builtins.input', lambda _: next(input_details))

        result = take_input.get_user_details()

        assert result == ('test_username', 'test_password', 'test_email')

    def test_get_username_password(self, monkeypatch, mocker):
        monkeypatch.setattr('builtins.input', lambda _: 'test_username')
        mocker.patch('pwinput.pwinput', return_value='test_password')

        result = take_input.get_username_password()

        assert result == ('test_username', 'test_password')

    def test_get_new_password(self, mocker):
        mocker.patch('pwinput.pwinput', return_value='test_password')

        result = take_input.get_new_password()
        assert result == 'test_password'

    def test_get_blog_details(self, monkeypatch, mocker_validation):
        details = ['test_title', 'test_content', 'test_tag']

        mocker_validation.validate_empty_input.return_value = False
        monkeypatch.setattr('builtins.input', lambda _: details.pop(0))

        result = take_input.get_blog_post_details()
        assert result == ('test_title', 'test_content', 'test_tag')
        mocker_validation.validate_empty_input.assert_called()

    def test_get_inputs(self, monkeypatch, mocker_validation):
        # testing four functions with similar function body
        test_inputs = ['test_comment', 'test_title', 'test_content', 'test_tag']
        test_inputs_copy = test_inputs[:]
        mocker_validation.validate_empty_input.return_value = False
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))

        results = [take_input.get_comment(), take_input.get_title(), take_input.get_new_content(),
                   take_input.get_tag_name()]

        assert results == test_inputs_copy
        mocker_validation.validate_empty_input.assert_called()

    def test_get_user_for_blog(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'test_user')

        result = take_input.get_user_for_blog()
        assert result == 'test_user'
