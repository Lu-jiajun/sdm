from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel, CoreModel2
from dvadmin.system.models import Users
from django.utils import timezone


class ForeignerModel(models.Model):
    外来人员编号 = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    外来人员姓名 = models.CharField(max_length=255, verbose_name="姓名")
    # Student_ID = models.CharField(max_length=255, verbose_name="学号")
    # inventory = models.IntegerField(verbose_name="库存量")
    # goods_price = models.FloatField(verbose_name="商品定价")
    宿舍号 = models.IntegerField(verbose_name="宿舍号")
    来访时间 = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="来访时间",
                                    verbose_name="来访时间")

    离开时间 = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="来访时间",
                                    verbose_name="来访时间")

    目的 = models.CharField(max_length=255, verbose_name="目的")
    宿管ID = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',
                               related_name='宿管ID_F', verbose_name="宿舍管理员")

    电话 = models.CharField(max_length=32, verbose_name="联系电话", null=True, blank=True,
                            help_text="联系电话")

    class Meta:
        db_table = "外来人员登记表"
        verbose_name = '外来人员登记表'
        verbose_name_plural = verbose_name
        ordering = ('来访时间',)


#
# class StudentInfoModel(CoreModel):
#     foreigner_name = models.CharField(max_length=255, verbose_name="姓名")
#     # Student_ID = models.CharField(max_length=255, verbose_name="学号")
#     inventory = models.IntegerField(verbose_name="库存量")
#     # goods_price = models.FloatField(verbose_name="商品定价")
#     dormitory_number = models.IntegerField(verbose_name="宿舍号")
#     visit_datatime = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="来访时间",
#                                           verbose_name="来访时间")
#
#     leave_datatime = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="来访时间",
#                                           verbose_name="来访时间")
#
#     purpose = models.CharField(max_length=255, verbose_name="目的")
#
#     # duty_personnel_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
#     # 在 dormitory.ForeignerModel 模型中有两个字段（creator 和 duty_personnel_id）引用相同的模型，但没有设置 related_name，导致反向关联名称冲突了。你可以通过在字段中添加 related_name 参数来解决这个问题。
#
#     creator = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='foreigner_creator')
#
#     duty_personnel_id = models.ForeignKey(Users, on_delete=models.CASCADE,
#                                           related_name='foreigner_duty_personnel')
#
#     foreigner_phone_number = models.CharField(max_length=32, verbose_name="联系电话", null=True, blank=True,
#                                               help_text="联系电话")
#
#     class Meta:
#         db_table = "dormitory_foreigner"
#         verbose_name = '外来人员登记表'
#         verbose_name_plural = verbose_name
#         ordering = ('visit_datatime',)


class RepairApplicationModel(models.Model):
    报修ID = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    楼号 = models.CharField(max_length=255, verbose_name="楼号")
    学号 = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',
                             related_name='学号_R', verbose_name="学号")
    报修名称 = models.CharField(max_length=30, verbose_name="报修名称")
    报修内容 = models.CharField(max_length=255, verbose_name="报修内容", null=True, blank=True, help_text="报修内容")
    报修日期 = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="报修日期",
                                    verbose_name="报修日期")
    审核状态 = models.CharField(max_length=255, verbose_name="审核状态", null=True, blank=True, help_text="审核状态")
    解决日期 = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="解决日期",
                                    verbose_name="解决日期")
    宿管ID = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',
                               related_name='宿管ID_R', verbose_name="宿管ID", default='admin')

    class Meta:
        db_table = "维修申请表"
        verbose_name = "维修申请表"
        verbose_name_plural = verbose_name
        ordering = ('报修ID',)


class StudentInfoModel(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    楼号 = models.CharField(max_length=255, verbose_name="楼号")
    宿舍号 = models.IntegerField(verbose_name="宿舍号")
    床号 = models.IntegerField(verbose_name="床号")
    学号 = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',
                             related_name='学号_SF', verbose_name="学号")

    # repair_title = models.CharField(max_length=30, verbose_name="维修名称")

    class Meta:
        db_table = "学生信息表"
        verbose_name = "学生信息表"
        verbose_name_plural = verbose_name
        ordering = ('学号',)


