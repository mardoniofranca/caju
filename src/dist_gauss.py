import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parâmetros da distribuição binomial
n = 100  # número de tentativas
p = 0.5  # probabilidade de sucesso em cada tentativa
k = np.arange(0, n+1)

# Distribuição Binomial
binomial = binom.pmf(k, n, p)

# Parâmetros da distribuição normal aproximada (gaussiana)
mu = n * p  # média
sigma = np.sqrt(n * p * (1 - p))  # desvio padrão

# Distribuição Gaussiana
gaussian = norm.pdf(k, mu, sigma)

# Plotando as distribuições
plt.plot(k, binomial, 'bo', label='Binomial')
plt.plot(k, gaussian, 'r-', label='Gaussiana (Normal)')
plt.xlabel('Número de Sucessos')
plt.ylabel('Probabilidade')
plt.title('Comparação entre Distribuição Binomial e Gaussiana')
plt.legend()
plt.show()