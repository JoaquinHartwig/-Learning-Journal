permisos_solicitados = [" READ ", "write", "EXECUTE", "  DELETE  "]
permisos_permitidos_rol = ["read", "write", "execute"]
solicitud_normalizada = []

for value in permisos_solicitados:
    value = value.strip().lower()
    solicitud_normalizada.append(value)

print(solicitud_normalizada)


if "delete" in solicitud_normalizada and "delete" not in permisos_permitidos_rol:
    print("ACCESO DENEGADO: Intento de borrado no autorizado.")

if ("write" in solicitud_normalizada and "execute" in solicitud_normalizada) and ("read" not in solicitud_normalizada):
    print("CONFIGURACIÓN INCONSISTENTE: No podés modificar ni ejecutar sin permiso de lectura.")
permisos_otorgados = []
permisos_denegados = []

for permiso in solicitud_normalizada:
    if permiso in permisos_permitidos_rol:
        permisos_otorgados.append(permiso)
    else:
        permisos_denegados.append(permiso)


print("\n--- RESUMEN DE PERMISOS ---")
print(f"Otorgados: {permisos_otorgados}")
print(f"Denegados: {permisos_denegados}")