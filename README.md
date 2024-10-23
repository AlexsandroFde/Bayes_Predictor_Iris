
# Previsão Naive Bayes de Espécie de Íris

Este projeto implementa um sistema de previsão de espécies de íris com base nas características da flor (comprimento e largura da sépala e pétala) utilizando o algoritmo **Naive Bayes**. A aplicação possui duas formas de entrada: um formulário para inserção manual dos dados ou a possibilidade de upload de um arquivo `.txt` contendo os dados.

## Como Usar

1. Execute o servidor Flask:

   ```bash
   flask run
   ```

2. Acesse a aplicação no navegador através de:

   ```
   http://127.0.0.1:5000
   ```

### Formulário de Entrada

1. Na aba **Formulário**, insira os valores das características da flor:
   - Comprimento da Sépala (cm)
   - Largura da Sépala (cm)
   - Comprimento da Pétala (cm)
   - Largura da Pétala (cm)
2. Clique no botão **Prever Espécie** para obter o resultado.

### Upload de Arquivo

1. Na aba **Upload de Arquivo**, selecione um arquivo `.txt` com os valores das características da flor no formato:
   ```
   sepal_length,sepal_width,petal_length,petal_width
   ```
2. Clique em **Enviar Arquivo** para fazer o upload e obter o resultado.

### Exemplo de Arquivo `.txt`

```txt
5.1,3.5,1.4,0.2
6.2,3.4,5.4,2.3
```

## Detalhes Técnicos

- **Algoritmo de Classificação**: O modelo utiliza **Naive Bayes**, um classificador probabilístico baseado no Teorema de Bayes, com suposições de independência entre os atributos. O modelo foi treinado utilizando o **conjunto de dados Íris**, amplamente utilizado em aprendizado de máquina.
  
- **Frontend**: A interface do usuário é desenvolvida utilizando HTML, CSS e JavaScript, oferecendo um formulário para inserção manual de dados e uma opção de upload de arquivos.

- **Backend**: A aplicação utiliza **Flask** para lidar com as requisições do usuário. O modelo de previsão é treinado e carregado no backend usando a biblioteca `scikit-learn`.

## Contribuição

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
