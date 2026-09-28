import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

def create_realistic_cracks(image_path, output_path):
    # Cargar la imagen y crear una máscara alfa para manejar transparencias
    original_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if original_image is None:
        print(f"Error al cargar la imagen: {image_path}")
        return

    height, width, channels = original_image.shape
    # Crear una imagen transparente del mismo tamaño
    cracked_layer = np.zeros((height, width, 4), dtype=np.uint8)

    # --- Generación de Grietas ---
    # Generar un patrón de ruido perlin o Voronoi simulado para grietas
    # Usaremos un enfoque basado en distancias aleatorias para un efecto de grieta orgánica.
    for _ in range(random.randint(1, 3)): # 1 a 3 centros de impacto
        center_x = random.randint(width//3, width*2//3)
        center_y = random.randint(height//3, height*2//3)
        num_branches = random.randint(12, 25)
        for _ in range(num_branches):
            branch_len = random.randint(50, max(width, height)//1)
            angle = random.uniform(0, 2 * np.pi)
            branch_nodes = []
            curr_x, curr_y = center_x, center_y
            for _ in range(branch_len):
                # Movimiento aleatorio con tendencia hacia afuera
                angle += random.uniform(-0.2, 0.2)
                dist = random.uniform(0.5, 5)
                curr_x += np.cos(angle) * dist
                curr_y += np.sin(angle) * dist
                # Deformar ligeramente la grieta
                branch_nodes.append((int(curr_x), int(curr_y)))
            
            # Dibujar la grieta con grosores variables
            # Primero un trazo muy fino y oscuro (la grieta profunda)
            prev_point = None
            for point in branch_nodes:
                thickness = random.randint(1, 2)
                color = (20, 20, 20, 255) # Color casi negro para el interior
                if prev_point:
                    cv2.line(cracked_layer, prev_point, point, color, thickness, cv2.LINE_AA)
                prev_point = point

            # Segundo, un trazo ligeramente más claro y grueso para el efecto de sombra
            prev_point = None
            for point in branch_nodes:
                thickness = random.randint(3, 5)
                color = (100, 100, 100, 150) # Gris semitransparente para la sombra
                if prev_point:
                    cv2.line(cracked_layer, prev_point, point, color, thickness, cv2.LINE_AA)
                prev_point = point
    
    # --- Procesamiento de Textura (Realismo) ---
    # Aplicar un desenfoque ligero a toda la capa de grietas
    cracked_layer_blurred = cv2.GaussianBlur(cracked_layer, (7, 7), 0)
    
    # --- Integración ---
    # Asegurarse de que la imagen original sea RGBA
    if channels == 3:
        original_rgba = cv2.cvtColor(original_image, cv2.COLOR_BGR2BGRA)
    else:
        original_rgba = original_image
        
    # Superponer la capa de grietas
    alpha_channel_mask = cracked_layer_blurred[:, :, 3] / 255.0
    for c in range(0, 3):
        original_rgba[:, :, c] = original_rgba[:, :, c] * (1 - alpha_channel_mask) + \
                                 cracked_layer_blurred[:, :, c] * alpha_channel_mask

    # Guardar la imagen resultante
    cv2.imwrite(output_path, original_rgba)
    return original_rgba, cracked_layer_blurred

# --- Ejecución de Ejemplo ---

# Procesar el huevo marrón
brown_egg_cracked, _ = create_realistic_cracks('image_0.png', 'brown_egg_cracked.png')

# Procesar el huevo blanco
white_egg_cracked, _ = create_realistic_cracked('image_1.png', 'white_egg_cracked.png')

# --- Visualización de los Resultados ---
plt.figure(figsize=(10, 5))

# Huevo Marrón
plt.subplot(1, 2, 1)
plt.title('Huevo Marrón Original vs. Agrietado')
plt.imshow(cv2.cvtColor(brown_egg_cracked, cv2.COLOR_BGRA2RGBA))
plt.axis('off')

# Huevo Blanco
plt.subplot(1, 2, 2)
plt.title('Huevo Blanco Original vs. Agrietado')
plt.imshow(cv2.cvtColor(white_egg_cracked, cv2.COLOR_BGRA2RGBA))
plt.axis('off')

plt.tight_layout()
plt.show()