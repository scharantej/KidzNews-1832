
from flask import Flask, render_template, request

app = Flask(__name__)

news_articles = [
    {
        "id": 1,
        "title": "SpaceX Launches Falcon 9 Rocket",
        "summary": "SpaceX successfully launched its Falcon 9 rocket from Cape Canaveral, Florida, on Tuesday. The rocket carried a payload of 60 Starlink satellites into orbit.",
        "image": "spacex-launch.jpg",
        "category": "Science"
    },
    {
        "id": 2,
        "title": "Biden Signs Climate Change Executive Order",
        "summary": "President Biden signed an executive order on Wednesday aimed at addressing climate change. The order sets ambitious goals for reducing greenhouse gas emissions and investing in clean energy.",
        "image": "biden-climate.jpg",
        "category": "Politics"
    },
    {
        "id": 3,
        "title": "New Study Finds Link Between Sleep and Heart Health",
        "summary": "A new study published in the journal JAMA Internal Medicine has found a link between sleep duration and heart health. The study found that people who sleep less than 6 hours per night have a higher risk of developing heart disease.",
        "image": "sleep-heart.jpg",
        "category": "Health"
    }
]

categories = ["Science", "Politics", "Health"]

@app.route('/')
def index():
    return render_template('index.html', articles=news_articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((article for article in news_articles if article["id"] == article_id), None)
    if article is None:
        return render_template('error.html'), 404
    return render_template('article.html', article=article)

@app.route('/category/<string:category_name>')
def category(category_name):
    articles = [article for article in news_articles if article["category"] == category_name]
    return render_template('index.html', articles=articles)

@app.route('/search')
def search():
    query = request.args.get('q')
    articles = [article for article in news_articles if query in article["title"]]
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
