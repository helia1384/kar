def user_profile(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    return {'user_profile': profile}

