# Create your views here.
from dormitory.models import ForeignerModel, RepairApplicationModel, StudentInfoModel, DormitoryInfoModel, \
    StudentStatueModel, dormitory_management, CommApplicationModel
from dormitory.serializers import ForeignerModelSerializer, ForeignerModelCreateUpdateSerializer, \
    RepairApplicationModelSerializer, RepairApplicationModelCreateUpdateSerializer, StudentInfoModelModelSerializer, \
    StudentInfoModelCreateUpdateSerializer, DormitoryInfoModelCreateUpdateSerializer, DormitoryInfoModelSerializer, \
    StudentStatueModelCreateUpdateSerializer, StudentStatueModelSerializer, dormitory_managementCreateUpdateSerializer, \
    dormitory_managementSerializer, CommApplicationModelSerializer0, CommApplicationModelCreateUpdateSerializer0
from dvadmin.utils.json_response import DetailResponse, SuccessResponse
from dvadmin.utils.viewset import CustomModelViewSet
from rest_framework.response import Response
from rest_framework import status
from dvadmin.system.models import Users


class ForeignerRegistrationView(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ForeignerModel.objects.all()
    serializer_class = ForeignerModelSerializer
    create_serializer_class = ForeignerModelCreateUpdateSerializer
    update_serializer_class = ForeignerModelCreateUpdateSerializer

    filter_fields = ['电话', '外来人员编号', '外来人员姓名', '宿舍号', '来访时间', '离开时间', '目的', '宿管ID']
    search_fields = ['来访时间']

    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self,request,*args,**kwargs):
    #     print("hello")
    #     return Response(data={'code': status.HTTP_200_OK, 'message': '删除成功'})
    #     # pass


