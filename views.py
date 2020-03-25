"""Define the views and view based operations here"""

from flask.views import MethodView


class HomeRoute(MethodView):
    """Landing page for user"""

    def get(self):
        return "hello world"
