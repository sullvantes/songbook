# songs/views.py
from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, FormView, ListView, TemplateView, View

from songbook.mixins import StaffRequiredMixin

from club.models import Club
from player.models import Player

from .emails import send_activation_email
from .forms import ResendActivationForm, SongSuggestionForm, UserRegistrationForm
from .models import Song

User = get_user_model()


class UserLoginView(LoginView):
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("register_form", UserRegistrationForm())
        return context


class RegisterView(FormView):
    template_name = "registration/login.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("activation_sent")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return redirect("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AuthenticationForm()
        context["register_form"] = self.get_form()
        return context

    def form_valid(self, form):
        user = form.save()
        send_activation_email(self.request, user)
        self.request.session["pending_activation_email"] = user.email
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        context["register_form"] = form
        return self.render_to_response(context)


class ActivationSentView(TemplateView):
    template_name = "registration/activation_sent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["email"] = self.request.session.pop("pending_activation_email", "")
        return context


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        user = self._get_user(uidb64)

        if user is not None and default_token_generator.check_token(user, token):
            if user.is_active:
                messages.info(request, "Your account is already active. You can log in.")
            else:
                user.is_active = True
                user.save(update_fields=["is_active"])
                messages.success(request, "Your email is confirmed. You can now log in.")
            return redirect("login")

        messages.error(request, "The confirmation link is invalid or has expired.")
        return redirect("resend_activation")

    def _get_user(self, uidb64):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            return User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return None


class ResendActivationView(FormView):
    template_name = "registration/resend_activation.html"
    form_class = ResendActivationForm
    success_url = reverse_lazy("activation_sent")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = User.objects.filter(email__iexact=email, is_active=False).first()
        if user is not None:
            send_activation_email(self.request, user)
            self.request.session["pending_activation_email"] = email
        else:
            self.request.session.pop("pending_activation_email", None)
        return super().form_valid(form)


class SongListView(ListView):
    model = Song
    paginate_by = 20

    def get_queryset(self):
        queryset = (
            Song.objects.filter(accepted=True)
            .prefetch_related("clubs", "tags")
            .select_related("player")
            .order_by("title")
        )

        search_query = self.request.GET.get("q", "").strip()
        self.search_query = search_query or None
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(lyrics__icontains=search_query)
                | Q(description__icontains=search_query)
                | Q(player__name__icontains=search_query)
                | Q(clubs__name__icontains=search_query)
                | Q(tags__name__icontains=search_query)
            )

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.search_query or ""
        context["pagination_query"] = (
            f"&{urlencode({'q': self.search_query})}" if self.search_query else ""
        )
        return context


class SongDeleteView(StaffRequiredMixin, View):
    def post(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        title = song.title
        song.delete()
        messages.success(request, f'Deleted song "{title}".')
        return redirect("songs:list")


class SongSuggestionCreateView(LoginRequiredMixin, CreateView):
    form_class = SongSuggestionForm
    template_name = "song/suggest_song.html"
    success_url = reverse_lazy("songs:list")

    def get_initial(self):
        initial = super().get_initial()
        club_slug = self.request.GET.get("club")
        if club_slug:
            club = Club.objects.filter(slug=club_slug).first()
            if club:
                initial["club"] = club.pk
        player_slug = self.request.GET.get("player")
        if player_slug:
            player = Player.objects.filter(slug=player_slug).first()
            if player:
                initial["player"] = player.pk
        return initial

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)