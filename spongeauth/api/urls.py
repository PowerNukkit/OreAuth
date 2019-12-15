from django.conf.urls import url

import api.views

app_name = "api"

urlpatterns = [
    url(r"^users$", api.views.list_users, name="users-list"),
    url(r"^users/(?P<username>[^/]+)$", api.views.user_detail, name="users-detail"),
    url(
        r"^users/(?P<for_username>[^/]+)/change-avatar-token/$",
        api.views.change_other_avatar_key,
        name="change-avatar-token",
    ),
]
