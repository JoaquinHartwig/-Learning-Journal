## Requisitos previos

- **Python 3.9** o superior
- **pip** (administrador de paquetes de Python) actualizado

---

## Instalación

### Opción 1: Mediante `pip` (Recomendado)

Se recomienda realizar la instalación dentro de un entorno virtual para evitar conflictos de dependencias:

1. **Crear y activar un entorno virtual:**

   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

2. **Instalar SciPy:**
   ```bash
   pip install --upgrade pip
   pip install scipy

## Verificación de la Instalación:

python -c "import scipy; print(scipy.__version__)"


## Ejercicios:


Ejercicio Nº1: Un jugador encesta triples con probabilidad
0.55. Calcula la probabilidad de que al tirar 6 veces enceste:
a) 4 veces b) Todas las veces c) Ninguna vez d) entre 2 y
4 veces (limites excluidos) e) 1 ≤ X ≤ 4