'''
  @author: hongzai
  @contact: 2505811377@qq.com
  @file: urls.py
  @time: 2022/4/8 12:23
  @desc:
  '''
from rest_framework.routers import SimpleRouter

from .views import CrudDemoModelViewSet

router = SimpleRouter()
router.register("api/crud_demo", CrudDemoModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls