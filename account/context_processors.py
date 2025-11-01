def user_profile(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    return {'user_profile': profile}


def cart_item_count(request):
    print('hi')
    cart = request.session.get('cart', {})
    # فرض بر اینکه cart ساختار {product_id: quantity} دارد
    return {'cart_item_count': len(cart)}


