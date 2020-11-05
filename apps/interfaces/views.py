from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from interfaces.models import Interfaces
from interfaces.serializer import InterfacesModeSerializer

from projects.utils import get_paginated_response


class InterfacesViewSet(viewsets.ModelViewSet):
    queryset = Interfaces.objects.filter(is_delete=False)
    serializer_class = InterfacesModeSerializer
    # 指定过滤引擎
    # filter_fields = [DjangoFilterBackend]
    filter_fields = ['id', 'name']
    # 指定权限类
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()  # 逻辑删除

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = serializer.data
            datas = get_paginated_response(datas)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
