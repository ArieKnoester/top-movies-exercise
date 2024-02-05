from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from models.movie import Movie, db
from forms.forms import AddMovieForm, EditMovieForm
import requests
from dotenv import load_dotenv
import os


load_dotenv(".env")
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///movies.db'
Bootstrap5(app)
db.init_app(app)

with app.app_context():
    db.create_all()

# Add a few example records to the db to start.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
#                 "extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with "
#                 "the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family ("
#                 "Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each "
#                 "other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.ranking.desc())).scalars()
    return render_template("index.html", movies=all_movies)


@app.route("/add")
def add():
    add_form = AddMovieForm()
    return render_template("add.html", form=add_form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = EditMovieForm()

    if edit_form.validate_on_submit():
        with app.app_context():
            movie_id = request.args.get("movie_id")
            movie_to_edit = db.get_or_404(Movie, movie_id)
            movie_to_edit.rating = request.form["rating"]
            movie_to_edit.review = request.form["review"]
            db.session.commit()
            return redirect(url_for('home'))

    return render_template("edit.html", form=edit_form)


@app.route("/delete")
def delete():
    with app.app_context():
        movie_id = request.args.get("movie_id")
        movie_to_delete = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
