from rest_framework import viewsets
from homekeeper.models import Homekeeper
from homekeeper.serializers import HomekeeperSerializer
from rest_framework.response import Response


class HomeKeeperViewSet(viewsets.ModelViewSet):
    queryset = Homekeeper.objects.all()
    serializer_class = HomekeeperSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        m = request.query_params.get('month')
        if m is not None:
            queryset = queryset.filter(pay_date__month=m)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
