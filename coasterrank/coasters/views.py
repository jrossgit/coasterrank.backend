from rest_framework import generics

from serializers import RollerCoasterSerializer
from models import RollerCoaster


class RollerCoasterListView(generics.ListAPIView):
    """List view for all roller coasters"""
    queryset = RollerCoaster.objects.all()
    serializer_class = RollerCoasterSerializer
