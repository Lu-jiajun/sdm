'''
  @author: hongzai
  @contact: 2505811377@qq.com
  @file: urls.py
  @time: 2022/4/8 12:23
  @desc:
  '''
from rest_framework.routers import SimpleRouter

from .views import ForeignerRegistrationView, RepairApplicationModelView, dormitory_managementView, \
    DormitoryInfoModelView, StudentStatueModelView, StudentInfoModelView, CommApplicationModelView0, \
    CommApplicationModelView1, CommApplicationModelView2

router = SimpleRouter()
router.register("api/foreigner_registration", ForeignerRegistrationView)
router.register("api/repair_application", RepairApplicationModelView)
router.register("api/student_info", StudentInfoModelView)
router.register("api/student_statue", StudentStatueModelView)
router.register("api/dormitory_info", DormitoryInfoModelView)
router.register("api/dormitory_management", dormitory_managementView)
# CommApplicationModelView0
router.register("api/comm_application0", CommApplicationModelView0)
router.register("api/comm_application1", CommApplicationModelView1)
router.register("api/comm_application2", CommApplicationModelView2)

urlpatterns = [
]
urlpatterns += router.urls
