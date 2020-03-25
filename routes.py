"""Define the Views here"""

from app import app
from views import *

# mapping for Views and views
app.add_url_rule("/", view_func=HomeView.as_view("home"))
app.add_url_rule("/admin/login", view_func=LoginView.as_view("admin_login"))
app.add_url_rule("/admin/signup", view_func=SignupView.as_view("admin_signup"))
app.add_url_rule(
    "/admin/post/new", view_func=PostCreateView.as_view("post_create_view")
)
app.add_url_rule("/admin/post/all", view_func=PostListView.as_view("post_list_view"))
app.add_url_rule(
    "/admin/post/<int:post_id>/view",
    view_func=PostDetailView.as_view("post_detail_view"),
)
app.add_url_rule(
    "/admin/post/<int:post_id>/edit", view_func=PostEditView.as_view("post_edit_view")
)
app.add_url_rule(
    "/admin/post/<int:post_id>/delete",
    view_func=PostDeleteView.as_view("post_delete_view"),
)
app.add_url_rule("/post/all", view_func=UserPostListView.as_view("user_post_List_view"))
app.add_url_rule(
    "/post/id/view", view_func=UserPostDetailView.as_view("user_post_detail_view")
)
