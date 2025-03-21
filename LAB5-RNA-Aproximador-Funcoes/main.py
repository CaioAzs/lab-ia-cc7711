import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MaxAbsScaler
import time

def carregar_arquivo(arquivo_path):
    print(f'Carregando arquivo: {arquivo_path}')
    arquivo = np.load(arquivo_path)
    x = arquivo[0]
    scaler = MaxAbsScaler().fit(arquivo[1])
    y = np.ravel(scaler.transform(arquivo[1]))
    return x, y

def simular_arquiteturas(x, y, iteracoes=400, num_simulacoes=10):
    arquiteturas = [
        (10,), 
        (15, 5),
        (20, 10, 5) 
    ]
    
    resultados = {}
    
    for arquitetura in arquiteturas:
        erros = []
        for _ in range(num_simulacoes):
            regr = MLPRegressor(hidden_layer_sizes=arquitetura,
                                max_iter=iteracoes,
                                activation='tanh',
                                solver='adam',
                                learning_rate='adaptive',
                                n_iter_no_change=iteracoes,
                                verbose=False)
            start_time = time.time()
            regr.fit(x, y)
            y_est = regr.predict(x)
            erro = np.mean((y - y_est) ** 2)
            erros.append(erro)
        
        media_erro = np.mean(erros)
        desvio_erro = np.std(erros)
        resultados[arquitetura] = (media_erro, desvio_erro)
        
    return resultados

def plotar_resultados(x, y, y_est, arquitetura, arquivo):
    plt.figure(figsize=[14,7])

    # Função original
    plt.subplot(1,3,1)
    plt.title('Função Original')
    plt.plot(x, y, color='green')

    # Curva de erro (com base nos erros anteriores)
    plt.subplot(1,3,2)
    plt.title('Curva erro (melhor resultado)')
    plt.plot(y - y_est, color='red')

    # Função original x função aproximada
    plt.subplot(1,3,3)
    plt.title(f'Função Original x Função Aproximada (Arquitetura {arquitetura})')
    plt.plot(x, y, linewidth=1, color='green')
    plt.plot(x, y_est, linewidth=2, color='blue')

    plt.suptitle(f'Resultados para {arquivo} - Arquitetura {arquitetura}')
    plt.show()

# Função principal
def main():
    arquivos = [f'teste{i}.npy' for i in range(1, 6)]
    dados = [carregar_arquivo(arquivo) for arquivo in arquivos]
    
    resultados_arquivos = {}

    for arquivo, (x, y) in zip(arquivos, dados):
        print(f"Realizando simulações para o arquivo {arquivo}")
        resultados_arquivos[arquivo] = simular_arquiteturas(x, y)

    for arquivo, resultados in resultados_arquivos.items():
        print(f"Resultados para {arquivo}:")
        for arquitetura, (media_erro, desvio_erro) in resultados.items():
            print(f"  Arquitetura {arquitetura}: Média do erro = {media_erro:.5f}, Desvio padrão = {desvio_erro:.5f}")

    for arquivo, resultados in resultados_arquivos.items():
        melhor_arquitetura = min(resultados, key=lambda k: resultados[k][0])
        arquitetura = melhor_arquitetura
        x, y = dados[arquivos.index(arquivo)]
        regr = MLPRegressor(hidden_layer_sizes=arquitetura,
                            max_iter=400,
                            activation='tanh',
                            solver='adam',
                            learning_rate='adaptive',
                            n_iter_no_change=400,
                            verbose=False)
        regr.fit(x, y)
        y_est = regr.predict(x)
        plotar_resultados(x, y, y_est, arquitetura, arquivo)

if __name__ == "__main__":
    main()