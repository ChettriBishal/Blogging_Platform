from utils.admin_only import admin
from config.prompts import ONLY_ADMIN
from config.roles import Role


class TempUser:
    def __init__(self, user_role):
        self.user_role = user_role


class TestAdminOnly:
    def test_admin_decorator(self):
        @admin
        def admin_only_function(current_user):
            return "Success!"

        # Test case 1: Admin user

        admin_user = TempUser(user_role=Role.ADMIN.value)
        result = admin_only_function(admin_user)
        assert result == "Success!"

        # Test case 2: Non-admin user
        def non_admin_case():
            non_admin_user = TempUser(user_role=Role.BLOGGER.value)
            try:
                admin_only_function(non_admin_user)
            except PermissionError as e:
                assert str(e) == ONLY_ADMIN

        non_admin_case()

