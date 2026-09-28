# Apuntes-Ciencia-de-Datos

Apuntes y talleres para el curso de competencias en ciencia de datos, centrados en redes neuronales: desde el perceptrón y el descenso del gradiente hasta redes densas, CNN y transferencia de aprendizaje.

## Contenido

### [`Perceptron/`](Perceptron/)
Fundamentos del perceptrón, descenso del gradiente y funciones de activación (ver [Perceptron/Readme.md](Perceptron/Readme.md)), y cuadernos de práctica:
- `Avanzada_Cuaderno_1_ANN_El_Perceptron.ipynb` — anatomía del perceptrón y regla de ajuste clásica.
- `Cuanderno_1_1_Perceptron_con_Sklearn_ipynb (1).ipynb` — perceptrón con scikit-learn.
- `Avanzada_Cuaderno_2_ANN_Red_Neuronal_sklearn_keras_tensorflow.ipynb` — comparativa sklearn / Keras / TensorFlow.
- `Circulos.ipynb` y `Practica_de_redes_neuronales_densas.ipynb` — clasificación no lineal con redes densas (MLP).
- `Avanzada_Cuaderno_5B_Taller_aplicado_ANN_Predicción_de_la_eficiencia_de_la_gasolina.ipynb` — taller aplicado de regresión (ANN).
- `Avanzada Cuaderno 6 CNN Procesamiento digital de imágenes.ipynb` — introducción a CNN y procesamiento de imágenes.
- `Cuaderno_7_Redes_Neuronales_Convolucionales_CNN.ipynb` — arquitectura y entrenamiento de una CNN.
- `Avanzada Cuaderno 8 CNN Transferencia de aprendizaje.ipynb` — transfer learning sobre modelos preentrenados.
- Modelos entrenados incluidos: `fashion_mnist_model.keras`, `modelo_mlp_circulos.joblib`, `primermillon.joblib`.

### [`Redes densas/`](Redes%20densas/)
Modelos secuenciales en TensorFlow/Keras (ver [Redes densas/Readme.md](Redes%20densas/Readme.md)):
- `Avanzada_Cuaderno_3_ANN_Red_neuronal_básica_de_regresion_lineal_Ejemplo.ipynb` — regresión lineal con una sola neurona (ej. Celsius → Fahrenheit).
- `Avanzada_Cuaderno_4_ANN_Red_Neuronal_Clasificación_(Redes_densas).ipynb` — clasificación con MLP, funciones de pérdida, batch size y early stopping.

### [`convoluciones-main/`](convoluciones-main/)
Demo en JavaScript de convoluciones y filtros de imagen en el navegador (imagen estática y cámara web). Requiere servirse desde un servidor local por restricciones del canvas:
```bash
cd convoluciones-main
python -m http.server 8000
# abrir http://localhost:8000/imagen.html o /camara.html
```

### [`taller/`](taller/)
Taller aplicado con app interactiva en Streamlit para clasificar prendas (Fashion-MNIST) por dibujo, cámara o imagen cargada:
- `app.py` — aplicación Streamlit (`fashion_mnist_modelo.keras`).
- `huevos.py`, `procesamiento.py` — scripts de procesamiento de imágenes con OpenCV.
- `Avanzada_Cuaderno_5B_...ipynb` — mismo taller de eficiencia de gasolina que en `Perceptron/`.
- `pacientes.csv`, `datos_procesados.json` — datos de ejemplo.

Para ejecutar la app:
```bash
cd taller
pip install -r requirements.txt
streamlit run app.py
```

### [`imagenes/`](imagenes/)
Recursos gráficos (diagramas del perceptrón, gradiente, funciones de activación) referenciados desde los distintos `README.md`, más un cuaderno introductorio a Keras.

## Requisitos generales

- Python 3.12+
- `tensorflow`, `keras`, `numpy`, `matplotlib`, `scikit-learn`
- Jupyter o Google Colab para los cuadernos `.ipynb`
