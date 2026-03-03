from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, Staff

# Create your views here.

def home(request):
    return render(request, "core/home.html")


def masajes_hombresnv1(request):
    return render(request, "core/masajes_hombresnv1.html")


def masajes_hombresnv2(request):
    return render(request, "core/masajes_hombresnv2.html")


def masajes_hombresnv3(request):
    return render(request, "core/masajes_hombresnv3.html")


def masajes_mujeresnv1(request):
    return render(request, "core/masajes_mujeresnv1.html")


def masajes_mujeresnv2(request):
    return render(request, "core/masajes_mujeresnv2.html")


def masajes_mujeresnv3(request):
    return render(request, "core/masajes_mujeresnv3.html")


def masajes_parejasguiado(request):
    return render(request, "core/masajes_parejasguiado.html")


def masajes_parejassimultaneo(request):
    return render(request, "core/masajes_parejassimultaneo.html")


def clases(request):
    return render(request, "core/clases.html")


def clases_individuales(request):
    return render(request, "core/clases_individuales.html")


def clases_pareja(request):
    return render(request, "core/clases_pareja.html")


def clases_video(request):
    return render(request, "core/clases_video.html")


def video_list(request):
    videos = Video.objects.all()

    context = {
        "videos": videos,
        "min_price": videos.order_by("precio").first().precio if videos.exists() else 0,
        "max_price": videos.order_by("-precio").first().precio if videos.exists() else 0,
    }

    return render(request, "core/videos/video_list.html", context)


def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)

    return render(request, "core/videos/video_detail.html", {
        "video": video
    })
        

def clases_online(request):
    return render(request, "core/clases_online.html")


def practicas(request):
    return render(request, "core/practicas.html")


def talleres(request):
    return render(request, "core/talleres.html")


def staff(request):
    return render(request, "core/staff.html")


def tienda(request):
    return render(request, "core/tienda.html")


def reserva_online(request):
    return render(request, "core/reserva_online.html")


def social(request):
    return render(request, "core/social.html")


def page(request):
    return render(request, "core/page.html")


def contact(request):
    return render(request, "core/contact.html")


def reclutar(request):
    return render(request, "core/reclutar.html")


def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)

    previous_video = Video.objects.filter(id__lt=video.id).order_by('-id').first()
    next_video = Video.objects.filter(id__gt=video.id).order_by('id').first()

    return render(request, "core/videos/video_detail.html", {
        "video": video,
        "previous_video": previous_video,
        "next_video": next_video,
    })

def add_to_cart(request, slug):
    video = get_object_or_404(Video, slug=slug)

    cart = request.session.get("cart", {})

    if slug in cart:
        cart[slug]["quantity"] += 1
    else:
        cart[slug] = {
            "title": video.titulo,
            "price": video.precio,
            "quantity": 1,
            "image": video.imagen.url
        }

    request.session["cart"] = cart
    return redirect("cart_detail")

def cart_detail(request):
    cart = request.session.get("cart", {})
    discount = 0
    promo_code = request.session.get("promo_code", "")

    total = 0

    for item in cart.values():
        item["subtotal"] = item["price"] * item["quantity"]
        total += item["subtotal"]

    if promo_code == "DESCUENTO10":
        discount = total * 0.10

    final_total = total - discount

    return render(request, "core/cart/cart_detail.html", {
        "cart": cart,
        "total": total,
        "discount": discount,
        "final_total": final_total,
        "promo_code": promo_code,
    })

def remove_from_cart(request, slug):
    if request.method == "POST":
        cart = request.session.get("cart", {})

    if slug in cart:
        del cart[slug]

    request.session["cart"] = cart
    return redirect("cart_detail")

def update_cart(request, slug):
    cart = request.session.get("cart", {})

    if request.method == "POST":
        action = request.POST.get("action")

        if slug in cart:

            if action == "increase":
                cart[slug]["quantity"] += 1

            elif action == "decrease":
                cart[slug]["quantity"] -= 1

                if cart[slug]["quantity"] <= 0:
                    del cart[slug]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart_detail")

def checkout(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0

    for slug, item in cart.items():
        video = Video.objects.get(slug=slug)
        quantity = item["quantity"]
        subtotal =  video.precio * quantity
        total += subtotal
        
        cart_items.append({
            "video": video,
            "quantity": quantity,
            "subtotal": subtotal,
        })
    
    return render(request, "core/checkout.html", {
        "cart_items": cart_items,
        "total": total,
    })

def apply_coupon(request):
    if request.method == "POST":
        code = request.POST.get("coupon_code")

        if code == "DESCUENTO10":
            request.session["discount"] = 0.10
        
        else:
            request.session["discount"] = 0
    return redirect("cart_detail")

def staff_detail(request, slug):
    member = get_object_or_404(Staff, slug=slug, activo=True)
    return render(request, "core/staff_detail.html", {
        "member": member
    })

def staff_list(request):
    members = Staff.objects.filter(activo=True)
    return render(request, "core/staff_list.html", {
    "members": members
    })

