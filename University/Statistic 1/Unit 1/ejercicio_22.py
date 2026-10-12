import numpy as np

# 1. Definir los intervalos y sus frecuencias absolutas (fa)
limites_inferiores = np.array([18, 21, 24, 27, 30])
limites_superiores = np.array([21, 24, 27, 30, 33])
fa = np.array([12, 25, 20, 12, 6])

# Marcas de clase (xi), amplitud (Ai) y total (n)
xi = (limites_inferiores + limites_superiores) / 2.0
Ai = limites_superiores[0] - limites_inferiores[0]
n = np.sum(fa)
Fa = np.cumsum(fa)

# --- TENDENCIA CENTRAL Y DISPERSIÓN ---
media = np.sum(xi * fa) / n
s2 = np.sum(fa * (xi - media)**2) / (n - 1)  # Varianza muestral
s = np.sqrt(s2)                              # Desvío estándar
cv = (s / media) * 100                        # Coeficiente de Variación %

# --- FUNCIÓN DE INTERPOLACIÓN PARA CUANTILES ---
def calcular_cuantil(porcentaje):
    pos = (porcentaje / 100.0) * n
    idx = np.searchsorted(Fa, pos)
    L_inf = limites_inferiores[idx]
    F_ant = Fa[idx - 1] if idx > 0 else 0
    f_propia = fa[idx]
    return L_inf + ((pos - F_ant) / f_propia) * Ai

mediana = calcular_cuantil(50)
q1 = calcular_cuantil(25)
q3 = calcular_cuantil(75)
p10 = calcular_cuantil(10)
p65 = calcular_cuantil(65)
p90 = calcular_cuantil(90)
ric = q3 - q1

# --- MODA (MÉTODO DELTA) ---
idx_m = np.argmax(fa)
L_inf_m = limites_inferiores[idx_m]
fm = fa[idx_m]
f_ant = fa[idx_m - 1] if idx_m > 0 else 0
f_sig = fa[idx_m + 1] if idx_m < len(fa) - 1 else 0
d1, d2 = fm - f_ant, fm - f_sig
moda = L_inf_m + (d1 / (d1 + d2)) * Ai

# --- MOMENTOS Y FORMA ---
m3 = np.sum(fa * (xi - media)**3) / n
m4 = np.sum(fa * (xi - media)**4) / n
asimetria = m3 / (s**3)
curtosis = m4 / (s**4)

# --- IMPRESIÓN DE RESULTADOS ---
print(f"--- VERIFICACIÓN DE RESULTADOS (n = {n}) ---")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Q1: {q1:.2f} | Q3: {q3:.2f} | RIC: {ric:.2f}")
print(f"P10: {p10:.2f} | P65: {p65:.2f} | P90: {p90:.2f}")
print(f"Desvío Estándar (s): {s:.2f} | CV%: {cv:.2f}%")
print(f"Momento 3 (m3): {m3:.2f} | Asimetría (SKm): {asimetria:.2f}")
print(f"Momento 4 (m4): {m4:.2f} | Curtosis (K4): {curtosis:.2f}")