# Análise da Disseminação do COVID-19 no Brasil

Este repositório contém um projeto que investiga os dados da disseminação do COVID-19 no Brasil desde o início da pandemia em fevereiro de 2020. O objetivo é analisar os padrões de propagação da doença, focando nos números de infectados, recuperados e óbitos, e utilizar técnicas de Machine Learning para prever números futuros e identificar o ponto de virada da curva de infecção em diferentes cenários.

## Conteúdo

- **Coleta de Dados**: Importação de dados históricos sobre casos de COVID-19.
- **Análise Exploratória**: Visualização de tendências de infecção e mortalidade.
- **Modelagem Preditiva**: Implementação de modelos de Machine Learning e séries temporais.
- **Visualização de Resultados**: Gráficos que mostram as previsões e análise dos dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Pandas**: Para manipulação e análise de dados.
- **NumPy**: Para operações numéricas.
- **Matplotlib**: Para visualização de dados.
- **Seaborn**: Para visualizações estatísticas.
- **Scikit-learn**: Para algoritmos de Machine Learning.
- **Statsmodels**: Para análise de séries temporais.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
```

## Uso

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/repositorio.git
   cd repositorio
   ```

2. Substitua o URL do arquivo CSV no código pelo link real ou caminho do arquivo com os dados de COVID-19.

3. Execute o script principal:
   ```bash
   python analise_covid.py
   ```

## Exemplo de Dados

O projeto pode ser utilizado com dados em formato CSV. Um exemplo de estrutura de dados poderia ser:

```csv
data,casos_confirmados,obitos
2020-02-01,0,0
2020-03-01,0,0
2020-04-01,10,0
2020-05-01,200,5
...
```

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para mais informações, entre em contato:

- **Nome**: Felipe Carrasco
- **E-mail**: sfelipe.morente1803@gmail.com

