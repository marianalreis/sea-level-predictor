import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
   

    # 1) Ler dados do arquivo CSV
    df = pd.read_csv("epa-sea-level.csv")

    # 2) Criar gráfico de dispersão (pontos reais do nível do mar)
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3) Criar primeira linha de melhor ajuste (usando todos os dados até 2050)
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    anos_todos = pd.Series(range(1880, 2051))
    previsao_todos = intercept + slope * anos_todos
    plt.plot(anos_todos, previsao_todos, color="red")

    # 4) Criar segunda linha de melhor ajuste (usando apenas dados a partir de 2000 até 2050)
    df_2000 = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    anos_2000 = pd.Series(range(2000, 2051))
    previsao_2000 = intercept2 + slope2 * anos_2000
    plt.plot(anos_2000, previsao_2000, color="green")

    # 5) Adicionar rótulos dos eixos e título do gráfico
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # 6) Salvar imagem e retornar eixo para os testes automáticos (NÃO MODIFICAR)
    plt.savefig("sea_level_plot.png")
    return plt.gca()