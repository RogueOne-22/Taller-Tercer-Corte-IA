# 🛡️ Filtro Anti-Spam con Bayes 

![Badge](https://img.shields.io/badge/IA-Naive%20Bayes-blue) ![Badge](https://img.shields.io/badge/Python-3.x-yellow) ![Badge](https://img.shields.io/badge/Status-Robust-green)

> **¿Qué es esto?** > Este ejemplo es capaz de "leer" tus correos y decidir automáticamente si son **SPAM** (basura) o **HAM** (correo legítimo), usando la probabilidad estadística. 🧠✨

---

## 🔍 Teorema de Bayes

Es una fórmula matemática que nos ayuda a actualizar nuestras diccionario cuando tenemos nueva evidencia. Se puede representar como una balanza, por ejemplo:

* La sospecha inicial ()"El 30% de todo es spam").
* Cada palabra del correo es un "peso" que ponemos en la balanza.
    * La palabra **"Gratis"** pesa más hacia el lado de **Spam**. 🔴
    * La palabra **"Reunión"** pesa menos hacia el lado de **No Spam**. 🟢

![Diagrama Naive Bayes](https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Bayes%27_Theorem_MMB_01.jpg/640px-Bayes%27_Theorem_MMB_01.jpg)

El algoritmo multiplica las probabilidades de todas las palabras para tomar la decisión final. Se llama **"Naive" (Ingenuo)** porque asume que las palabras no tienen relación entre sí.
---

## 💪Cambios

La versión básica de este algoritmo falla en la vida real. se le realizo **dos mejoras matemáticas** para que funcione con mas palabras:

### 1. El Problema de la "Palabra Intrusa" 👽
**Fallo:** Si llega un correo con una palabra que el sistema NUNCA ha visto (ej. "Criptomoneda"), la probabilidad es **0** haciendo que el resultado sea cero y El filtro fallaría.

**✨ Solución: Laplace Smoothing**
Se pretende que **todas** las palabras del diccionario han aparecido al menos 1 vez.
> *Fórmula:* `(Conteo real + 1)`  
> Así, ninguna palabra vale 0. Si es nueva, vale muy poquito, pero esta incluida.

### 2. Underflow 😵‍💫
**El fallo:** Cuando se multiplica probabilidades pequeñas (0.001 × 0.05 × 0.0002...), el número se puede volver lo suficientemente pequeño que el computador se queda sin memoria y lo redondea a cero.

**✨ La Solución: Logaritmos**
En lugar de multiplicar números diminutos, **suma de logaritmos**.
> `log(A) + log(B)` es mucho más fácil de manejar que `A × B`.  
> Esto permite procesar textos largos sin errores numéricos.

---

## ⚙️ Algoritmo

Explicación del programa paso a paso:

### 🧹 Paso 1: Preprocesado
Antes de leer, el algoritmo **normaliza** el texto.
* Convierte todo a **minúsculas** (para que "OFERTA" y "oferta" sean lo mismo).
* Elimina **signos de puntuación** (puntos, comas, signos de exclamación).
* Separa el texto en una lista de palabras individuales (Tokens).

### 👨‍🏫 Paso 2: Entrenamiento
El algoritmo "aprende".
1.  Recibe una lista de correos ya etiquetados (Spam o Seguro).
2.  Crea un diccionario (**Vocabulario**).
3.  Cuenta cuántas veces aparece cada palabra en correos Spam vs. Seguros.
4.  Calcula la **Probabilidad**: ¿Qué tan común es recibir spam en general?

### 👨‍⚖️ Paso 3: Predicción
Cuando llega un correo nuevo:
1.  El algoritmo busca cada palabra en su memoria.
2.  Si la palabra existe, recupera su probabilidad.
3.  Suma los puntajes en dos casillas: `Score_Spam` y `Score_Ham`.
4.  **Veredicto Final:** Compara los puntajes. El que tenga el número mayor, gana.

---

## 🚀 Ejemplo

```python
# Ejemplo de uso conceptual:

# 1. Crear el cerebro
bot = DetectorSpamRobusto()

# 2. Entrenar (enseñarle qué es spam y qué no)
correos = ["Compra ya", "Reunión mañana"]
etiquetas = [1, 0] # 1=Spam, 0=Seguro
bot.entrenar(correos, etiquetas)

# 3. Preguntar
resultado = bot.predecir("Compra urgente ahora")
print(resultado) 
# Salida: 🛑 ES SPAM

```

## ✨Autor
### Paula S
