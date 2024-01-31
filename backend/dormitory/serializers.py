'''
  @author: hongzai
  @contact: 2505811377@qq.com
  @file: serializers.py
  @time: 2022/4/8 11:12
  @desc:
  '''
from dormitory.models import ForeignerModel, RepairApplicationModel, StudentInfoModel, DormitoryInfoModel, \
    StudentStatueModel, dormitory_management, CommApplicationModel
from dvadmin.utils.serializers import CustomModelSerializer
from rest_framework import serializers


class ForeignerModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = ForeignerModel
        fields = "__all__"


class ForeignerModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = ForeignerModel
        fields = '__all__'


# RepairApplicationModel


class RepairApplicationModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = RepairApplicationModel
        fields = "__all__"


class RepairApplicationModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = RepairApplicationModel
        fields = '__all__'


class StudentInfoModelModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = StudentInfoModel
        fields = "__all__"


class StudentInfoModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = StudentInfoModel
        fields = '__all__'


class DormitoryInfoModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = DormitoryInfoModel
        fields = "__all__"


class DormitoryInfoModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = DormitoryInfoModel
        fields = '__all__'


class StudentStatueModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = StudentStatueModel
        fields = "__all__"


class StudentStatueModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = StudentStatueModel
        fields = '__all__'


class dormitory_managementSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = dormitory_management
        fields = "__all__"


class dormitory_managementCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = dormitory_management
        fields = '__all__'


class CommApplicationModelSerializer0(CustomModelSerializer):
    """
    序列化器
    """
    # option = serializers.IntegerField(default=0)

    class Meta:
        model = CommApplicationModel
        fields = "__all__"


class CommApplicationModelCreateUpdateSerializer0(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = CommApplicationModel
        fields = '__all__'

