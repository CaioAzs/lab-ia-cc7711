# pip install opencv-python matplotlib
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Carregar imagem e converter para RGB
img = cv2.imread('./images/Girafa.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Converter para escala de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Threshold binário invertido com base no valor máximo
a = img_gray.max()
_, thresh = cv2.threshold(img_gray, a / 2 * 1.7, a, cv2.THRESH_BINARY_INV)

# Aplicar gradiente morfológico
tamanhoKernel = 15
kernel = np.ones((tamanhoKernel, tamanhoKernel), np.uint8)
img_grad = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)

# Encontrar contornos
contours, hierarchy = cv2.findContours(
    image=img_grad,
    mode=cv2.RETR_TREE,
    method=cv2.CHAIN_APPROX_SIMPLE
)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Desenhar contornos na imagem
img_copy = img.copy()
final = cv2.drawContours(img_copy, contours, -1, (255, 0, 0), 2)

fig1 = plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.imshow(img)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(thresh, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(img_grad, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(final)
plt.axis('off')

plt.tight_layout()

# Salvar plot com todos os passos
# fig1.savefig("Passo_a_Passo.png", dpi=300)
plt.show()

# Novo plot: imagem final grande
fig2 = plt.figure(figsize=(10, 8))
plt.imshow(final)
plt.axis('off')
plt.tight_layout()
plt.show()

# Salvar imagem final com contornos
# cv2.imwrite("Final_Girafa.png", cv2.cvtColor(final, cv2.COLOR_RGB2BGR))
