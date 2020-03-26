"""Define the views and view based operations here"""

from flask.views import MethodView
from flask import render_template, request, redirect
from forms import *
from models import *
import datetime
from app import db
import copy


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
        form = CreatePostForm()
        return render_template("post_create_view.html", form=form)

    def post(self):
        form = CreatePostForm(data=request.form)
        data = copy.deepcopy(form.data)
        if form.validate():
            data.pop("csrf_token")
            post = Post(**data)
            db.session.add(post)
            db.session.commit()
            return redirect("/admin/post/new")
        return render_template("post_create_view.html", form=form)


class PostListView(MethodView):
    """view post for admin"""

    def get(self):
        posts = Post.query.all()
        print(posts)
        return render_template("post_list_view.html", posts=posts)


class PostEditView(MethodView):
    """edit post for admin"""

    def get(self, post_id):
        post = Post.query.filter_by(id=post_id).one()
        form = CreatePostForm(data=post.__dict__)
        return render_template("post_edit_view.html", form=form)

    def post(self, post_id):
        post = Post.query.filter_by(id=post_id).one()
        form = CreatePostForm(data=request.form)
        data = copy.deepcopy(form.data)
        if form.validate():
            data.pop("csrf_token")
            post.title = data["title"]
            post.subtitle = data["subtitle"]
            post.content = data["content"]
            db.session.commit()
            return redirect("/admin/post/all")


class PostDeleteView(MethodView):
    """delete post for admin"""

    def get(self, post_id):
        post = Post.query.filter_by(id=post_id).one()
        db.session.delete(post)
        db.session.commit()

        return redirect("/admin/post/all")


class PostDetailView(MethodView):
    """delete post for admin"""

    def get(self, post_id):
        post = Post.query.filter_by(id=post_id).one()

        return render_template("post_detail_view.html", post=post)


class UserPostListView(MethodView):
    """User Post List View"""

    def get(self):
        return render_template("user_post_view.html")


class UserPostDetailView(MethodView):
    """User Post Detail View"""

    def get(self):
        return render_template("user_post_detail_view.html")
