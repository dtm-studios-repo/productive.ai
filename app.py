from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve the stock.html page
@app.route('/')
def index():
    return render_template('stock.html')

# Endpoint to handle form submission and return stock recommendations
@app.route('/recommend-stocks', methods=['POST'])
def recommend_stocks():
    data = request.json
    days = int(data['days'])
    returns = float(data['returns'])

    # Placeholder AI logic for stock recommendations
    # In a real scenario, you would replace this with your actual model logic
    recommended_stocks = []
    
    if days <= 30 and returns >= 10:
        recommended_stocks = ["AAPL", "GOOGL", "MSFT"]
    elif days <= 60 and returns >= 5:
        recommended_stocks = ["AMZN", "TSLA", "FB"]
    else:
        recommended_stocks = ["No strong matches found"]

    return jsonify({"stocks": recommended_stocks})

if __name__ == '__main__':
    app.run(debug=True)
