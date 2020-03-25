"""Define the views and view based operations here"""

from flask.views import MethodView
from flask import render_template


class HomeView(MethodView):
    """Landing page for user"""

    def get(self):
        return render_template("home.html")


class LoginView(MethodView):
    """Login page for admin"""

    def get(self):
        return render_template("login_view.html")


class SignupView(MethodView):
    """signup page for admin"""

    def get(self):
        return render_template("signup_view.html")


class PostCreateView(MethodView):
    """create post for admin"""

    def get(self):
        return render_template("post_create_view.html")


class PostListView(MethodView):
    """view post for admin"""

    def get(self):
        return render_template("post_list_view.html")


class PostEditView(MethodView):
    """edit post for admin"""

    def get(self):
        return render_template("post_edit_view.html")


class PostDeleteView(MethodView):
    """delete post for admin"""

    def get(self):
        return render_template("post_delete_view.html")


class PostDetailView(MethodView):
    """delete post for admin"""

    def get(self):
        return render_template("post_detail_view.html")


class UserPostListView(MethodView):
    """User Post List View"""

    def get(self):
        return render_template("user_post_view.html")


class UserPostDetailView(MethodView):
    """User Post Detail View"""

    def get(self):
        return render_template("user_post_detail_view.html")
