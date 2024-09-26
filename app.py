from flask import Flask, request, jsonify, render_template, send_file
import joblib
import pandas as pd

app = Flask(__name__)

# Carregar o modelo salvo
model = joblib.load('naive_bayes_model.pkl')

# Rota principal (GET)
@app.route('/')
def home():
    return render_template('index.html')

# Rota para realizar previsão (POST)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
    prediction = model.predict([features])[0]
    species = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
    predicted_species = species[prediction]
    return jsonify({'prediction': predicted_species})

# Rota para upload de arquivo (POST)
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file or not file.filename.endswith('.txt'):
        return 'Invalid file format', 400

    # Ler o arquivo .txt
    data = pd.read_csv(file, delim_whitespace=True, header=None)

    results = []
    for index, row in data.iterrows():
        features = row.tolist()
        prediction = model.predict([features])[0]
        species = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
        predicted_species = species[prediction]
        results.append(f"{' '.join(map(str, features))} {predicted_species}")

    # Salvar resultados em um novo arquivo .txt
    result_filename = 'result.txt'
    with open(result_filename, 'w') as f:
        for result in results:
            f.write(result + '\n')

    return send_file(result_filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
