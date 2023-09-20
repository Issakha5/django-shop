from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from ..models.product import Product
from ..models.category import Category
from ..models.review import Review


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get("category", "")

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get("query", "")

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        "categories": categories,
        "products": products,
        "active_category": active_category,
    }

    return render(request, "product/shop.html", context)


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == "POST":
        rating = request.POST.get("rating", 3)
        content = request.POST.get("content", "")

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user,
                )

            return redirect("product", slug=slug)

    return render(request, "product/product.html", {"product": product})
