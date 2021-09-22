from flask.helpers import url_for
from werkzeug.utils import redirect
from flask import render_template, request, abort
from flask_login import login_required, current_user
from app.models import Comment, Pitch, User
from app.main.forms import CommentForm, PitchForm, UpdateProfile
from . import main
from .. import db, photos

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


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.get_pitches(current_user.id)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user, pitches=pitches)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/pitch/<int:id>/vote/<vote>', methods=['GET','POST'])
@login_required
def vote(id, vote):
    pitch = Pitch.get_pitch(id)
    if vote == 'upvote':
        pitch.upvotes = pitch.upvotes + 1
    else:
        pitch.downvotes = pitch.downvotes + 1
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route("/filter/<category>")
def filter_pitches(category):
    pitches = Pitch.query.filter_by(category = category).all()
    return render_template("index.html", pitches=pitches)
