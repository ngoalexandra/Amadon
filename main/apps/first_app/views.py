from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, strptime, localtime
from datetime import datetime

def index(request):
    return render(request, 'first_app/index.html')

def process(request):
    # refer back to product_id within the hidden input. For example, if the value of the product_id = 1, it will pull from the price '1' below which = $18.99
    price = {
        '1' : 18.99,
        '2' : 27.99,
        '3' : 12.99,
        '4' : 4.99,
    }
    quantity = request.POST['quantity']
    product = request.POST['product_id']
    # this is saying that the total is the amount (quantity) of items bought and multiply that by the price
    # you do not need to put qoutes around price[product] because product is already a string (REFER TO PRODUCT) in code above
    request.session['total'] = int(quantity) * price[product]
    # if there is no total purchase in session , total purchase will now equal to total
    if 'total_purchase' not in request.session:
        request.session['total_purchase'] = request.session['total']
    # if total purchase is in session we want to increment
    else: 
        request.session['total_purchase'] += request.session['total']
        # this will determine how many items you bought depending on the number you click in the dropdown bar
        request.session['number_of_items'] = int(quantity)
    if 'buy' in request.POST:
        redirect('/checkout')
    return redirect('/checkout')



def checkout(request):
    return render(request, 'first_app/result.html')

def back(request):
    return redirect('/')
