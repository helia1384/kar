from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product
from django.shortcuts import render
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

# لیست محصولات
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)



# افزودن محصول
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'image']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'image']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        return self.get_object().user == self.request.user



# حذف محصول
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'productس/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        return self.get_object().user == self.request.user



# products/views.py


def product_list(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})

    for product in products:
        pid = str(product.id)
        product.qty_in_cart = cart.get(pid, 0)  # 👈 مقدار موجود در سبد

    return render(request, 'products/product_list.html', {
        'products': products
    })


def cart_detail(request):
    # کد مربوط به نمایش سبد خرید
    return render(request, 'products/cart.html')





# تابع برای آپدیت سبد خرید






logger = logging.getLogger(__name__)

@require_POST
@csrf_exempt
def update_cart(request):
    print("🎯 update_cart view called!")  # برای تست

    try:
        # لاگ request body
        body = request.body.decode('utf-8')
        print(f"📨 Request body: {body}")

        data = json.loads(body)
        product_id = str(data.get('product_id'))
        action = data.get('action')

        print(f"🛍️ Action: {action}, Product ID: {product_id}")

        # دریافت سبد خرید از session
        cart = request.session.get('cart', {})
        print(f"📦 Current cart: {cart}")

        # پردازش action
        if action == 'add':
            cart[product_id] = cart.get(product_id, 0) + 1
            print(f"➕ Added product {product_id}, new count: {cart[product_id]}")
        elif action == 'increase':
            cart[product_id] = cart.get(product_id, 0) + 1
            print(f"📈 Increased product {product_id}, new count: {cart[product_id]}")
        elif action == 'decrease':
            if product_id in cart:
                if cart[product_id] > 1:
                    cart[product_id] -= 1
                    print(f"📉 Decreased product {product_id}, new count: {cart[product_id]}")
                else:
                    del cart[product_id]
                    print(f"🗑️ Removed product {product_id}")

        # ذخیره در session
        request.session['cart'] = cart
        request.session.modified = True

        # محاسبه تعداد کل
        total_count = len(cart)
        product_count = cart.get(product_id, 0)

        print(f"🔄 Updated cart: {cart}")
        print(f"🔢 Total count: {total_count}, Product count: {product_count}")

        return JsonResponse({
            'success': True,
            'cart_count': total_count,
            'product_count': product_count,
            'message': 'سبد خرید بروزرسانی شد'
        })

    except Exception as e:
        print(f"💥 Error in update_cart: {e}")
        import traceback
        traceback.print_exc()

        return JsonResponse({
            'success': False,
            'error': str(e)
        })

def get_cart_count(request):
        cart = request.session.get('cart', {})
        total_count = sum(cart.values())
        return JsonResponse({'cart_count': total_count})