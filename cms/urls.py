# from django.urls import path
# from cms.views import (
#     AddVisitFormView,
#     EditVisitFormView,
#     HomePageView,
#     CustomerTableView,
#     export_users_xls,
#     export_new_users_xls,
# )
#
# urlpatterns = [
#     path('', HomePageView.as_view(), name='cms_main_page'),
#     path('dashboard/', HomePageView.as_view(), name='cms_dashboard'),
#     path('customers/', CustomerTableView.as_view(), name='cms_customers'),
#     path('add-visit/', AddVisitFormView.as_view(), name='add_visit_page'),
#     path('edit-visit/<int:pk>', EditVisitFormView.as_view(), name='edit_visit_page'),
#     path('export/xls/', export_users_xls, name='export_users_xls'),
#     path('export/xls/new', export_new_users_xls, name='export_new_users_xls'),
# ]
