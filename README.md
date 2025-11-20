# 📘 Taller 3er Corte

![Badge](https://img.shields.io/badge/Topic-Reinforcement%20Learning-red) ![Badge](https://img.shields.io/badge/Topic-Naive%20Bayes-green) 

> **Resumen:** Este repositorio se encuentra el desarollo del taller de tercer corte en el cual se ven los siguientes temas:
> 1.  **Aprendizaje por Refuerzo:** Teoría de toma de decisiones, ecuaciones y arquitecturas.
> 2.  **Teorema de Bayes:** Implementación de un ejemplo basado en el teorema de Bayes que filtra los correos de Spam.
> 3.  **High Demand Algorithms for 2025:** Resumen de los algoritmos líderes en la industria actual. 
---

## Parte I: Aprendizaje por Refuerzo  🤖

### A. Toma de Decisiones bajo Incertidumbre
**Pregunta:** *¿Cómo puede un agente aprender a tomar decisiones óptimas en un entorno incierto?*

El agente modela el mundo como un **Proceso de Decisión de Markov (MDP)**. No memoriza respuestas, sino que aprende a maximizar el **retorno esperado** a largo plazo ($G_t$). Para resolver la incertidumbre, utiliza la **Ecuación de Bellman**, que descompone el valor de una decisión en recompensa inmediata + futuro descontado:

$$Q(s, a) = R + \gamma \cdot \max_{a'} Q(s', a')$$

### B. Arquitecturas y Algoritmos
En Deep RL, clasificamos los algoritmos según qué función aproximan las redes neuronales:

![Diagrama de Arquitecturas RL](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Reinforcement_learning_diagram.svg/800px-Reinforcement_learning_diagram.svg.png)

| Tipo | Algoritmo Clave | Descripción Técnica |
| :--- | :--- | :--- |
| **Value-Based** | **DQN (Deep Q-Network)** | Aprende la función de valor $Q(s,a)$. Selecciona acciones deterministas buscando el valor máximo. |
| **Policy-Based** | **REINFORCE** | Aprende directamente la política $\pi(a\|s)$ ajustando las probabilidades de acción mediante gradiente. |
| **Actor-Critic** | **PPO (Proximal Policy Optimization)** | **Híbrido:** Un "Actor" decide la acción y un "Crítico" evalúa qué tan buena fue. Es el estándar actual por su estabilidad. |

### C. Aplicaciones Industriales
* **Robótica:** Control dinámico de movimiento (Boston Dynamics).
* **Finanzas:** Trading algorítmico y gestión de carteras.
* **Data Centers:** Optimización de sistemas de enfriamiento (Google DeepMind).
* **LLMs:** Alineación de modelos de lenguaje con feedback humano (RLHF).

---

## Parte II: Teorema de Bayes (Práctica) 📧

Clasificador de correos utilizando el **Teorema de Bayes**.

### Desafío
El algoritmo matemático estándar falla en entornos reales por dos problemas críticos que hemos solucionado en este código:

1.  **Problema del Cero (Zero Frequency):** Si una palabra es nueva, su probabilidad es 0, anulando toda la ecuación.
    * *Solución:* **Suavizado de Laplace** (Sumar +1 a todos los conteos).
2.  **Problema del Underflow Aritmético:** Multiplicar muchas probabilidades pequeñas (ej. $0.001^{100}$) causa errores de redondeo a cero.
    * *Solución:* **Logaritmos**. Transformamos multiplicaciones en sumas: $\log(a \cdot b) = \log(a) + \log(b)$.

```
Ejemplo de salida:
        
        return "🛑 SPAM" if log_spam > log_ham else "✅ SEGURO"
```

Parte III: ALgoritmos en tendencia en 2025 🚀

Resumen de las tecnologías y algoritmos dominantes por sector en la actualidad.
| Dominio | Algoritmo Líder | Academia vs. Industria |
| :--- | :--- | :--- |
| **Datos Tabulares** <br>*(Excel/SQL/Riesgo)* | **XGBoost / LightGBM** | **Industria:** El rey absoluto por velocidad y manejo de datos faltantes. Las redes neuronales rara vez superan a los árboles aquí. |
| **Visión Computarizada** <br>*(Detección Objetos)* | **YOLO v8/v10** | **Industria:** Preferido por su capacidad de trabajar en tiempo real (video). <br>**Academia:** Prefiere *Vision Transformers (ViT)* por precisión pura. |
| **NLP** <br>*(Texto/Chat)* | **Transformers (GPT/Llama)** | Estándar indiscutible. Arquitecturas basadas en *Attention Mechanism* han reemplazado a las RNN/LSTM. |
| **Robótica y Control** | **PPO (Proximal Policy Opt)** | Usado por su estabilidad matemática para evitar que los agentes "olviden" lo aprendido. |
| **Generación Imagen** | **Stable Diffusion** | Modelos de difusión latente han reemplazado a las GANs en la generación de arte. |
| **Anomalías** <br>*(Fraude)* | **Isolation Forest** | Estándar eficiente para detectar "datos raros" en banca y ciberseguridad. |

# Autor
### Paula S
