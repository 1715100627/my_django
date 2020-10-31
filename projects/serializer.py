from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from projects.models import Projects
from interfaces.models import Interfaces


# 创建自定义校验器
def is_unique_project_name(name):
    if '项目' not in name:
        raise serializers.ValidationError('项目名中必须包含项目关键词')


class ProjectSerializer(serializers.Serializer):
    # read_only只输出不输入  write_only只输入
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='项目名称', max_length=200, help_text='项目名称',
                                 validators=[UniqueValidator(Projects.objects.all(),
                                                             message='项目名已存在'), is_unique_project_name])
    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programer = serializers.CharField(label='开发人员', max_length=200, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=100, help_text='发布应用')
    # null数据库可以为空 blank前端可以为空 default默认
    desc = serializers.CharField(label='简要描述', help_text='简要描述', allow_null=True, default='', allow_blank=True)

    # 单字段校验
    def validate_name(self, value):
        if not value.endswith("项目"):
            raise serializers.ValidationError('必须以项目结尾')
        return value

    def create(self, validated_data):
        project = Projects.objects.create(**validated_data)
        return project

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance


class ProjectModeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label='项目名称', max_length=200, help_text='项目名称',
                                 validators=[UniqueValidator(Projects.objects.all(),
                                                             message='项目名已存在'), is_unique_project_name])

    class Meta:
        model = Projects
        # filter=('id','name','leader','tester')
        # filter = '__all__'
        exclude = ('publish_app', 'desc')
        # read_only_fields = ('leader', 'tester')
        extra_kwarge = {
            'leader': {
                "write_only": True,
                "error_messages": {"max_length": "最大不超过50个字节"}
            }
        }

    # 单字段校验
    def validate_name(self, value):
        if not value.endswith("项目"):
            raise serializers.ValidationError('必须以项目结尾')
        return value


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name')


class InterfacesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name', 'tester')


class InterfacesByProjectIdSerializer(serializers.ModelSerializer):
    interfaces_set = InterfacesNameSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ('id', 'interfaces_set')
