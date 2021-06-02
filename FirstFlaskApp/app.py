from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    """Show homepage"""

    html =  """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """
    return html

@app.route('/hello')
def say_hello():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the hello page</p>
        </body>
    </html>
    """
    return html

@app.route('/goodbye')
def say_bye():
    return "GOOD BYE!"

@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args['sort']
    #use term to match db data retrun term
    return f"<h1>Search results for: {term} <p>Sorting by: {sort}</p></h1>"

# @app.route("/post", method=["POST"])
# def post_demo():
#     return "YOU MADE A POST REQUEST!"

@app.route("/add-comment")
def add_comment_form():
    """Show form for adding a comment."""

    return """
      <h1>Add Comment</h1>    
      <form method="POST">
        <input type="text" placeholder="comment" name="comment"/>
        <input type="text" placeholder="username" name="username"/>
        <button>Submit</button>
      </form>
      """

@app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""
    comment = request.form["comment"]
    username = request.form["username"]
    print(request.form)
    # save that into a database!
    return f"""
    <h1>SAVED YOUR COMMENT</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment} </li>
    </ul>
    """

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing the {subreddit} subreddit</h1>"


POSTS = {
  1: "Flask is pretty cool",
  2: "Python is neat-o"
}

@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Show post with given integer id."""
    print("post_id is a ", type(post_id))
    post = POSTS.get(post_id, "Post not found")
    return f"<h1>Post #{post_id}</h1><p>{post}</p>"

