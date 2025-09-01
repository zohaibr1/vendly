from .models import Cart

def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(
            customer=request.user,
            is_active=True
        )
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        cart, _ = Cart.objects.get_or_create(session_key=session_key,is_active=True)

    return cart
