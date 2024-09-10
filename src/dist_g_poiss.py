import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm, poisson

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

# Distribuição de Poisson com lambda = mu (média da binomial)
poisson_dist = poisson.pmf(k, mu)

# Plotando as distribuições
plt.plot(k, binomial, 'bo', label='Binomial')
plt.plot(k, gaussian, 'r-', label='Gaussiana (Normal)')
plt.plot(k, poisson_dist, 'g--', label='Poisson')
plt.xlabel('Número de Sucessos')
plt.ylabel('Probabilidade')
plt.title('Comparação entre Distribuições: Binomial, Gaussiana e Poisson')
#plt.title('Distribuição de Poisson')
plt.legend()
plt.show()
