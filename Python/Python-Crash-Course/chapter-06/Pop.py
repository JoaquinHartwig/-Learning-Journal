servidor = {'host': '127.0.0.1', 'puerto': 8080, 'status': 'active'}

# Elimina 'status' y guarda su valor
estado_previo = servidor.pop('status')
print(f"Estado removido: {estado_previo}")  # Output: Estado removido: active

# Uso seguro con valor por defecto si la clave no existe
intento_fallido = servidor.pop('token', 'Clave no encontrada')
print(intento_fallido)  # Output: Clave no encontrada


tarea = {'id': 101, 'titulo': 'Corregir bug', 'prioridad': 'alta'}

# Remueve el último elemento ingresado ('prioridad')
clave_eliminada, valor_eliminado = tarea.popitem()

print(f"Removido: {clave_eliminada} -> {valor_eliminado}")
# Output: Removido: prioridad -> alta