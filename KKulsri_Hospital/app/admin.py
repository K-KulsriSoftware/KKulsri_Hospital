from django.contrib import admin
from app.models import Profile
from django.contrib.auth.models import User

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profiles'

# # Define a new User admin

# class UserAdmin(ProfileInline):
#     inlines = (ProfileInline, )


# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
