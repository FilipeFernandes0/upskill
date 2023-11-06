from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Categories,Expense
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from userpreferences.models import UserPreferences
import datetime
import csv
from django.http import HttpResponse
import xlwt







def search_expenses(request):
# This function handles the search functionality for expenses based on various parameters

    if request.method == 'POST':
        # Retrieving the search text from the request body
        search_str = json.loads(request.body).get('searchText')
        # Filtering expenses based on the search text and the owner's user ID

        expenses=Expense.objects.filter(
            amount__istartswith=search_str, owner=request.user) | Expense.objects.filter(
            date__istartswith=search_str, owner=request.user) | Expense.objects.filter(
            description__icontains=search_str, owner=request.user) | Expense.objects.filter(
            category__istartswith=search_str, owner=request.user)
# Converting the queryset into a list of dictionaries and returning it as a JSON response

        data = expenses.values()

        return JsonResponse(list(data),safe=False)




@login_required(login_url='/authentication/login')
def index(request):
    categories= Categories.objects.all()
    expenses= Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses,4)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator,page_number)
    currency= UserPreferences.objects.get(user=request.user).currency
    context={
        'expenses':expenses,
        'page_obj':page_obj,
        'currency':currency
    }
    return render(request,'expenses/index.html',context)

@login_required(login_url='/authentication/login')
def add_expense(request):
    categories= Categories.objects.all()

    context = {
        'categories':categories,
        'values':request.POST
        }

    if request.method == 'GET':        

        return render(request,'expenses/add_expense.html',context)

    if request.method == 'POST':
        amount=request.POST['amount']

        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'expenses/add_expense.html',context)
        
    
        description=request.POST['description']
        date=request.POST['expense_date']
        category=request.POST['category']


        if not description:
            messages.error(request,'description is required')
            return render(request,'expenses/add_expense.html',context)
        
        Expense.objects.create(owner=request.user,amount=amount,date=date,category=category,description=description)
        messages.success(request,'Expense saved successfully')
        return redirect('expenses')
    
@login_required(login_url='/authentication/login')
def expense_edit(request,id):
    expense = Expense.objects.get(pk=id)
    categories= Categories.objects.all()

    context={
        'expense':expense,
        'values':expense,
        'categories':categories
    }

    if request.method == 'GET':
        return render(request,'expenses/edit-expense.html',context)
    if request.method == 'POST':
        amount=request.POST['amount']

        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'expenses/edit-expense.html',context)
        
    
        description=request.POST['description']
        date=request.POST['expense_date']
        category=request.POST['category']


        if not description:
            messages.error(request,'description is required')
            return render(request,'expenses/edit-expense.html',context)
        

        expense.owner = request.user
        expense.amount = amount
        expense.date = date
        expense.category = category

        expense.description = description
        expense.save()

        messages.success(request,'Expense updated successfully')
        return redirect('expenses')


@login_required(login_url='/authentication/login')
def delete_expense(request,id):


    expense=Expense.objects.get(pk=id)
    
    expense.delete()
    messages.success(request,'Expense removed')
    return redirect('expenses')


# This view function calculates the total expenses for each category within the last six months and returns the data as a JSON response.

def expense_category_summary(request):
        # Get the current date

    todays_date = datetime.date.today()
     # Calculate the date six months ago
    six_months_ago = todays_date - datetime.timedelta(days=30*6)
    # Retrieve all expenses for the logged-in user within the last six months

    expenses = Expense.objects.filter(owner=request.user,date__gte=six_months_ago,date__lte=todays_date)
    # Initialize an empty dictionary to store the final report

    finalrep = {}
    # Define a function to extract the category from an expense object

    def get_category(expense):
        return expense.category

# Create a list of unique categories from the expenses

    category_list = list(set(map(get_category,expenses)))

# Define a function to calculate the total expense amount for a specific category

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)

        for item in filtered_by_category:
            amount+=item.amount

        return amount
        
# Calculate the total expense amount for each category and store the result in the final report dictionary
    
    for x in expenses:
        for y in category_list:
            finalrep[y]= get_expense_category_amount(y)

    return JsonResponse({'expense_category_data': finalrep},safe=False)


def stats_view(request):
    return render(request,'expenses/stats.html')


def export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=Expenses'+str(datetime.datetime.now())+'.csv'

    writer = csv.writer(response)
    writer.writerow(['Amount','Description','Category','Date'])

    expenses=Expense.objects.filter(owner=request.user)

    for expense in expenses:
        writer.writerow([expense.amount, expense.description,expense.category,expense.date])

    return response


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expenses'+str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Amount','Description','Category','Date']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()

    rows = Expense.objects.filter(owner=request.user).values_list('amount','description','category','date')

    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)

    wb.save(response)

    return response