class RepairApplicationModelView(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = RepairApplicationModel.objects.all()
    serializer_class = RepairApplicationModelSerializer
    create_serializer_class = RepairApplicationModelCreateUpdateSerializer
    update_serializer_class = RepairApplicationModelCreateUpdateSerializer
    # 报修日期     审核状态    宿管ID    解决日期    报修内容    报修名称    学号    楼号    报修ID
    filter_fields = ['报修ID', '报修日期', '审核状态', '宿管ID', '解决日期', '报修内容', '报修名称', '学号', '楼号']
    search_fields = ['学号']


class StudentInfoModelView(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = StudentInfoModel.objects.all()
    serializer_class = StudentInfoModelModelSerializer
    create_serializer_class = StudentInfoModelCreateUpdateSerializer
    update_serializer_class = StudentInfoModelCreateUpdateSerializer
    # 学生信息（学号，姓名，性别，楼号，宿舍号，床位号，部门ID，联系方式）
    filter_fields = ['学号', '楼号', '宿舍号', '床号']
    search_fields = ['学号']


class DormitoryInfoModelView(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = DormitoryInfoModel.objects.all()
    serializer_class = DormitoryInfoModelSerializer
    create_serializer_class = DormitoryInfoModelCreateUpdateSerializer
    update_serializer_class = DormitoryInfoModelCreateUpdateSerializer
    # 宿舍信息（楼号，宿舍号，总床位数，空床位数，寝室长ID）

    filter_fields = ['楼号', '宿舍号', '总床位数', '空床位数', '寝室长ID']
    search_fields = ['宿舍号']


# StudentStatueModel

class StudentStatueModelView(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = StudentStatueModel.objects.all()
    serializer_class = StudentStatueModelSerializer
    create_serializer_class = StudentStatueModelCreateUpdateSerializer
    update_serializer_class = StudentStatueModelCreateUpdateSerializer
    # 学生状态（学号，状态，开始时间，结束时间）
    filter_fields = ['学号', '学生状态', '开始时间', '开始时间']
    search_fields = ['学号']


class dormitory_managementView(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = dormitory_management.objects.all()
    serializer_class = dormitory_managementSerializer
    create_serializer_class = dormitory_managementCreateUpdateSerializer
    update_serializer_class = dormitory_managementCreateUpdateSerializer
    filter_fields = ['楼号', '宿管ID']
    search_fields = ['楼号']


class CommApplicationModelView0(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = CommApplicationModel.objects.all()
    serializer_class = CommApplicationModelSerializer0
    create_serializer_class = CommApplicationModelCreateUpdateSerializer0
    update_serializer_class = CommApplicationModelCreateUpdateSerializer0
    # 学号，选项，开始时间，结束时间，原因，审核状态
    filter_fields = ['学号', '选项', '原因', '审核状态', '开始时间', '结束时间']
    search_fields = ['学号']

    def create(self, request, *args, **kwargs):
        # 获取 POST 请求中的数据
        data = request.data.copy()  # 创建数据的副本以防修改原始数据
        # 添加新的键值对
        data['选项'] = "留校申请"
        # 将修改后的数据重新赋值给 request.data
        # request.data = data

        serializer = self.get_serializer(data=data, request=request)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return DetailResponse(data=serializer.data, msg="新增成功")

    def list(self, request, *args, **kwargs):
        # print('------------------------------------------------------------------------------')
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, request=request)
            option_1_data = [item for item in serializer.data if item.get('选项') == '留校申请']
            return SuccessResponse(data=option_1_data, msg="获取成功")
            # return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True, request=request)
        # return SuccessResponse(data=serializer.data, msg="获取成功")
        # print('------------------------------------------------------------------------------')
        option_1_data = [item for item in serializer.data if item.get('选项') == '留校申请']
        return SuccessResponse(data=option_1_data, msg="获取成功")

class CommApplicationModelView1(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = CommApplicationModel.objects.all()
    serializer_class = CommApplicationModelSerializer0
    create_serializer_class = CommApplicationModelCreateUpdateSerializer0
    update_serializer_class = CommApplicationModelCreateUpdateSerializer0
    filter_fields = ['学号', '选项', '原因', '审核状态', '开始时间', '结束时间']
    search_fields = ['学号']

    def create(self, request, *args, **kwargs):
        # 获取 POST 请求中的数据
        data = request.data.copy()  # 创建数据的副本以防修改原始数据
        # 添加新的键值对
        data['选项'] = "退宿申请"
        # 将修改后的数据重新赋值给 request.data
        # request.data = data

        serializer = self.get_serializer(data=data, request=request)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return DetailResponse(data=serializer.data, msg="新增成功")

    # def list(self, request, *args, **kwargs):
    #     # queryset = self.filter_queryset(self.get_queryset())
    #     # 获取符合条件的 queryset
    #     queryset = CommApplicationModel.objects.filter(选项="退宿申请")
    #
    #     # 更新符合条件的记录的 option 字段为 "留校申请"
    #     # queryset.update(option="退宿申请")
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True, request=request)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(queryset, many=True, request=request)
    #     return SuccessResponse(data=serializer.data, msg="获取成功")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, request=request)
            option_1_data = [item for item in serializer.data if item.get('选项') == '退宿申请']
            return SuccessResponse(data=option_1_data, msg="获取成功")
            # return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True, request=request)
        # return SuccessResponse(data=serializer.data, msg="获取成功")
        option_1_data = [item for item in serializer.data if item.get('选项') == '退宿申请']
        return SuccessResponse(data=option_1_data, msg="获取成功")


class CommApplicationModelView2(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = CommApplicationModel.objects.all()
    serializer_class = CommApplicationModelSerializer0
    create_serializer_class = CommApplicationModelCreateUpdateSerializer0
    update_serializer_class = CommApplicationModelCreateUpdateSerializer0
    filter_fields = ['学号', '选项', '原因', '审核状态', '开始时间', '结束时间']
    search_fields = ['学号']

    def create(self, request, *args, **kwargs):
        # 获取 POST 请求中的数据
        data = request.data.copy()  # 创建数据的副本以防修改原始数据
        # 添加新的键值对
        data['选项'] = "换宿申请"
        # 将修改后的数据重新赋值给 request.data
        # request.data = data

        serializer = self.get_serializer(data=data, request=request)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return DetailResponse(data=serializer.data, msg="新增成功")

    # def list(self, request, *args, **kwargs):
    #     # queryset = self.filter_queryset(self.get_queryset())
    #     # 获取符合条件的 queryset
    #     queryset = CommApplicationModel.objects.filter(选项="换宿申请")
    #
    #     # 更新符合条件的记录的 option 字段为 "留校申请"
    #     # queryset.update(option="换宿申请")
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True, request=request)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(queryset, many=True, request=request)
    #     return SuccessResponse(data=serializer.data, msg="获取成功")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, request=request)
            # return self.get_paginated_response(serializer.data)
            option_1_data = [item for item in serializer.data if item.get('选项') == '换宿申请']
            return SuccessResponse(data=option_1_data, msg="获取成功")
        serializer = self.get_serializer(queryset, many=True, request=request)
        # return SuccessResponse(data=serializer.data, msg="获取成功")
        option_1_data = [item for item in serializer.data if item.get('选项') == '换宿申请']
        return SuccessResponse(data=option_1_data, msg="获取成功")
