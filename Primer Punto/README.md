# 📘 Aprendizaje por Refuerzo

> **Este documento responde tres preguntas fundamentales sobre aprendizaje por refuerzo**

---

## 📋 Índice de Contenidos
1. [Optimización bajo Incertidumbre (Pregunta A)](#a-¿cómo-puede-un-agente-aprender-a-tomar-decisiones-óptimas-en-un-entorno-incierto)
2. [Taxonomía y Arquitecturas (Pregunta B)](#b-¿cuáles-son-los-tipos-de-algoritmos-y-sus-arquitecturas)
3. [Aplicaciones Industriales (Pregunta C)](#c-en-la-industria-estos-algoritmos-para-qué-se-utilizan)

---

## 1. ¿Cómo puede un agente aprender a tomar decisiones óptimas en un entorno incierto? 🎲

Para que un agente computacional converja hacia una política óptima ($\pi^*$) en un entorno donde las transiciones son estocásticas (probabilísticas), se debe formalizar el problema mediante un **Proceso de Decisión de Markov (MDP)**.

El aprendizaje no ocurre por memoria, sino mediante la **maximización del retorno esperado** ($G_t$). El agente resuelve utilizando dos mecanismos matemáticos:

### A. La Ecuación de Optimalidad de Bellman
Esta ecuación permite al agente estimar el valor presente de sus acciones considerando todas las posibles recompensas futuras, ponderadas por su probabilidad de ocurrencia:

$$ Q^*(s, a) = \mathbb{E}_{s'} $$

* **$R$ (Recompensa):** Feedback inmediato.
* **$\gamma$ (Factor de Descuento):** Determina la importancia del futuro frente al presente.

### B. Aproximación de la Función de Valor
En entornos inciertos, el agente construye una "superficie de valor" que le indica qué tan bueno es estar en un estado $s$. A través de métodos como **Diferencia Temporal (TD-Learning)**, el agente actualiza sus predicciones paso a paso comparando su expectativa con la realidad observada, reduciendo progresivamente el error de predicción.

---

## 2. ¿Cuáles son los tipos de algoritmos de aprendizaje por refuerzo que existen y cuáles son sus arquitecturas? 

🏗️ En el Aprendizaje por Refuerzo Profundo (Deep RL), se clasifica los algoritmos según la función objetivo que optimizan. La imagen describe la arquitectura de red neuronal para cada familia.

![Diagrama de Arquitecturas de Deep RL: Value vs Policy vs Actor-Critic](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Reinforcement_learning_diagram.svg/1200px-Reinforcement_learning_diagram.svg.png)
*(Nota: Este diagrama ilustra el flujo de tensores para cada paradigma descrito abajo)*

### a. Métodos Basados en Valor (Value-Based) 💎
El objetivo es aproximar la función $Q(s, a)$. El agente selecciona la acción con el valor más alto.
* **Algoritmo Representativo:** **DQN (Deep Q-Network)**.
* **Arquitectura:**
    * **Input:** Tensor de Estado $S$ (ej. imagen pixelada).
    * **Red:** CNN (Convolucional) + Capas Densas (Fully Connected).
    * **Output:** Un vector de valores escalares, uno por cada acción posible.
    * **Elemento Clave:** *Experience Replay Buffer* (memoria para romper correlaciones temporales).

### b. Métodos Basados en Política (Policy-Based) 📜
El objetivo es optimizar directamente la función de política $\pi(a|s)$ sin calcular valores intermedios necesariamente.
* **Algoritmo Representativo:** **REINFORCE**.
* **Arquitectura:**
    * **Input:** Tensor de Estado $S$.
    * **Red:** Red Neuronal profunda.
    * **Output:** Una distribución de probabilidad (Softmax) sobre las acciones.
    * **Elemento Clave:** *Gradiente de Política* ($\nabla_\theta J(\theta)$), que ajusta los pesos en la dirección que aumenta la recompensa esperada.

### c. Arquitecturas Actor-Crítico (Actor-Critic) 🔄
Combinan las ventajas de los dos anteriores para mayor estabilidad y eficiencia. Es el estándar actual.
* **Algoritmo Representativo:** **PPO (Proximal Policy Optimization)**.
* **Arquitectura Híbrida:**
    * **Cabeza del Actor (Policy):** Decide *qué* acción tomar (Output: Probabilidades).
    * **Cabeza del Crítico (Value):** Evalúa *qué tan buena* fue la acción (Output: Valor Escalar $V(s)$).
    * **Interacción:** El Crítico calcula el "Error de Predicción" (TD-Error) y lo usa para enseñar al Actor a corregir sus probabilidades.

---

## 3. En la industria estos algoritmos para qué se utilizan? 🚀

La capacidad de resolver problemas de optimización dinámica no lineal ha llevado al RL a sectores importantes:

### 🦾 Robótica y Control Autónomo
Se utiliza para resolver problemas de cinemática compleja donde la programación tradicional es inviable.
* **Ejemplo:** Robots cuadrúpedos (como Spot de Boston Dynamics) aprendiendo a recuperar el equilibrio tras un empujón imprevisto o a navegar terrenos irregulares mediante *Sim-to-Real transfer*.

### 📉 Finanzas Algorítmicas (FinTech)
Sistemas de trading que operan en milisegundos.
* **Ejemplo:** Ejecución óptima de órdenes (Smart Order Routing) para minimizar el impacto en el mercado y gestión dinámica de portafolios ajustando el riesgo en tiempo real según la volatilidad estocástica del mercado.

### 🏭 Optimización Energética y Procesos
Control de sistemas físicos a gran escala.
* **Ejemplo:** **Google DeepMind** aplicó RL para controlar los sistemas de enfriamiento de sus Data Centers, logrando una reducción del 40% en el consumo de energía al predecir la carga térmica y ajustar las válvulas de forma proactiva.

### 🧬 Salud y Biomedicina
Personalización de tratamientos.
* **Ejemplo:** Diseño de regímenes de dosificación dinámicos para pacientes con enfermedades crónicas, optimizando la eficacia del fármaco mientras se minimiza la toxicidad acumulada en el cuerpo.

***
