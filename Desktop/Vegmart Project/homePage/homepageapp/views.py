from django.shortcuts import render
from .models import Vegetable

def home(request):
    category = request.GET.get('category', None)  # Get the selected category from query parameters

    # Define allowed categories
    allowed_categories = ['domestic', 'commercial']
    
    # Validate category
    if category not in allowed_categories and category is not None:
        category = None

    # Query based on category
    if category:
        vegetables = Vegetable.objects.filter(category=category)
    else:
        vegetables = Vegetable.objects.all()
    
    # Render the response
    return render(request, 'home.html', {'vegetables': vegetables, 'selected_category': category})
