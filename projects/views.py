from rest_framework import viewsets
from rest_framework.response import Response

from projects.models import Projects
from projects.serializer import ProjectModeSerializer, ProjectNameSerializer
from rest_framework.decorators import action


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectModeSerializer
    # 指定过滤引擎
    # filter_fields = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'tester']

    # 可以是用action装饰器声明自定义的动作
    # detail(url是否需要传递Pk，一条数据为True)
    @action(methods=['get'], detail=False)
    def names(self, request):
        queryset = self.get_queryset()
        serializer = ProjectNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)
