"""
URL configuration for songbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from club.views import ClubListView
from songbook.views import health_check
from song.views import (
    ActivateAccountView,
    ActivationSentView,
    RegisterView,
    ResendActivationView,
    UserLoginView,
)

urlpatterns = [
    path("health/", health_check, name="health"),
    path("admin/", admin.site.urls),
    path("accounts/login/", UserLoginView.as_view(), name="login"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
    path(
        "accounts/activate/<uidb64>/<token>/",
        ActivateAccountView.as_view(),
        name="activate",
    ),
    path("accounts/activation-sent/", ActivationSentView.as_view(), name="activation_sent"),
    path("accounts/resend-activation/", ResendActivationView.as_view(), name="resend_activation"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("", ClubListView.as_view(), name="home"),
    path("songs/", include("song.urls", namespace="songs")),
    path("players/", include("player.urls", namespace="players")),
    path("clubs/", include("club.urls", namespace="clubs")),
    path("matches/", include("chant.urls", namespace="chants")),
]

if settings.DEBUG or getattr(settings, "SERVE_MEDIA", False):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
