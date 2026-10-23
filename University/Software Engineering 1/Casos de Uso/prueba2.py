from graphviz import Digraph

dot = Digraph('CasosDeUso_VidaAnimal', format='png')
dot.attr(rankdir='LR', size='12,8', fontname='Arial')

# Actor principal a la izquierda
dot.node('Tutor', 'Tutor de Mascota\n(Actor)', shape='box', style='rounded')

# Rectángulo del Sistema
with dot.subgraph(name='cluster_sistema') as c:
  c.attr(
      label='Sistema de Gestión de Turnos Vida Animal',
      style='rounded',
      color='black',
      fontsize='14',
  )
  c.node_attr.update(shape='ellipse', fontname='Arial')

  c.node('UC1', 'Solicitar turno')
  c.node('UC2', 'Consultar disponibilidad')
  c.node('UC3', 'Registrarse en el sistema')
  c.node('UC4', 'Configurar agenda\nde disponibilidad')
  c.node('UC5', 'Generar reportes\nestadísticos')
  c.node('UC6', 'Cancelar / Confirmar\nturno')

# Actores secundarios a la derecha
dot.node('Vet', 'Veterinario\n(Actor)', shape='box', style='rounded')
dot.node('Admin', 'Personal Administrativo\n(Actor)', shape='box', style='rounded')

# Conexiones Actores <-> Casos de uso
dot.edge('Tutor', 'UC1', dir='none')
dot.edge('Tutor', 'UC6', dir='none')
dot.edge('UC1', 'Admin', dir='none')
dot.edge('UC4', 'Vet', dir='none')
dot.edge('UC5', 'Admin', dir='none')

# Relaciones UML escapando los símbolos < y > con entidades HTML
dot.edge('UC1', 'UC2', label='&lt;&lt;include&gt;&gt;', style='dashed')
dot.edge('UC3', 'UC1', label='&lt;&lt;extend&gt;&gt;', style='dashed')

# Generar y renderizar
dot.render('diagrama_casos_de_uso', view=True)
print('¡Diagrama generado exitosamente!')