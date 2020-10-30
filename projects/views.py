from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from projects.models import Projects
from rest_framework.filters import OrderingFilter
from projects.serializer import ProjectSerializer, ProjectModeSerializer


class ProjectsList(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModeSerializer
    # 指定过滤引擎
    # filter_fields = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'tester']

    def get(self, request):
        project_qs = self.get_queryset()
        project_qs = self.filter_queryset(project_qs)

        page = self.paginate_queryset(project_qs)
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(instance=project_qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors)
        project = serializer.save()

        serializer = self.get_serializer(instance=project)
        return Response(serializer.data, status=201)


class ProjectDetail(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModeSerializer

    def get(self, request, pk):
        project = self.get_object()

        serializer = self.get_serializer(instance=project)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        project = self.get_object()
        serializer = self.get_serializer(instance=project, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors)

        serializer.save()

        return Response(serializer.data, status=201)

    def delete(self, request, pk):
        project = self.get_object()
        project.delete()
        return Response(None, status=204)
