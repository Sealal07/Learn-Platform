from django.urls import path
from . import views

urlpatterns = [
    path('mine/',
         views.ManageCourseListView.as_view(),
         name='manage_course_list'),

    path('create/',
         views.CourseCreateView.as_view(),
         name='add_course'),

    path('<pk>/edit/',
         views.CourseUpdateView.as_view(),
         name='change_course'),
    path('<pk>/delete/',
         views.CourseDeleteView.as_view(),
         name='delete_course'),
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(),
         name='course_module_update'),
    path('module/<int:module_id>/content/<m_N>/create/',
         views.ContentCreateUpdateView.as_view(),
         name='module_content_create'),
    path('module/<int:module_id>/content/<m_N>/<id>/',
         views.ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path('content/<int:id>/delete/',
         views.ContentDeleteView.as_view(),
         name='module_content_delete'),
    path('module/<int:module_id>/',
         views.ModuleContentListView.as_view(),
         name='module_content_list'),
    path('module/order/', views.ModuleOrderView.as_view(),
         name='module_order'),
    path('content/order/', views.ContentOrderView.as_view(),
         name='content_order'),
    path('<pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path('module/detail/<pk>/', views.ModuleDetailView.as_view(), name='module_detail'),
]
