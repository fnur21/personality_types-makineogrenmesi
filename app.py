from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Model ve dönüştürücüler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tahmin", methods=["POST"])
def tahmin():
    try:
        data = request.get_json()
        features = [int(data[f"q{i}"]) for i in range(1, 8)]
        scaled = scaler.transform([features])
        prediction = model.predict(scaled)[0]
        label = label_encoder.inverse_transform([prediction])[0]
        return jsonify({"tahmin": label})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
