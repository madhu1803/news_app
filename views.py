"""Define the views and view based operations here"""

from flask.views import MethodView
from flask import render_template, request, redirect, url_for
from forms import *
from models import *
import datetime
from app import db
import copy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)


class HomeView(MethodView):
    """Landing page for user"""

    # decorators = [login_required]
    @login_required
    def get(self):
        return render_template("home.html")


class LoginView(MethodView):
    """Login page for admin"""

    def get(self):
        form = LoginForm()
        return render_template("signup_view.html", form=form)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            admin = Admin.query.filter_by(email=form.email.data).first()
            if admin:
                if check_password_hash(admin.password, form.password.data):
                    login_user(admin)
                    return redirect(url_for("post_create_view"))

        return "<h1>invalid username/password</h1>"


class SignupView(MethodView):
    """signup page for admin"""

    def get(self):
        form = RegisterForm()
        return render_template("signup_view.html", form=form)

    def post(self):
        form = RegisterForm(data=request.form)
        data = copy.deepcopy(form.data)
        if form.validate():
            hashed_password = generate_password_hash(
                form.password.data, method="sha256"
            )
            data.pop("csrf_token")
            data["password"] = hashed_password
            admin = Admin(**data)
            db.session.add(admin)
            db.session.commit()
            return "<h1>New user has been created</h1>"
        return render_template("signup_view.html", form=form)


class PostCreateView(MethodView):
    """create post for admin"""

    def get(self):
        # on get request | render the form for post creation
        form = CreatePostForm()
        return render_template("post_create_view.html", form=form)

    def post(self):
        # on post request | get form data
        form = CreatePostForm(data=request.form)
        data = copy.deepcopy(form.data)
        # if the form is valid |store it in post table in db and redirect to posts view
        if form.validate():
            # del csrf token
            data.pop("csrf_token")
            post = Post(**data)
            # add the post object
            db.session.add(post)
            # commit the changes
            db.session.commit()
            return redirect("/admin/post/all")
        # form not valid | render the form in create view
        return render_template("post_create_view.html", form=form)


class PostListView(MethodView):
    """view post for admin"""

    def get(self):
        # on get request | fetch all posts from post table in db and render the posts to template
        posts = Post.query.all()
        return render_template("post_list_view.html", posts=posts)


class PostEditView(MethodView):
    """edit/update post for admin"""

    def get(self, post_id):
        # on get request  |  get the post details by id  add to form data and render the form
        post = Post.query.filter_by(id=post_id).one()
        # convert post sql object to python dict and pass it to form
        form = CreatePostForm(data=post.__dict__)
        return render_template("post_edit_view.html", form=form)

    def post(self, post_id):
        # on post request | get the form data and update the post
        post = Post.query.filter_by(id=post_id).one()
        form = CreatePostForm(data=request.form)
        data = copy.deepcopy(form.data)
        # if form validate | update the details of post
        if form.validate():
            data.pop("csrf_token")
            post.title = data["title"]
            post.subtitle = data["subtitle"]
            post.content = data["content"]
            # commit update to the object
            db.session.commit()
            return redirect("/admin/post/all")


class PostDeleteView(MethodView):
    """delete post for admin"""

    def get(self, post_id):
        # on get request | fetch the post  by id and delete it
        post = Post.query.filter_by(id=post_id).one()
        db.session.delete(post)
        db.session.commit()
        return redirect("/admin/post/all")


class PostDetailView(MethodView):
    """delete post for admin"""

    def get(self, post_id):
        # on get request | fetch the post by id  and display it
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
