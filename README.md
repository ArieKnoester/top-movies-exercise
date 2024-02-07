# top-movies-exercise

## Description:
Another Python course exercise building on concepts covered in previous exercises. This a 'Top 10 Movies'
website which allows the user to add, delete, and update movie 'ratings' and 'reviews'. 'styles.css' was
provided by the course as was some starting code (See Initial commit). Data for movies come from
The Movie Database's api (https://themoviedb.com) 

Key modules:
- Flask (and Jinja templating)
- Bootstrap_Flask
- Requests
- WTForms
- Flask_WTF
- flask_sqlalchemy
- SQLAlchemy

### Notes:
- This is my solution based on the requirements given. At no point did I look at the instructor's code
to complete this exercise.
- Movies are sorted by **ranking** in descending order.
- When a user edits their **raiting** of a movie, **ranking** is updated automatically.
- When a user adds a movie to the list, they are prompted to add a rating and a short review
before it is committed to the database. Rating and review fields are required inputs.