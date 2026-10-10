import graphviz

# Definición del código DOT con los nodos, tiempos y dependencias
dot_code = """
digraph PERT {
    rankdir=LR;
    node [shape=none, margin=0, fontname="Helvetica,Arial,sans-serif"];
    edge [fontname="Helvetica,Arial,sans-serif", fontsize=10];

    // Nodos secuenciales iniciales
    N1 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>1</B></TD></TR><TR><TD>0</TD><TD>0</TD></TR></TABLE>>];
    N2 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>2</B></TD></TR><TR><TD>2</TD><TD>2</TD></TR></TABLE>>];
    N3 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>3</B></TD></TR><TR><TD>4</TD><TD>4</TD></TR></TABLE>>];
    N4 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>4</B></TD></TR><TR><TD>6</TD><TD>6</TD></TR></TABLE>>];
    N5 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>5</B></TD></TR><TR><TD>9</TD><TD>9</TD></TR></TABLE>>];
    N6 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>6</B></TD></TR><TR><TD>11</TD><TD>11</TD></TR></TABLE>>];
    N7 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>7</B></TD></TR><TR><TD>14</TD><TD>14</TD></TR></TABLE>>];
    N8 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>8</B></TD></TR><TR><TD>18</TD><TD>18</TD></TR></TABLE>>];
    N9 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>9</B></TD></TR><TR><TD>21</TD><TD>21</TD></TR></TABLE>>];
    N10 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>10</B></TD></TR><TR><TD>23</TD><TD>23</TD></TR></TABLE>>];
    N11 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>11</B></TD></TR><TR><TD>27</TD><TD>27</TD></TR></TABLE>>];
    N12 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>12</B></TD></TR><TR><TD>29</TD><TD>29</TD></TR></TABLE>>];
    N13 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>13</B></TD></TR><TR><TD>32</TD><TD>32</TD></TR></TABLE>>];
    N14 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>14</B></TD></TR><TR><TD>36</TD><TD>36</TD></TR></TABLE>>];
    N15 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>15</B></TD></TR><TR><TD>40</TD><TD>40</TD></TR></TABLE>>];
    N16 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>16</B></TD></TR><TR><TD>43</TD><TD>43</TD></TR></TABLE>>];
    N17 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>17</B></TD></TR><TR><TD>47</TD><TD>47</TD></TR></TABLE>>];
    N18 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>18</B></TD></TR><TR><TD>51</TD><TD>51</TD></TR></TABLE>>];

    // Nodos de la primera bifurcación
    N19 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>19</B></TD></TR><TR><TD>54</TD><TD>54</TD></TR></TABLE>>];
    N20 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>20</B></TD></TR><TR><TD>54</TD><TD>54</TD></TR></TABLE>>];
    N21 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>21</B></TD></TR><TR><TD>54</TD><TD>54</TD></TR></TABLE>>];
    N22 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>22</B></TD></TR><TR><TD>54</TD><TD>54</TD></TR></TABLE>>];

    // Nodos de continuación
    N23 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>23</B></TD></TR><TR><TD>58</TD><TD>58</TD></TR></TABLE>>];
    N24 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>24</B></TD></TR><TR><TD>73</TD><TD>73</TD></TR></TABLE>>];
    N25 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>25</B></TD></TR><TR><TD>80</TD><TD>80</TD></TR></TABLE>>];

    // Nodos de la bifurcación final
    N26 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>26</B></TD></TR><TR><TD>83</TD><TD>83</TD></TR></TABLE>>];
    N27 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>27</B></TD></TR><TR><TD>83</TD><TD>85</TD></TR></TABLE>>];
    N28 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>28</B></TD></TR><TR><TD>85</TD><TD>85</TD></TR></TABLE>>];
    N29 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" STYLE="ROUNDED"><TR><TD COLSPAN="2"><B>29</B></TD></TR><TR><TD>85</TD><TD>85</TD></TR></TABLE>>];

    // Relaciones de tareas secuenciales iniciales (Ruta Crítica)
    N1 -> N2 [label=" 1 (2)", color="red", penwidth=2.0];
    N2 -> N3 [label=" 2 (2)", color="red", penwidth=2.0];
    N3 -> N4 [label=" 3 (2)", color="red", penwidth=2.0];
    N4 -> N5 [label=" 4 (3)", color="red", penwidth=2.0];
    N5 -> N6 [label=" 5 (2)", color="red", penwidth=2.0];
    N6 -> N7 [label=" 6 (3)", color="red", penwidth=2.0];
    N7 -> N8 [label=" 7 (4)", color="red", penwidth=2.0];
    N8 -> N9 [label=" 8 (3)", color="red", penwidth=2.0];
    N9 -> N10 [label=" 9 (2)", color="red", penwidth=2.0];
    N10 -> N11 [label=" 10 (4)", color="red", penwidth=2.0];
    N11 -> N12 [label=" 11 (2)", color="red", penwidth=2.0];
    N12 -> N13 [label=" 12 (3)", color="red", penwidth=2.0];
    N13 -> N14 [label=" 13 (4)", color="red", penwidth=2.0];
    N14 -> N15 [label=" 14 (4)", color="red", penwidth=2.0];
    N15 -> N16 [label=" 15 (3)", color="red", penwidth=2.0];
    N16 -> N17 [label=" 16 (4)", color="red", penwidth=2.0];
    N17 -> N18 [label=" 17 (4)", color="red", penwidth=2.0];

    // Bifurcación en paralelo Tareas 18, 19, 20 (Ruta Crítica)
    N18 -> N19 [label=" 18 (3)", color="red", penwidth=2.0];
    N18 -> N20 [label=" 19 (3)", color="red", penwidth=2.0];
    N18 -> N21 [label=" 20 (3)", color="red", penwidth=2.0];

    // Convergencia con Tareas Ficticias (Ruta Crítica)
    N19 -> N22 [label=" F (0)", style="dashed", color="red", penwidth=2.0];
    N20 -> N22 [label=" F (0)", style="dashed", color="red", penwidth=2.0];
    N21 -> N22 [label=" F (0)", style="dashed", color="red", penwidth=2.0];

    // Tareas Secuenciales 21 a 23 (Ruta Crítica)
    N22 -> N23 [label=" 21 (4)", color="red", penwidth=2.0];
    N23 -> N24 [label=" 22 (15)", color="red", penwidth=2.0];
    N24 -> N25 [label=" 23 (7)", color="red", penwidth=2.0];

    // Bifurcación Final
    N25 -> N26 [label=" 24 (3)", color="red", penwidth=2.0];
    N25 -> N27 [label=" 26 (3)"]; // Única tarea con holgura (No es crítica)
    N26 -> N28 [label=" 25 (2)", color="red", penwidth=2.0];

    // Cierre del diagrama con Tareas Ficticias
    N27 -> N29 [label=" F (0)", style="dashed"];
    N28 -> N29 [label=" F (0)", style="dashed", color="red", penwidth=2.0];
}
"""

# Inicializar y renderizar el gráfico
grafico = graphviz.Source(dot_code)

# render('nombre_del_archivo', formato='extension', view=True para abrirlo automáticamente)
grafico.render('diagrama_pert_proyecto', format='png', view=True)