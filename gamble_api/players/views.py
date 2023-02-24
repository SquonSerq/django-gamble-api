from players.models import Player
from rest_framework import generics

from .serializers import PlayerSerializer


class PlayerDetailViewSet(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = "bot_id"
