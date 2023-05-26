#Creado por Cesar Augusto Perez Mayo de 2023
import pandas as pd
import random

def generar_sistema(n,L):
    """funcion rápida para crear un sistema de N puntos aleatorio en una caja
       cúbica de dimension L,
       devuelve las coordendas en un dataframe de columnas x,y,z
    """
    #
    x = []
    y = []
    z = []
    for i in range(n):
        x.append(random.uniform(0,L))
        y.append(random.uniform(0,L))
        z.append(random.uniform(0,L))
    return  pd.DataFrame({'x':x,'y':y,'z':z})
    

def centrar(x,dx,L):
    """Funcion para centrar una coordenada 1-D en un sistema de dimension L usando
    condiciones de frontera periodicas
    recibe
    la coordenada a centrar: x
    la distancia al centro del sistema: dx
    la dimension lineal de sistema: L
    
    devuelve la corodenada centrada
    """
    if x <= L/2:
        if x + dx <= L:
            x = x + dx
        else:
            x = x + dx - L
    else:
        if x + dx >= 0:
            x = x - dx
        else:
            x = L - x + dx
    
    return x
    
    
    
if __name__ == '__main__':
    #crear sistema
    L = 50
    N = 20
    sistema = generar_sistema(N,L)
    xc = sistema.iloc[0,0]
    yc = sistema.iloc[0,1]
    zc = sistema.iloc[0,2]
    
    dx = abs(xc - L/2)
    dy = abs(yc - L/2)
    dz = abs(zc - L/2)
    
    
    print('x_old:     ',xc)
    print('dx:        ',dx)
    print('x_new:     ',  centrar(xc,dx,L))
    
    
    sistema['x_c'] = sistema['x'].apply(centrar,args=(dx,L))
    sistema['y_c'] = sistema['y'].apply(centrar,args=(dy,L))
    sistema['z_c'] = sistema['z'].apply(centrar,args=(dz,L))
    
    
    
