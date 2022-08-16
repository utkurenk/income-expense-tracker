from django.shortcuts import render, redirect
from .models import Transaction
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect
from .filters import TransactionFilter


@login_required(login_url="/login")
def index(request):
    user = request.user
    transactions = Transaction.objects.filter(Client=user)
    balance = 0
    for i in transactions:
        if i.Type == "Income":
            balance += i.Amount
        else:
            balance -= i.Amount
    my_filter = TransactionFilter(request.GET, queryset=transactions)
    transactions = my_filter.qs
    context = {
        "transactions": transactions,
        "balance": balance,
        "my_filter": my_filter,
    }
    return render(request, 'index.html', context)


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(request, "registration/sign_up.html", {"form": form})


@login_required(login_url="/login")
def income(request):
    user = request.user
    transaction = Transaction.objects.filter(Client=user)
    context = {
        "transaction": transaction
    }
    return render(request, 'income.html', context)


@login_required(login_url="/login")
def add_one(request):
    x = request.POST['Amount']
    transactions = Transaction(Type="Income", Amount=x)
    transactions.Client = request.user
    transactions.save()
    return HttpResponseRedirect(reverse('income'))


@login_required(login_url="/login")
def expense(request):
    user = request.user
    transactions = Transaction.objects.filter(Client=user)
    context = {
        "transactions": transactions,
    }
    return render(request, 'expense.html', context)


@login_required(login_url="/login")
def add_two(request):
    x = request.POST['Amount']
    y = request.POST["Category"]
    transaction = Transaction(Type="Expense", Amount=x, Category=y)
    transaction.Client = request.user
    transaction.save()
    return HttpResponseRedirect(reverse('expense'))
