from scipy.stats import norm, nakagami
from scipy.special import gamma
import numpy as np
import matplotlib.pyplot as plt


def nakagami_m(h,m):
    return (2*(m**m)*h**(2*m-1)*np.exp(-m*h**2))/gamma(m)

def fit(data, filename):
    Pr = 10**(data/10)
    h = np.sqrt(Pr/np.mean(Pr))
    paramh = nakagami.fit(h)
    x = np.linspace(0,3,1000)
    fig, ax = plt.subplots(sharey=False)
    ax.plot(x, nakagami.pdf(x,nu=paramh[0],loc=paramh[1],scale=paramh[2]))
    ax.set_ylabel('Nakagami')
    ax2 = ax.twinx()
    h.plot(kind='hist', ax=ax2, color='g')
    fig.savefig(filename + '_dist' +'.png', bbox_inches='tight',dpi=300)
    pass