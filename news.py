from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve the news.html page
@app.route('/')
def index():
    return render_template('news.html')

# Endpoint to summarize news based on the subtopic
@app.route('/summarize-news', methods=['POST'])
def summarize_news():
    data = request.json
    subtopic = data['subtopic']
    
    # Placeholder AI logic for news summarization
    summaries = {
        'Technology': 'Latest technology news summary: AI advancements, tech mergers, and new smartphone releases.',
        'Finance': 'Finance news summary: Stock market fluctuations, cryptocurrency trends, and financial regulations updates.',
        'Health': 'Health news summary: COVID-19 updates, new vaccine developments, and mental health awareness.',
        'Sports': 'Sports news summary: Latest football match results, cricket tournaments, and Olympic updates.',
        'Politics': 'Politics news summary: Election results, policy debates, and international relations highlights.'
    }

    summary = summaries.get(subtopic, 'No news available for this subtopic.')

    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
