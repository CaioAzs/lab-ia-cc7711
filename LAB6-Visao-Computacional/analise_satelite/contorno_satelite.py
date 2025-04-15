# pip install opencv-python matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar imagem
img = cv2.imread('./images/Satelite.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# TONS DE CINZA
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Aplicar blur
blur = cv2.GaussianBlur(gray, (7, 7), 0)

# BORDAS
edges = cv2.Canny(blur, 50, 150)

# Dilatação
kernel = np.ones((3, 3), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)

# Encontrar contornos
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtrar por área mínima
min_area = 8000
filtered = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

# Desenhar contornos
img_final = img.copy()
cv2.drawContours(img_final, filtered, -1, (0, 0, 255), 2)

fig1 = plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.imshow(img)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(blur, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(dilated, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(img_final)
plt.axis('off')

plt.tight_layout()

# Salvar plot com todos os passos
# fig1.savefig("Passo_a_Passo.png", dpi=300)
plt.show()

# Novo plot: imagem final grande
fig2 = plt.figure(figsize=(10, 8))
plt.imshow(img_final)
plt.axis('off')
plt.tight_layout()
plt.show()

# Salvar imagem final com contornos
# cv2.imwrite("Final_Satelite.png", cv2.cvtColor(img_final, cv2.COLOR_RGB2BGR))
