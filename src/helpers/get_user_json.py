def user_details(user):
    return {
        'username': user.username,
        'role': user.user_role,
        'email': user.email,
        'registration_date': user.registration_date,
    }
