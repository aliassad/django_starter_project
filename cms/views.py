# import json
# import logging
# import requests
# import xlwt
# from django.http import HttpResponse
# from search_listview.list import SearchableListView
# from django.contrib import messages
# from django.shortcuts import render
# from django.views import generic
# from . import constants as cms_app_constants
# from .models import CustomerVisit
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.db.models import Q
# from datetime import datetime,timedelta
# from django.utils import timezone
#
#
# class CustomerTableView(LoginRequiredMixin, generic.ListView):
#     template_name = 'cms/customers_table.html'
#     paginate_by = 10
#     context_object_name = "customers"
#     model = CustomerVisit
#
#     def get_queryset(self):  # new
#         if self.request.GET.get('q'):
#             return CustomerVisit.objects.filter(
#                 Q(first_name__contains=self.request.GET.get('q')) |
#                 Q(last_name__contains=self.request.GET.get('q')) |
#                 Q(phone_number__contains=self.request.GET.get('q')) |
#                 Q(email__contains=self.request.GET.get('q')),
#             )
#         else:
#             return CustomerVisit.objects.all()
#
#
# class PublicHomePageFormView(LoginRequiredMixin, generic.CreateView):
#     """Display the form for recording a new customer visit"""
#     model = CustomerVisit
#     template_name = 'cms/add_visit.html'
#     fields = '__all__'
#     success_url = '/add-visit'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         messages.success(self.request, cms_app_constants.CUSTOMER_VISIT_ADDED)
#         return super().form_valid(form)
#
#
# class HomePageView(LoginRequiredMixin, generic.TemplateView):
#     template_name = 'cms/home.html'
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in the publisher
#         if self.request.user.is_superuser:
#             context['total_patients'] = CustomerVisit.objects.all().count()
#             context['new_patients'] = CustomerVisit.objects.filter(visits=1).count()
#             context['returning_patients'] = CustomerVisit.objects.filter(visits__gt=1).count()
#
#             if 'date_to' in self.request.GET and 'date_from' in self.request.GET:
#                 context['filtered_total_patients'] = CustomerVisit.objects \
#                     .filter(created_at__gte=self.request.GET['date_from']) \
#                     .filter(created_at__lte=self.request.GET['date_to']) \
#                     .count()
#                 context['filtered_new_patients'] = CustomerVisit.objects.filter(visits=1) \
#                     .filter(created_at__gte=self.request.GET['date_from']) \
#                     .filter(created_at__lte=self.request.GET['date_to']) \
#                     .count()
#                 context['filtered_returning_patients'] = CustomerVisit.objects.filter(visits__gt=1) \
#                     .filter(created_at__contains=self.request.GET['date_from']) \
#                     .filter(created_at__lte=self.request.GET['date_to']) \
#                     .count()
#         else:
#             context['total_patients'] = CustomerVisit.objects.filter(
#                 Q(created_at__contains=str(timezone.now().date())) |
#                 Q(updated_at__contains=str(timezone.now().date())))\
#                 .count()
#             context['new_patients'] = CustomerVisit.objects.filter(
#                 created_at__contains=str(timezone.now().date()), visits=1).count()
#             context['returning_patients'] = CustomerVisit.objects.filter(
#                 updated_at__contains=str(timezone.now().date()), visits__gt=1).count()
#         return context
#
#
# class AddVisitFormView(LoginRequiredMixin, generic.CreateView):
#     """Display the form for recording a new customer visit"""
#     model = CustomerVisit
#     template_name = 'cms/add_visit.html'
#     fields = '__all__'
#     success_url = '/cms/add-visit'
#
#     def form_valid(self, form):
#         customer_visit = form.save(commit=False)
#         customer_visit.save()
#         form.instance.user = self.request.user
#         messages.success(self.request, cms_app_constants.CUSTOMER_VISIT_ADDED)
#         return super().form_valid(form)
#
#
# class EditVisitFormView(LoginRequiredMixin, generic.UpdateView):
#     """Display the form for recording a new customer visit"""
#     model = CustomerVisit
#     template_name = 'cms/add_visit.html'
#     fields = '__all__'
#     success_url = '/cms/customers'
#
#     def form_valid(self, form):
#         customer_visit = form.save(commit=False)
#         customer_visit.visits = customer_visit.visits + 1
#         customer_visit.save()
#         form.instance.user = self.request.user
#         messages.success(self.request, cms_app_constants.CUSTOMER_VISIT_ADDED)
#         return super().form_valid(form)
#
#
# def export_users_xls(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="customers_data.xls"'
#
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('customers')
#
#     # Sheet header, first row
#     row_num = 0
#
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#
#     columns = [
#         'Id', 'First name', 'Last name', 'Email address',
#         'Phone number', 'Referral source', 'Street address', 'City',
#         '# Visits', 'First visit date', 'Recent visit date', 'Banned ?',
#     ]
#
#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)
#
#     # Sheet body, remaining rows
#     font_style = xlwt.XFStyle()
#
#     rows = CustomerVisit.objects.all().values_list(
#         'customer_id', 'first_name', 'last_name', 'email',
#         'phone_number', 'referral_source', 'street_address', 'city',
#         'visits', 'created_at', 'updated_at', 'banned'
#
#     )
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)
#
#     wb.save(response)
#     return response
#
#
# def export_new_users_xls(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="new_customers_data.xls"'
#
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('Customers')
#
#     # Sheet header, first row
#     row_num = 0
#
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#
#     columns = [
#         'Id', 'First name', 'Last name', 'Email address',
#         'Phone number', 'Referral source', 'Street address', 'City',
#         '# Visits', 'First visit date', 'Recent visit date', 'Banned ?',
#     ]
#
#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)
#
#     # Sheet body, remaining rows
#     font_style = xlwt.XFStyle()
#
#     rows = CustomerVisit.objects.filter(visits=1).all().values_list(
#         'customer_id', 'first_name', 'last_name', 'email',
#         'phone_number', 'referral_source', 'street_address', 'city',
#         'visits', 'created_at', 'updated_at', 'banned'
#
#     )
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)
#
#     wb.save(response)
#     return response
