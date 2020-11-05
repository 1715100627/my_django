from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from projects.models import Projects
from interfaces.models import Interfaces
from projects.serializer import ProjectModeSerializer, ProjectNameSerializer, InterfacesByProjectIdSerializer
from rest_framework.decorators import action

from projects.utils import get_paginated_response


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.filter(is_delete=False)
    serializer_class = ProjectModeSerializer
    # 指定过滤引擎
    # filter_fields = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'tester']
    # 指定权限类
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()  # 逻辑删除

    # 可以是用action装饰器声明自定义的动作
    # detail(url是否需要传递Pk，一条数据为True)
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProjectNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def interfaces(self, request, pk=None):
        interface_objs = Interfaces.objects.filter(project_id=pk, is_delete=False)
        one_list = []
        for obj in interface_objs:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)

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
