import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
   

    # 1) Ler dados do arquivo CSV
     # Aqui eu carrego o arquivo com os dados do nível do mar
    df = pd.read_csv("epa-sea-level.csv")

    # 2) Criar gráfico de dispersão (pontos reais do nível do mar)
    # Eu ploto cada ponto real do conjunto de dados (ano x nível do mar), isso me permite visualizar como os valores se comportam ao longo do tempo e serve como base para comparar com as linhas de tendência que vou adicionar depois.
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3) Criar primeira linha de melhor ajuste (usando todos os dados até 2050)
    # Eu calculo a linha de melhor ajuste considerando toda a série histórica, essa linha mostra a tendência de longo prazo e me ajuda a prever o nível do mar até 2050, assumindo que o padrão histórico se mantenha.
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    anos_todos = pd.Series(range(1880, 2051))
    previsao_todos = intercept + slope * anos_todos
    plt.plot(anos_todos, previsao_todos, color="red")

    # 4) Criar segunda linha de melhor ajuste (usando apenas dados a partir de 2000 até 2050)
    # Agora eu refaço o cálculo, mas usando apenas os dados mais recentes (de 2000 em diante), o objetivo é verificar se a tendência atual está mais acentuada que a histórica, o que pode indicar aceleração no aumento do nível do mar.
    df_2000 = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    anos_2000 = pd.Series(range(2000, 2051))
    previsao_2000 = intercept2 + slope2 * anos_2000
    plt.plot(anos_2000, previsao_2000, color="green")

    # 5) Adicionar rótulos dos eixos e título do gráfico
    # Eu adiciono título e rótulos para que qualquer pessoa consiga entender o gráfico, o eixo X mostra os anos, eixo Y mostra o nível do mar em polegadas, e o título resume a mensagem principal.
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # 6) Salvar imagem e retornar eixo para os testes automáticos (NÃO MODIFICAR)
    # Por fim, esse código salva a figura em um arquivo PNG, que pode ser usado em relatórios ou apresentações, e retorno o eixo do gráfico.
    plt.savefig("sea_level_plot.png")
    return plt.gca()