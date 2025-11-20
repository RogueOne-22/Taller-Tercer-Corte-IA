# 🚀 Algoritmos y Tecnologías en IA (2025)

![Badge](https://img.shields.io/badge/AI-State%20of%20the%20Art-blueviolet) ![Badge](https://img.shields.io/badge/Industry-Vs-Academia-orange) ![Badge](https://img.shields.io/badge/Documentation-Technical-blue)

> Este documento sirve como compendio técnico sobre los algoritmos, arquitecturas y técnicas más predominantes en el ecosistema de Inteligencia Artificial actual, destacando sus aplicaciones prácticas y diferencias de implementación.

---

## 1. Datos Tabulares y Negocio 📊
*(Excel, SQL, Finanzas, entre otros)*

 Los algoritmos de ensamble (árboles de decisión) dominan por su capacidad de manejar datos faltantes y su interpretabilidad.

| Algoritmo | Uso Principal | Características Clave |
| :--- | :--- | :--- |
| **XGBoost** | **Industria (Estándar)** | El caballo de batalla. Optimizado para velocidad y rendimiento. Usa regularización L1/L2 para evitar overfitting. |
| **LightGBM** | **Big Data / Kaggle** | Desarrollado por Microsoft. Usa un crecimiento de árbol "leaf-wise" (por hojas) en lugar de por niveles. Es drásticamente más rápido y consume menos memoria. |
| **CatBoost** | **Datos Categóricos** | Desarrollado por Yandex. Maneja variables categóricas (ej. "Rojo", "Azul") automáticamente sin necesidad de *One-Hot Encoding* previo. |

---

## 2. Visión artificial 👁️
*(Detección de objetos, diagnóstico médico y vehículos autónomos.)*

### 🏭 Industria:
* **YOLO (You Only Look Once) v8/v9/v10:**
    * **Arquitectura:** CNN de una sola etapa.
    * **Características:** Procesa la imagen completa una sola vez y predice cajas delimitadoras y clases simultáneamente.
    * **Uso:** Cámaras de seguridad, detección de defectos en manufactura, conducción autónoma.

### 🎓 Academia:  
* **Vision Transformers (ViT):**
    * **Arquitectura:** Transformer (sin convoluciones).
    * **Características:** Divide la imagen en "parches" (ej. 16x16 px) y los trata como palabras en una frase. Supera a las CNNs cuando hay *datasets* masivos.
    * **Uso:** Investigación médica de alta precisión, clasificación satelital.

En esta rama se percibe una division en su aplicabilidad en cuando a la velocidad para la industria y la precisión para la academia.

---

## 3. Procesamiento de Lenguaje Natural (NLP) 🗣️
* LLMs (Large Language Models).*

La arquitectura **Transformer** ha desplazado a todas las anteriores (RNN, LSTM).

### Arquitecturas Dominantes
* **Decoder-Only (Familia GPT / Llama / Mistral):**
    * **Función:** Generación de texto. Predicen la "siguiente palabra".
    * **Tecnología:** Mecanismo de *Self-Attention*.
    * **Uso:** Chatbots, generación de código, asistentes virtuales.
* **Encoder-Only (Familia BERT / RoBERTa):**
    * **Función:** Comprensión y Clasificación.
    * **Uso:** Motores de búsqueda (Google), análisis de sentimientos, extracción de entidades legales.

### Tecnologías de Optimización (Muy populares hoy)
* **LoRA (Low-Rank Adaptation):**
    * Permite re-entrenar modelos gigantes (como Llama-3) en una sola GPU de consumidor, modificando solo una pequeña fracción de los pesos.
* **RAG (Retrieval-Augmented Generation):**
    * Conecta un LLM (como GPT-4) a una base de datos privada para que responda con hechos reales y no alucine.

---

## 4. IA Generativa 🎨
*Creación de imágenes, audio y video.*

| Algoritmo | Tipo | Características |
| :--- | :--- | :--- |
| **Latent Diffusion Models** | **Stable Diffusion** | Aprenden a eliminar el "ruido" de una imagen estática hasta formar una imagen nítida. Dominan la generación de arte actual. |
| **GANs (Generative Adversarial Networks)** | **StyleGAN** | Dos redes peleando (Generador vs Discriminador). Aunque desplazadas por Diffusion, siguen siendo líderes en generación de rostros humanos hiperrealistas. |

---

## 5. Aprendizaje por Refuerzo y Robótica 🤖
*Toma de decisiones secuenciales.*

* **PPO (Proximal Policy Optimization):**
    * **El Favorito:** Usado por OpenAI y la industria en general.
    * **Por qué:** Es el equilibrio perfecto entre facilidad de implementación y estabilidad matemática.
* **SAC (Soft Actor-Critic):**
    * **Robótica Física:** Muy utilizado para entrenar robots reales.
    * **Características:** Maximiza no solo la recompensa, sino la "entropía" (la aleatoriedad), lo que permite al robot explorar mejor y no quedarse atascado en movimientos rígidos.

---

## 6. Aprendizaje No Supervisado y Reducción Dimensional (Unsupervised)
*Encontrar patrones ocultos sin etiquetas.*

* **Isolation Forest:**
    * **Industria:** El estándar de oro para **Detección de Anomalías** (Fraude bancario, fallos en servidores). Funciona aislando los puntos "raros" aleatoriamente.
* **UMAP (Uniform Manifold Approximation and Projection):**
    * **Visualización:** Reemplazó al antiguo t-SNE.
    * **Uso:** Permite visualizar datos de 100 dimensiones en un gráfico 2D manteniedo la estructura global de los datos. Muy usado en bioinformática (genética).

---

### 🏆 Resumen de las aplicaciones mas actuales

| Si tienes... | Usa esto... |
| :--- | :--- |
| **Tablas de Excel / DB** | XGBoost o LightGBM |
| **Imágenes (Tiempo real)** | YOLO |
| **Imágenes (Alta precisión)** | Vision Transformer (ViT) |
| **Texto / Chat** | Llama 3 / GPT-4 (Transformers) |
| **Pocos datos de texto** | BERT (Fine-tuned) |
| **Robots / Videojuegos** | PPO |
| **Detección de Fraude** | Isolation Forest |

***

## Autor
### Paula S