class DormitoryInfoModel(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    楼号 = models.CharField(max_length=255, verbose_name="楼号")
    宿舍号 = models.IntegerField(verbose_name="宿舍号")
    总床位数 = models.IntegerField(verbose_name="总床位数")
    空床位数 = models.IntegerField(verbose_name="空床位数")
    # Student_ID = models.CharField(max_length=255, verbose_name="学号")
    寝室长ID = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',
                                 related_name='寝室长ID_R', verbose_name="寝室长ID", blank=True, null=True)

    class Meta:
        db_table = "宿舍信息表"
        verbose_name = "宿舍信息表"
        verbose_name_plural = verbose_name
        ordering = ('宿舍号',)
        unique_together = ('楼号', '宿舍号')
        indexes = [
            models.Index(fields=["楼号", "宿舍号"]),
        ]


class StudentStatueModel(models.Model):
    # building_number = models.CharField(max_length=255, verbose_name="楼号")
    # dormitory_number = models.IntegerField(verbose_name="宿舍号")
    # total_bed_number = models.IntegerField(verbose_name="总床号")
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    学生状态 = models.CharField(max_length=8, verbose_name="学生状态", default='在校')
    学号 = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',
                              verbose_name="学号", unique=True, related_name='学号_username')
    # 学号 = models.CharField(max_length=150, unique=True, db_index=True, verbose_name="用户账号",
    #                         help_text="学号")
    开始时间 = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="开始时间",
                                    verbose_name="开始时间")
    结束时间 = models.DateTimeField(auto_now=False, null=True, blank=True, help_text="结束时间",
                                    verbose_name="结束时间")

    # head_of_dormitory = models.CharField(max_length=30, verbose_name="宿舍长id")

    class Meta:
        db_table = "学生状态表"
        verbose_name = "学生状态表"
        verbose_name_plural = verbose_name
        ordering = ('开始时间',)


class dormitory_management(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    楼号 = models.CharField(max_length=255, verbose_name="楼号")

    # dormitory_number = models.IntegerField(verbose_name="宿舍号")
    # total_bed_number = models.IntegerField(verbose_name="总床号")
    # statue = models.CharField(max_length='8', verbose_name="statue")
    # Student_ID = models.CharField(max_length=255, verbose_name="学号")
    宿管ID = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',
                               related_name='宿管ID_Dm', verbose_name="宿舍管理员", unique=False)

    # head_of_dormitory = models.CharField(max_length=30, verbose_name="宿舍长id")

    class Meta:
        db_table = "宿管信息表"
        verbose_name = "宿管信息表"
        verbose_name_plural = verbose_name
        ordering = ('楼号',)
        unique_together = ('楼号', '宿管ID')
        indexes = [
            models.Index(fields=["楼号", "宿管ID"]),
        ]


class CommApplicationModel(CoreModel2):
    # building_number = models.CharField(max_length=255, verbose_name="楼号")
    # dormitory_number = models.IntegerField(verbose_name="宿舍号")
    # total_bed_number = models.IntegerField(verbose_name="总床号")
    # empty_bed_number = models.IntegerField(verbose_name="空床号")
    # Student_ID = models.CharField(max_length=255, verbose_name="学号")
    # head_of_dormitory = models.CharField(max_length=30, verbose_name="宿舍长id")
    OPTION_CHOICES = [
        (0, '留宿'),
        (1, '退宿'),
        (2, '换宿'),
    ]
    STATUS_CHOICES = [
        (0, '未审批'),
        (1, '审批通过'),
        (2, '不予通过'), ]
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    选项 = models.CharField(max_length=8, default='留校申请')
    学号 = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username',
                             related_name='学号_A', verbose_name="学号")
    开始时间 = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="开始时间",
                                    verbose_name="开始时间")
    结束时间 = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="结束时间",
                                    verbose_name="结束时间")
    原因 = models.CharField(max_length=255, verbose_name="原因", null=True, blank=True, help_text="原因")
    # statu = models.IntegerField(choices=STATUS_CHOICES, default=0)
    审核状态 = models.CharField(max_length=16, default="未审批")
    床号 = models.CharField(max_length=16, default="1",null=True)
    宿舍号 = models.CharField(max_length=16, default="318",null=True)

    class Meta:
        db_table = "申请表"
        verbose_name = "申请表"
        verbose_name_plural = verbose_name
        ordering = ('学号',)
        unique_together = ('学号', '选项', "开始时间")
        indexes = [
            models.Index(fields=["学号", "选项", "开始时间"], name="index"),
        ]

    def save(self, *args, **kwargs):
        # 如果模型实例不存在主键值（新记录），不设置结束时间
        if not self.pk:
            super().save(*args, **kwargs)
        else:
            # 如果模型实例存在主键值（更新记录），设置结束时间为当前时间
            self.结束时间 = timezone.now()
            super().save(*args, **kwargs)

