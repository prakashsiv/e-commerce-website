from flask import Flask, render_template, jsonify

app = Flask(__name__)
##print(__name__)

ITEMS = [{
  "product_id": 1,
  "product_name": "Kapasa Sowla",
  "product_type": "Saree",
  "product_material": "100% Cotton",
  "product_price": "Rs. 600"
}, {
  "product_id": 2,
  "product_name": "Medhuv Pasu Sowla",
  "product_type": "Saree",
  "product_material": "Soft Silk",
  "product_price": "Rs. 1200"
}, {
  "product_id": 3,
  "product_name": "Pasu Sowla",
  "product_type": "Saree",
  "product_material": "Pure Silk",
  "product_price": "Rs. 5000"
}, {
  "product_id": 4,
  "product_name": "Kapasa Dhovat",
  "product_type": "Veshti",
  "product_material": "100% Cotton"
}]


@app.route("/")
def hello_ishsi():
  return render_template('home.html', items=ITEMS, company_name="IshSi")


@app.route("/buy")
def hello_buy():
  return jsonify(ITEMS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
