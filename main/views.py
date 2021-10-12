from django.shortcuts import render
from django.views import View


class AdminPage(View):
    def get(self, request):
        return render(request, 'main/admin-page.html')




class DataEntryPage(View):
    def get(self, request):
        return render(request, 'main/dataEntry-page.html')


class ManagerPage(View):
    def get(self, request):
        return render(request, 'main/manager-page.html')


class ResidentPage(View):
    def get(self, request):
        return render(request, 'main/resident-page.html')
