from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)
app.app_context().push()

class BlogIt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True, unique=False)
    author = db.Column(db.String(100), nullable=False, unique=False)
    content = db.Column(db.Text, nullable=False)
    posted_on = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow())
    def __repr__(self):
        return self.title
db.create_all()
db.session.commit()

@app.route('/')
def home():
    return render_template('html/index.html')

@app.route('/about')
def about():
    return render_template('html/about.html')

@app.route('/team')
def team():
    return render_template('html/team.html')


@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_title = request.form['input']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogIt(title=post_title,
                        content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('html/index.html')

@app.route('/posts',  methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['input']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogIt(title=post_title,
                        content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogIt.query.order_by(BlogIt.posted_on).all()
        return render_template('html/display_post.html', posts=all_posts)
    
@app.route('/readblog', methods=['GET', 'POST'])
def read_blog():
    query_string = request.query_string.decode("utf-8") 
    title_clicked_with_modulo = query_string.replace("query=","")
    title_clicked = title_clicked_with_modulo.replace("%20"," ")
    print(title_clicked)
    # blogit_title = BlogIt.query.filter(BlogIt.id < index_clicked).all()
    blogit_details_clicked = BlogIt.query.filter_by(title = title_clicked).first()

    return render_template('html/display_content.html', details = blogit_details_clicked)
# @app.route('/posts')
# def posts():
#     return render_template('html/display_post.html')
if __name__ == '__main__':
    app.run(port=8000, debug=True)