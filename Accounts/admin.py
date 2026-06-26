from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Notification


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "email", "nom", "prenom",
        "type_utilisateur", "is_active", "is_staff", "date_joined"
    )
    list_filter = ("type_utilisateur", "is_active", "is_staff")
    search_fields = ("email", "nom", "prenom", "telephone")
    ordering = ("-date_joined",)

    # Écrase les fieldsets de BaseUserAdmin (qui utilise username)
    fieldsets = (
        ("Identifiants", {
            "fields": ("email", "password")
        }),
        ("Informations personnelles", {
            "fields": ("nom", "prenom", "telephone", "photo")
        }),
        ("Rôle & Statut", {
            "fields": ("type_utilisateur", "is_active", "is_staff", "is_superuser")
        }),
        ("Permissions", {
            "fields": ("groups", "user_permissions"),
            "classes": ("collapse",)
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "nom", "prenom",
                "type_utilisateur", "password1", "password2"
            ),
        }),
    )

    # Obligatoire : neutralise les champs de BaseUserAdmin absents de notre User
    filter_horizontal = ("groups", "user_permissions")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "titre", "destinataire", "type_notification", "lu", "date_creation"
    )
    list_filter = ("type_notification", "lu")
    search_fields = ("titre", "message", "destinataire__email")
    ordering = ("-date_creation",)
    readonly_fields = ("date_creation",)