import math
import re

class DetectorSpamRobusto:
    def __init__(self):
        # Contadores
        self.vocabulario = set()
        self.spam_counts = {}
        self.ham_counts = {} # Ham = No Spam
        self.total_spam = 0
        self.total_ham = 0
        
        # Priors (se calcularán al entrenar)
        self.prob_spam = 0.0
        self.prob_ham = 0.0

    def limpiar_texto(self, texto):
        """Convierte a minúsculas y quita signos de puntuación básicos"""
        texto = texto.lower()
        palabras = re.findall(r'\b\w+\b', texto)
        return palabras

    def entrenar(self, correos, etiquetas):
        """
        Aprende de una lista de correos.
        etiquetas: 1 para Spam, 0 para No Spam (Ham)
        """
        num_correos = len(correos)
        self.prob_spam = sum(etiquetas) / num_correos
        self.prob_ham = 1.0 - self.prob_spam # P(Ham) = 1 - P(Spam)

        print(f"--- Entrenamiento Iniciado con {num_correos} correos ---")

        for i in range(num_correos):
            palabras = self.limpiar_texto(correos[i])
            es_spam = etiquetas[i] == 1
            
            for palabra in palabras:
                self.vocabulario.add(palabra)
                if es_spam:
                    self.spam_counts[palabra] = self.spam_counts.get(palabra, 0) + 1
                    self.total_spam += 1
                else:
                    self.ham_counts[palabra] = self.ham_counts.get(palabra, 0) + 1
                    self.total_ham += 1
        
        print("Entrenamiento finalizado.\n")

    def calcular_probabilidad_palabra(self, palabra):
        """
        Aplica SUAVIZADO DE LAPLACE (Add-1 Smoothing).
        P(w|c) = (conteo_w + 1) / (total_palabras_c + tamaño_vocabulario)
        """
        n_vocab = len(self.vocabulario)
        
        # Para Spam
        conteo_spam = self.spam_counts.get(palabra, 0)
        p_word_spam = (conteo_spam + 1) / (self.total_spam + n_vocab)
        
        # Para Ham
        conteo_ham = self.ham_counts.get(palabra, 0)
        p_word_ham = (conteo_ham + 1) / (self.total_ham + n_vocab)
        
        return p_word_spam, p_word_ham

    def predecir(self, mensaje):
        palabras = self.limpiar_texto(mensaje)
        
        # Usamos LOGARITMOS para evitar Underflow
        # log(P(Spam)) inicial
        log_prob_spam = math.log(self.prob_spam)
        log_prob_ham = math.log(self.prob_ham)
        
        for palabra in palabras:
            # Si la palabra no existe en el vocabulario, la ignoramos en este ejemplo simple
            # (Aunque Laplace ya maneja palabras raras, si es totalmente nueva no aporta info)
            if palabra in self.vocabulario:
                p_spam, p_ham = self.calcular_probabilidad_palabra(palabra)
                
                # Sumamos logs en lugar de multiplicar probabilidades
                log_prob_spam += math.log(p_spam)
                log_prob_ham += math.log(p_ham)
        
        # Imprimir detalles técnicos
        print(f"Mensaje: '{mensaje}'")
        print(f"  > Log-Score Spam: {log_prob_spam:.2f}")
        print(f"  > Log-Score Ham:  {log_prob_ham:.2f}")
        
        if log_prob_spam > log_prob_ham:
            return "🛑 ES SPAM"
        else:
            return "✅ ES SEGURO"

# ==========================================
# PRUEBA DE ROBUSTEZ
# ==========================================

# 1. Datos de Entrenamiento (Pequeño Dataset)
correos_train = [
    "Oferta gratis compra ahora dinero",    # Spam
    "Reunión de trabajo urgente mañana",   # Ham
    "Gana dinero facil casino gratis",      # Spam
    "Hola mamá, te quiero",                 # Ham
    "Urgente actualiza tu contraseña banco" # Spam
]
etiquetas_train = [1, 0, 1, 0, 1] # 1=Spam, 0=Ham

# 2. Instanciar y Entrenar
filtro = DetectorSpamRobusto()
filtro.entrenar(correos_train, etiquetas_train)

# 3. Predecir casos nuevos
# Nota: "Lotería" nunca se vio en el entrenamiento. 
# El algoritmo simple fallaría (división por cero o prob=0).
# Este algoritmo usa Laplace para manejarlo.

resultado1 = filtro.predecir("Urgente oferta de casino")
print(f"  > Resultado: {resultado1}\n")

resultado2 = filtro.predecir("Reunión de trabajo mañana")
print(f"  > Resultado: {resultado2}\n")

# Caso difícil: Palabra desconocida ("Lotería") + Palabra spam ("Dinero")
resultado3 = filtro.predecir("Gana la lotería y dinero") 
print(f"  > Resultado: {resultado3}")