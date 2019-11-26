from rest_framework import permissions
from rest_framework_simplejwt import authentication
class TestView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)
    def get(self, request, *args, **kwargs):
        return Response('ok')