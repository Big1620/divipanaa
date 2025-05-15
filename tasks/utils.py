from .models import Usuario

def get_usuario_from_request(request):
    """Devuelve el modelo Usuario vinculado al request.user."""
    if not request.user.is_authenticated:
        return None
    try:
        return Usuario.objects.get(user=request.user)
    except Usuario.DoesNotExist:
        return None
