import json
import logging
import requests
import xlwt
from django.http import HttpResponse
from search_listview.list import SearchableListView
from django.contrib import messages
from django.shortcuts import render
from django.views import generic
from . import constants as cms_app_constants
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from datetime import datetime,timedelta
from django.utils import timezone


class HomePageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'cms/home.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return context

