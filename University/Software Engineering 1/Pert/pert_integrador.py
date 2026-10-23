import matplotlib.pyplot as plt
import networkx as nx

# 1. Definición de la Red AoA
tareas = [
    (0, 1, "1", 1),
    (1, 2, "1.2", 1),  
    (1, 3, "2", 1),
    (3, 4, "2.1", 1),
    (4, 5, "2.2", 1),
    (5, 6, "3", 1),
    (6, 7, "3.1", 1),
    (6, 8, "3.2", 1),
    (7, 9, "Fict.", 0),  
    (8, 9, "Fict.", 0),  
    (9, 10, "4", 3),
    (10, 11, "4.1", 1),
    (11, 12, "4.2", 1),
    (12, 13, "4.3", 1),
    (13, 14, "5", 1),
    (14, 15, "5.1", 1),
    (14, 16, "5.2", 1),
    (15, 17, "Fict.", 0), 
    (16, 17, "Fict.", 0), 
    (17, 18, "5.3", 1),
    (18, 19, "6", 2),     
    (18, 20, "6.1", 1),
    (20, 21, "6.2", 1),
    (20, 22, "6.3", 1),   
    (21, 23, "7", 2),     
    (21, 24, "7.1", 1),
    (24, 25, "7.2", 1),
    (25, 26, "7.3", 1)
]

G = nx.DiGraph()
for u, v, nombre, dur in tareas:
    G.add_edge(u, v, tarea=nombre, dur=dur, ficticia=(dur==0))
    G.add_node(u, Te=0, Tt=999)
    G.add_node(v, Te=0, Tt=999)

# 2. Forward Pass (Te)
nodos_ordenados = list(nx.topological_sort(G))
G.nodes[0]['Te'] = 0

for nodo in nodos_ordenados:
    for predecesor in G.predecessors(nodo):
        duracion_tarea = G.edges[predecesor, nodo]['dur']
        G.nodes[nodo]['Te'] = max(G.nodes[nodo]['Te'], G.nodes[predecesor]['Te'] + duracion_tarea)

duracion_total = G.nodes[nodos_ordenados[-1]]['Te']

# 3. Backward Pass (Tt)
for nodo in G.nodes():
    if G.out_degree(nodo) == 0:  
        G.nodes[nodo]['Tt'] = duracion_total

for nodo in reversed(nodos_ordenados):
    for sucesor in G.successors(nodo):
        duracion_tarea = G.edges[nodo, sucesor]['dur']
        G.nodes[nodo]['Tt'] = min(G.nodes[nodo]['Tt'], G.nodes[sucesor]['Tt'] - duracion_tarea)

# 4. Coordenadas Espaciadas (Escala X ampliada)
pos = {
    0: (0, 0), 1: (3, 0), 2: (6, 2), 3: (6, 0), 
    4: (9, 0), 5: (12, 0), 6: (15, 0), 
    7: (18, 1.5), 8: (18, -1.5), 9: (21, 0), 
    10: (24, 0), 11: (27, 0), 12: (30, 0), 13: (33, 0), 14: (36, 0),
    15: (39, 1.5), 16: (39, -1.5), 17: (42, 0), 18: (45, 0), 
    19: (48, 2), 20: (48, 0), 21: (51, 0), 22: (51, -2), 
    23: (54, 2), 24: (54, 0), 25: (57, 0), 26: (60, 0)
}

# 5. Renderizado Gráfico Panorámico
fig, ax = plt.subplots(figsize=(38, 8))
ax.set_title(f"MÉTODO AOA (Actividad en la Flecha) - Duración Total: {duracion_total} Días\nCírculos = Eventos | Flechas = Tareas", fontsize=18, fontweight='bold', pad=25)

# Dibujar Flechas
for u, v in G.edges():
    es_ficticia = G.edges[u, v]['ficticia']
    estilo = 'dashed' if es_ficticia else 'solid'
    color_flecha = '#7f8c8d' if es_ficticia else '#2c3e50'
    grosor = 1.5 if es_ficticia else 2.5
    
    ax.annotate("", xy=pos[v], xytext=pos[u],
                arrowprops=dict(arrowstyle="->", color=color_flecha, lw=grosor, ls=estilo, shrinkA=30, shrinkB=30))
    
    # Textos de flecha elevados para no chocar
    x_text = (pos[u][0] + pos[v][0]) / 2
    y_text = ((pos[u][1] + pos[v][1]) / 2) + 0.35
    texto_tarea = G.edges[u, v]['tarea'] + (f" ({G.edges[u,v]['dur']}d)" if not es_ficticia else "")
    ax.text(x_text, y_text, texto_tarea, fontsize=9.5, fontweight='bold', color='black', ha='center', va='center', bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.9))

# Dibujar Eventos
radio = 0.6
for nodo, (x, y) in pos.items():
    Te = G.nodes[nodo]['Te']
    Tt = G.nodes[nodo]['Tt']
    holgura = Tt - Te
    es_critico = (holgura == 0) and (G.out_degree(nodo) > 0 or nodo == 26)
    
    color_borde = '#e74c3c' if es_critico else '#3498db'
    
    circle = plt.Circle((x, y), radio, facecolor='#ffffff', edgecolor=color_borde, linewidth=2.5, zorder=5)
    ax.add_patch(circle)
    
    ax.plot([x - radio*0.85, x + radio*0.85], [y, y], color=color_borde, linewidth=1.5, zorder=6)
    ax.plot([x, x], [y - radio, y], color=color_borde, linewidth=1.5, zorder=6)
    
    ax.text(x, y + 0.25, f"Ev.{nodo}", fontsize=9, fontweight='bold', ha='center', va='center', zorder=7)
    ax.text(x - 0.25, y - 0.25, f"{Te}", fontsize=10, fontweight='bold', color='#27ae60', ha='center', va='center', zorder=7)
    ax.text(x + 0.25, y - 0.25, f"{Tt}", fontsize=10, fontweight='bold', color='#c0392b', ha='center', va='center', zorder=7)

ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig("pert_profesor_limpio.png", dpi=300, bbox_inches='tight')
plt.show()