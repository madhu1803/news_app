"""Define the views and view based operations here"""

from flask.views import MethodView


class HomeView(MethodView):
    """Landing page for user"""

    def get(self):
        return "hello world"


class LoginView(MethodView):
    """Login page for admin"""

    def get(self):
        return "admin login"


class SignupView(MethodView):
    """signup page for admin"""

    def get(self):
        return "admin signup"


class PostCreateView(MethodView):
    """create post for admin"""

    def get(self):
        return "admin post create"


class PostListView(MethodView):
    """view post for admin"""

    def get(self):
        return "admin post view"


class PostEditView(MethodView):
    """edit post for admin"""

    def get(self):
        return "admin post edit"


class PostDeleteView(MethodView):
    """delete post for admin"""

    def get(self):
        return "admin post delete"


class PostDetailView(MethodView):
    """delete post for admin"""

    def get(self):
        return "admin post view details"


class UserPostListView(MethodView):
    """User Post List View"""

    def get(self):
        return "User Post List View"


class UserPostDetailView(MethodView):
    """User Post Detail View"""

    def get(self):
        return "User Post Detail View"
