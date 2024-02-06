from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sites.models import Site
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from apps.blog.sitemaps import BlogSitemap
from apps.mainPage.sitemaps import MainPageViewSitemap


def redirect_to_domain(request):
    current_site = Site.objects.get_current()
    redirect_url = f"https://{current_site.domain}"
    return RedirectView.as_view(url=redirect_url)(request)

sitemaps = {
    'index': MainPageViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.mainPage.urls')),
    path('blog/', include('apps.blog.urls')),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    re_path(r'^robots\.txt', include('robots.urls')),

    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('', redirect_to_domain,),
]

# Manage static files and url through nginx in production
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls"))
    ]
