from flask.helpers import url_for
from werkzeug.utils import redirect
from flask import render_template, request
from flask_login import login_required, current_user
from app.models import Comment, Pitch
from app.main.forms import CommentForm, PitchForm
from . import main
from .. import db

# Views
@main.route("/")
def index():
    pitches = Pitch.get_all_pitches()
    return render_template("index.html", pitches=pitches)


@main.route("/my_pitches")
@login_required
def my_pitches():
    pitches = Pitch.get_pitches(current_user.id)
    return render_template("my_pitches.html", pitches=pitches)


@main.route("/pitch", methods=["GET", "POST"])
@login_required
def add_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(
            title=form.title.data,
            category=form.category.data,
            pitch=form.pitch.data,
            user=current_user,
        )
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for("main.my_pitches"))

    title = "Add Pitch"
    return render_template("new_pitch.html", pitch_form=form, title=title)

@main.route("/pitch/comments/<int:id>", methods=['GET','POST'])
@login_required
def comments(id):
    form = CommentForm()
    pitch = Pitch.get_pitch(id)
    if request.method == 'GET':
        comments = pitch.comments
        return render_template("comments.html", comments=comments, user=current_user, comment_form=form)
    else:
        if form.validate_on_submit():
            comment = Comment(comment=form.comment.data, pitch=pitch, user_id=current_user.id)
            db.session.add(comment)
            db.session.commit()
            # refetch comments
            comments = pitch.comments
            # clear form since we are rendering same view
            form.comment.data = ""
            return render_template("comments.html", comments=comments, user=current_user, comment_form=form)