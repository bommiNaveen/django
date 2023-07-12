from django.urls import path
from .views import studentdetails,post_student,update_student,delete_student



# router = routers.DefaultRouter()
# router.register('student',studentViewSet)

urlpatterns = [

    path ('',studentdetails, name = 'studentdetails'),
    path ('add/',post_student,name = 'post_student'),
    path ('update/<int:id>/',update_student,name = 'update_student'),
    path ('delete/<int:id>/',delete_student,name = 'delete_student'),

]