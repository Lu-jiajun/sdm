'''
  @author: hongzai
  @contact: 2505811377@qq.com
  @file: serializers.py
  @time: 2022/4/8 11:12
  @desc:
  '''
from crud_demo.models import CrudDemoModel
from dvadmin.utils.serializers import CustomModelSerializer


class CrudDemoModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = CrudDemoModel
        fields = "__all__"


class CrudDemoModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = CrudDemoModel
        fields = '__all__'