from .models import Staff

def staff_members(request):
    return {
        "navbar_staff":
Staff.objects.filter(activo=True)        
    }