from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from products.models import Saree
import razorpay

# 🔑 Razorpay credentials (REPLACE with your real keys!)
razorpay_client = razorpay.Client(auth=("rzp_test_yourkey", "your_secret_key"))

# 🛒 In-memory cart (for demo; not stored in DB)
cart = {}

# ✅ Home Page
def home(request):
    products = Saree.objects.all()
    return render(request, 'home.html', {'products': products})

# 🛍️ Shop Page
def shop(request):
    items = Saree.objects.all()
    return render(request, 'shop.html', {'items': items})

# 🔍 Product Detail Page
def product_detail(request, id):
    item = get_object_or_404(Saree, id=id)
    return render(request, 'product_detail.html', {'item': item})

# ➕ Add to Cart
def add_to_cart(request, saree_id):
    cart[saree_id] = cart.get(saree_id, 0) + 1
    return redirect('cart')

# ➖ Remove from Cart
def remove_from_cart(request, saree_id):
    if saree_id in cart:
        del cart[saree_id]
    return redirect('cart')

# 🧺 Cart Page with Razorpay Integration
def cart_view(request):
    sarees = []
    total_price = 0

    for saree_id, quantity in cart.items():
        saree = get_object_or_404(Saree, id=saree_id)
        saree.quantity = quantity
        saree.total = saree.price * quantity
        total_price += saree.total
        sarees.append(saree)

    # 🧾 Razorpay Order
    razorpay_order = razorpay_client.order.create({
        'amount': int(total_price * 100),  # ₹ to paise
        'currency': 'INR',
        'payment_capture': '1'
    })

    context = {
        'items': sarees,
        'total': total_price,
        'order_id': razorpay_order['id'],
        'razorpay_key': "rzp_test_yourkey",  # Replace in production
    }
    return render(request, 'cart.html', context)

