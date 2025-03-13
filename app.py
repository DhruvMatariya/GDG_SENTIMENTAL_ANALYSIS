from flask import Flask, render_template
from reddit_sentiment import reddit_data  # Import reddit_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=list(reddit_data)) # Pass reddit_data to template

if __name__ == '__main__':
    app.run(debug=True)
