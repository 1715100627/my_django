from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from projects.models import Projects
from rest_framework.filters import OrderingFilter
from projects.serializer import ProjectSerializer, ProjectModeSerializer


class ProjectsList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModeSerializer
    # 指定过滤引擎
    # filter_fields = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'tester']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectDetail(GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Projects.objects.all()
    serializer_class = ProjectModeSerializer

    def get(self, request, *args, **kwargs):
        self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
