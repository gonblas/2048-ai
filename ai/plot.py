import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def Plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()

    # Plotear las puntuaciones y puntuaciones promedio
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores, label='Scores')
    plt.plot(mean_scores, label='Mean Scores')

    # Configuración adicional del gráfico
    plt.ylim(ymin=0)

    # Agregar texto con el último puntaje y el puntaje máximo
    plt.text(len(scores)-1, scores[-1], f'Last Score: {scores[-1]}')
    max_score = max(scores)
    plt.text(len(scores)-1, max_score, f'Max Score: {max_score}')

    # Mostrar leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show(block=False)
    plt.pause(.1)
