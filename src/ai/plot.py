import matplotlib.pyplot as plt
from IPython import display

plt.ion()

# Inicializa la figura y el eje una vez
fig, ax = plt.subplots()

def Plot(scores, mean_scores):
    # Limpia la salida anterior
    display.clear_output(wait=True)
    
    # Limpia el eje actual
    ax.clear()

    # Configura el título y etiquetas del gráfico
    ax.set_title('Training...')
    ax.set_xlabel('Number of Games')
    ax.set_ylabel('Score')

    # Plotea los datos
    ax.plot(scores, label='Scores')
    ax.plot(mean_scores, label='Mean Scores')

    # Configura límites y texto en el gráfico
    ax.set_ylim(ymin=0)
    ax.text(len(scores)-1, scores[-1], str(scores[-1]))
    ax.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))

    # Muestra la leyenda
    ax.legend()

    # Muestra el gráfico sin bloquear el código
    display.display(fig)
    plt.pause(0.1)