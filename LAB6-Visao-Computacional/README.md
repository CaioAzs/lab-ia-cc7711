<H1> Caio de Souza Conceição - RA: 22.122.033-8 </H1>
<H1> Lucas Dias Batista - RA: 22.122.065-0 </H1>

---

# Avião

![Image](https://github.com/user-attachments/assets/c0b7911d-5545-49a8-a52c-a3fea53f6ae5)

1. **Conversão para tons de cinza**: A imagem é convertida para escala de cinza para simplificar a detecção de bordas.
2. **Aplicação de borramento (blur)**: Um filtro Gaussiano é aplicado para reduzir o ruído da imagem antes da detecção de bordas.
3. **Detecção de bordas (Canny)**: O método Canny é usado para identificar as bordas da imagem.
4. **Dilatação**: A operação morfológica de dilatação expande as bordas detectadas, melhorando a definição dos contornos.
5. **Detecção de contornos**: Os contornos são encontrados a partir da imagem dilatada.
6. **Filtragem por área mínima**: Apenas contornos com área superior a um valor mínimo são mantidos.

# Girafa

![Image](https://github.com/user-attachments/assets/ca176580-b3a1-4244-b2fc-85305bf27a2f)

1. **Conversão para tons de cinza**: A imagem é convertida para escala de cinza para simplificar o processamento.
2. **Threshold binário invertido**: Um limiar é aplicado para inverter a imagem.
3. **Aplicação de gradiente morfológico**: Um gradiente morfológico é aplicado para destacar as bordas.
4. **Detecção de contornos**: Os contornos são encontrados a partir da imagem resultante do gradiente.
5. **Ordenação dos contornos**: Os contornos são ordenados por área, do maior para o menor.

# Satélite

![Image](https://github.com/user-attachments/assets/3ac2cf7a-93ab-43d1-9b34-30bf75637490)

1. **Conversão para tons de cinza**: A imagem é convertida para escala de cinza para simplificar a detecção de bordas.
2. **Aplicação de borramento (blur)**: Um filtro Gaussiano é aplicado para suavizar a imagem e reduzir o ruído.
3. **Detecção de bordas (Canny)**: O método Canny é utilizado para detectar bordas na imagem.
4. **Dilatação**: A operação de dilatação é aplicada para expandir as bordas detectadas, tornando-as mais visíveis.
5. **Detecção de contornos**: Contornos são identificados na imagem dilatada.
6. **Filtragem por área mínima**: Apenas contornos com área maior que um valor mínimo são mantidos.

Para executar os arquivos .py, entre na pasta LAB6: cd .\LAB6-Visao-Computacional\
As imagens com o passo a passo e a imgem final de cada contorno estão nas pastas de análise.
Os comandos para salvar as imagens como png estão comentados, pois já foram gerados.