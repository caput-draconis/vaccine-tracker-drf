from rest_framework_swagger.views import get_swagger_view
from django.urls import path
from student_details import views as student_views
from vaccine_drive import views as vaccine_views

urlpatterns = [
    path('students/', student_views.student_list),
    path('addStudent/', student_views.student_add),
    path('deleteStudent/<int:pk>/', student_views.student_delete),
    path('vaccineDrive/',vaccine_views.vaccine_list),
    path('updateDrive/<int:pk>/',vaccine_views.vaccine_update),
    path('bulkAdd/',student_views.BulkAdd.as_view(), name='student-add'),    
]

schema_view = get_swagger_view(title='Vaccine Tracker API',patterns=urlpatterns)

