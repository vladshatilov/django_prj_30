from rest_framework.generics import CreateAPIView
from auth_user.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
