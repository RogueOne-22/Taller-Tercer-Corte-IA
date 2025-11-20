import numpy as np
import matplotlib.pyplot as plt
import time
import random

# Entorno: Un pasillo lineal de 6 estados (0 a 5)
# Meta: Llegar al estado 5 (Recompensa +10)
N_ESTADOS = 6
ACCIONES = ['Izquierda', 'Derecha'] # 0: Izq, 1: Der
N_ACCIONES = len(ACCIONES)

# Paramétodos de aprendizaje por refuerzo
ALPHA = 0.5      # Tasa de aprendizaje (qué tan rápido aceptamos nueva info)
GAMMA = 0.9      # Factor de descuento (cuánto nos importa el futuro)
EPSILON = 0.2    # Probabilidad de explorar (hacer locuras)

# Inicializamos la Tabla Q con ceros
q_table = np.zeros((N_ESTADOS, N_ACCIONES))

# --- Configuración de Gráficos (Matplotlib) ---
plt.ion() 
fig, ax = plt.subplots(figsize=(8, 6))

def actualizar_grafico(episodio):
    ax.clear()
    # Creamos el mapa de calor
    cax = ax.matshow(q_table, cmap='viridis', vmin=0, vmax=10)
    
   
    ax.set_title(f'Memoria del Agente (Tabla Q) - Episodio: {episodio}')
    ax.set_ylabel('Estados (Posición del 0 al 5)')
    ax.set_xlabel('Acciones (0: Izq, 1: Der)')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(ACCIONES)
    
 
    for (i, j), z in np.ndenumerate(q_table):
        color = 'white' if z < 5 else 'black'
        ax.text(j, i, '{:0.2f}'.format(z), ha='center', va='center', color=color, weight='bold')

    plt.draw()
    plt.pause(0.1) # Pausa breve para que el ojo humano vea el cambio

# --- El Algoritmo Q-Learning ---
print("Iniciando entrenamiento... observa la ventana del gráfico.")

for episodio in range(20): # 20 intentos
    estado = 0 # Incializacion agente en cero
    terminado = False
    
    while not terminado:
        # Elegir Acción (Estrategia Epsilon-Greedy)
        if random.uniform(0, 1) < EPSILON:
            accion = random.choice([0, 1]) # Explorar
        else:
            accion = np.argmax(q_table[estado]) # Explotar (usar lo mejor conocido)

        # Ejecutar y observar resultado
        
        if accion == 0: # Izquierda
            proximo_estado = max(0, estado - 1)
            recompensa = 0
        else: 
            proximo_estado = min(N_ESTADOS - 1, estado + 1)
            if proximo_estado == 5 and estado != 5: # ¡Llegó a la meta!
                recompensa = 10
                terminado = True
            else:
                recompensa = 0

        # 3. ACTUALIZACIÓN DE BELLMAN 
        # Q(s,a) = Q(s,a) + alpha * [R + gamma * max(Q(s',a')) - Q(s,a)]
        
        valor_actual = q_table[estado, accion]
        mejor_futuro = np.max(q_table[proximo_estado]) # El valor del mejor estado siguiente
        
        nuevo_valor = valor_actual + ALPHA * (recompensa + GAMMA * mejor_futuro - valor_actual)
        q_table[estado, accion] = nuevo_valor

        estado = proximo_estado

        if terminado:
            actualizar_grafico(episodio + 1)

print("Entrenamiento finalizado. Cierra la ventana para terminar.")
plt.ioff()
plt.show()