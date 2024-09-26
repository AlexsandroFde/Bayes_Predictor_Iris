document.getElementById('form-tab').addEventListener('click', function() {
    document.getElementById('form-section').classList.add('active');
    document.getElementById('file-section').classList.remove('active');
    this.classList.add('active');
    document.getElementById('file-tab').classList.remove('active');
});

document.getElementById('file-tab').addEventListener('click', function() {
    document.getElementById('file-section').classList.add('active');
    document.getElementById('form-section').classList.remove('active');
    this.classList.add('active');
    document.getElementById('form-tab').classList.remove('active');
});

document.getElementById('prediction-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const data = {
        sepal_length: parseFloat(document.getElementById('sepal_length').value),
        sepal_width: parseFloat(document.getElementById('sepal_width').value),
        petal_length: parseFloat(document.getElementById('petal_length').value),
        petal_width: parseFloat(document.getElementById('petal_width').value)
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById('result').textContent = `Previsão: ${result.prediction}`;
    } catch (error) {
        console.error('Erro na previsão:', error);
        document.getElementById('result').textContent = 'Erro ao obter a previsão. Tente novamente.';
    }
});

document.getElementById('file-upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    try {
        const response = await fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.blob();
        const url = window.URL.createObjectURL(result);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'result.txt';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    } catch (error) {
        console.error('Erro no upload do arquivo:', error);
        document.getElementById('file-result').textContent = 'Erro ao processar o arquivo. Tente novamente.';
    }
});
