from django.shortcuts import render

def main_view(request):
    return render(request, "vacancies/index.html")

def vacancies_view(request):
    return render(request, "vacancies/vacancies.html")

def cat_view(request):
    return render(request, "vacancies/category.html")

def companies_view(request):
    return render(request, "vacancies/company.html")

def one_vac_view(request):
    return render(request, "vacancies/vacancy.html")
