<H1> Caio de Souza Conceição - RA: 22.122.033-8 </H1>
<H1> Lucas Dias Batista - RA: 22.122.065-0 </H1>

---

## Funções de Pertinência Utilizadas
Foram utilizadas três variáveis de entrada com diferentes funções de pertinência:

- **Dieta**: Função triangular com categorias 'ruim', 'media' e 'boa'.
- **Atividade Física**: Função gaussiana com categorias 'baixa', 'moderada' e 'alta'.
- **Peso**: Função trapezoidal com categorias 'baixo', 'normal' e 'alto'.

## Testes Realizados
Foram realizados testes com as variáveis definidas da seguinte forma:

- **Dieta = 7**
- **Atividade Física = 7**
- **Peso = 70kg**

### Resultados dos Testes com Diferentes Métodos de Cálculo:
- **Trapezoidal**: Obesidade calculada = 52.33

![Image](https://github.com/user-attachments/assets/04c00a3c-a14c-4886-9a87-5e5bf78429ac)

- **Triangular**: Obesidade calculada = 38.82

![Image](https://github.com/user-attachments/assets/5c5f545e-b514-4bb5-b519-8ce30aab40f2)

- **Gaussiano**: Obesidade calculada = 43.77

![Image](https://github.com/user-attachments/assets/cc11e939-7f53-4ace-8d3e-85192e863b67)

---

## Análise de Sensibilidade
Durante os testes, observou-se que:

- Um aumento na qualidade da dieta e na intensidade da atividade física reduz significativamente o nível de obesidade.
- O peso tem uma influência direta e proporcional no resultado. Valores mais altos de peso resultam em maiores índices de obesidade, independentemente das outras variáveis.

## Exploração dos Valores Limites
Ao testar valores extremos, os seguintes resultados foram observados:

- **Dieta = 0**, **Atividade = 0**, **Peso = 150**: Resultado de obesidade muito elevado.
- **Dieta = 10**, **Atividade = 10**, **Peso = 30**: Resultado de obesidade muito baixo.

## Inclusão de Nova Variável e Regras
Uma nova variável chamada **Tempo de Atividade Física** foi adicionada para refinar a análise. As regras foram ajustadas para incluir cenários onde uma maior frequência de exercícios impacta diretamente na redução dos níveis de obesidade.

## Experiência e Outras Aplicações
O desenvolvimento desse sistema ajudou a entender como a lógica fuzzy funciona na prática. Além disso, o sistema pode ser utilizado em outras áreas, como na climatização, ajustando automaticamente a temperatura de ambientes com base em variáveis como temperatura externa, número de pessoas e horário. Isso mostra como a lógica fuzzy pode ser útil para resolver problemas quantitativos.