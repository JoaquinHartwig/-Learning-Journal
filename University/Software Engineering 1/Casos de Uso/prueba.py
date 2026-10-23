import matplotlib.patches as patches
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Límite del Sistema
rect = patches.Rectangle(
    (3, 1),
    4.2,
    8,
    linewidth=2,
    edgecolor='navy',
    facecolor='#f0f4f8',
    linestyle='--',
)
ax.add_patch(rect)
ax.text(
    5.1,
    8.7,
    'Sistema de Gestión de Turnos Vida Animal',
    fontsize=12,
    fontweight='bold',
    ha='center',
)

# Actores
actores = {
    'Tutor': (1, 5, 'Tutor de\nMascota'),
    'Vet': (8.8, 7.5, 'Veterinario'),
    'Admin': (8.8, 2.5, 'Personal\nAdministrativo'),
}

for key, (x, y, text) in actores.items():
    ax.scatter(x, y, s=400, color='darkorange')
    ax.text(x, y - 0.7, text, fontsize=10, ha='center', fontweight='bold')

# Casos de Uso (Óvalos)
casos = {
    'UC1': (5.1, 7.5, 'Solicitar turno'),
    'UC2': (5.1, 6.0, 'Consultar disponibilidad'),
    'UC3': (5.1, 4.5, 'Registrarse en el sistema'),
    'UC4': (5.1, 3.2, 'Configurar agenda\nde disponibilidad'),
    'UC5': (5.1, 2.0, 'Generar reportes\nestadísticos'),
    'UC6': (3.8, 5.0, 'Cancelar /\nConfirmar turno'),
}

for key, (x, y, text) in casos.items():
    ellipse = patches.Ellipse(
        (x, y),
        1.8,
        0.8,
        edgecolor='darkblue',
        facecolor='white',
        linewidth=1.5,
    )
    ax.add_patch(ellipse)
    ax.text(x, y, text, fontsize=8, ha='center', va='center')

# Relaciones Actores -> Casos de uso
ax.plot([1, 4.2], [5, 7.5], 'k-', lw=1)  # Tutor -> Solicitar
ax.plot([1, 3.0], [5, 5.0], 'k-', lw=1)  # Tutor -> Cancelar/Confirmar
ax.plot([8.8, 6.0], [7.5, 3.2], 'k-', lw=1)  # Vet -> Configurar agenda
ax.plot([8.8, 6.0], [2.5, 2.0], 'k-', lw=1)  # Admin -> Reportes
ax.plot([8.8, 6.0], [2.5, 7.5], 'k-', lw=1)  # Admin -> Solicitar

# Flechas punteadas (Include / Extend)
ax.annotate(
    '<<include>>',
    xy=(5.1, 6.4),
    xytext=(5.1, 7.1),
    arrowprops=dict(arrowstyle='->', linestyle='dashed', color='red'),
    ha='center',
    fontsize=8,
    color='red',
)
ax.annotate(
    '<<extend>>',
    xy=(5.1, 4.9),
    xytext=(5.1, 7.1),
    arrowprops=dict(
        arrowstyle='->',
        linestyle='dashed',
        color='green',
        connectionstyle='arc3,rad=-0.3',
    ),
    ha='center',
    fontsize=8,
    color='green',
)

plt.tight_layout()
plt.show()