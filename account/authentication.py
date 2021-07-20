from django.contrib.auth.models import User

class EmailAuthBackend():
    """
    Authenticate using e-mail address
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username.capitalize())
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class CapitalizedAuthBackend():
    """
    Authenticate using capitalized user
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username.capitalize())
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
