
import matplotlib.pyplot as plt


def create_graphic(df):
    # Calcular el precio promedio
    precio_promedio = df['Precio'].mean()

    # Crear un gráfico de dispersión con valores x e y
    x = range(len(df))
    y = df['Precio']

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.5)
    plt.axhline(precio_promedio, color='red', linestyle='--', label='Precio Promedio')
    plt.title('Variación de Precios de los Artículos')
    plt.xlabel('Artículos')
    plt.ylabel('Precio (en pesos)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Guardar el gráfico como un archivo PDF
    plt.savefig('grafico_dispersión.pdf', format='pdf')

    # Mostrar un mensaje de confirmación
    print("Gráfico de dispersión guardado como 'grafico_dispersión.pdf'")
