import re
from django.shortcuts import render,redirect

# Create your views here.
def view_bag(request):
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add product to bag"""
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag',{})
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    
    if size: 
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys(): #if item already in bag, add item Id, size + quantity to dictionary
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size':{size:quantity}} #if not already in bag, create dictionary of item, so 1 item ID can hold multiple size entries 'item by size : xl:1'
            
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity                
        bag[item_id] = quantity
    
    request.session['bag'] = bag
 
    return redirect(redirect_url)