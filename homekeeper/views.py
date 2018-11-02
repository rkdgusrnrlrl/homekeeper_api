from rest_framework import viewsets
from homekeeper.models import Homekeeper
from homekeeper.serializers import HomekeeperSerializer
from rest_framework.response import Response
from django.db.models import Sum


class HomeKeeperViewSet(viewsets.ModelViewSet):
    queryset = Homekeeper.objects.all()
    serializer_class = HomekeeperSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        m = request.query_params.get('month')
        if m is not None:
            queryset = queryset.filter(pay_date__month=m)

        in_sum = self.sum_money_by_inout(queryset, 'IN')
        out_sum = self.sum_money_by_inout(queryset, 'OUT')
        total = in_sum - out_sum

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'total': total,
            'list': serializer.data
        })

    def sum_money_by_inout(self, queryset, inout):
        result = queryset.filter(inout=inout).aggregate(Sum('money'))
        return result['money__sum'] if result['money__sum'] else 0
