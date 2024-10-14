from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import EducationProduct, PricingPost, StaffPost, NewsPost, GalleryPost, ContactMessage
from django.urls import path,reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group

# Register your models with custom admin configurations

@admin.register(EducationProduct)
class EducationProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_date', 'image', 'price')
    list_filter = ('title', 'created_date')

@admin.register(PricingPost)
class PricingPostAdmin(admin.ModelAdmin):
    list_display = ('payment_plan', 'amount', 'created_date', 'description')
    list_filter = ('payment_plan', 'created_date')

@admin.register(StaffPost)
class StaffPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'subject', 'about')
    list_filter = ('name', 'subject', 'created_date')

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'image', 'created_date', 'article')
    list_filter = ('headline', 'created_date')

@admin.register(GalleryPost)
class GalleryPostAdmin(admin.ModelAdmin):
    list_display = ('image', 'created_date')
    list_filter = ('created_date',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email')
    search_fields = ('first_name', 'email', 'message')
    list_filter = ('email',)
    list_per_page = 20

# Custom admin site class
class CustomAdminSite(admin.AdminSite):
    site_header = "My Application Admin"
    site_title = "My Application Admin Portal"
    index_title = "Welcome to My Application Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('home/', self.admin_view(self.home_view), name='home'),  # Custom URL
            path('logout/', self.admin_view(self.logout_view), name='logout'),  # Custom URL
        ]
        return custom_urls + urls

    def home_view(self, request):
        return redirect(reverse('index'))  # Redirect to the named URL for the home page
    def logout_view(self, request):
        return redirect(reverse ('logout'))

# Create an instance of the custom admin site
custom_admin_site = CustomAdminSite()

# Register your models with the custom admin site
# custom_admin_site.register(YourModel)

# Set the custom admin site instance as the default one
admin.site = custom_admin_site
# Register built-in models with the custom admin site
custom_admin_site.register(User)
custom_admin_site.register(Group)

# Register your custom models with the custom admin site
custom_admin_site.register(EducationProduct, EducationProductsAdmin)
custom_admin_site.register(PricingPost, PricingPostAdmin)
custom_admin_site.register(StaffPost, StaffPostAdmin)
custom_admin_site.register(NewsPost, NewsPostAdmin)
custom_admin_site.register(GalleryPost, GalleryPostAdmin)
custom_admin_site.register(ContactMessage, ContactMessageAdmin)

# Override the default admin site instance with the custom one
admin.site = custom_admin_site
