from flask import Flask, jsonify

app = Flask(__name__)

food_items = [
      {"id": 1, "name": "Pizza", "price": 10},
      {"id": 2, "name": "Burger", "price": 5},
      {"id": 3, "name": "Pasta", "price": 8} ]

@app.route('/foods', methods = ['GET'])
def get_food_items():
      return jsonify(food_items)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000, debug=True)
