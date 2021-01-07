from .models import Reservation, ReservedTable, LastVisit
from rest_framework import viewsets, permissions
from .serializer import ReservationSerializer, ReservedTableSerializer, LastVisitSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.AllowAny]


class ReservedTableViewSet(viewsets.ModelViewSet):
    queryset = ReservedTable.objects.all()
    serializer_class = ReservedTableSerializer
    permission_classes = [permissions.AllowAny]


class LastVisitViewSet(viewsets.ModelViewSet):
    queryset = LastVisit.objects.all()
    serializer_class = LastVisitSerializer
    permission_classes = [permissions.AllowAny]
