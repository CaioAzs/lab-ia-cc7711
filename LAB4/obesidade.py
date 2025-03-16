import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variáveis de entrada (Antecedents)
dieta = ctrl.Antecedent(np.arange(0, 11, 1), 'dieta')
atividade = ctrl.Antecedent(np.arange(0, 11, 1), 'atividade')
peso = ctrl.Antecedent(np.arange(30, 151, 1), 'peso')

# Variável de saída (Consequent)
obesidade = ctrl.Consequent(np.arange(0, 101, 1), 'obesidade')

# Atribuição automática de categorias (automf) para as variáveis de entrada
dieta.automf(names=['ruim', 'media', 'boa'])
atividade.automf(names=['baixa', 'moderada', 'alta'])
peso.automf(names=['baixo', 'normal', 'alto'])

# # Método Triangular
# obesidade['baixa'] = fuzz.trimf(obesidade.universe, [0, 0, 50])
# obesidade['media'] = fuzz.trimf(obesidade.universe, [25, 50, 75])
# obesidade['alta'] = fuzz.trimf(obesidade.universe, [50, 100, 100])

# # Método Gaussiano
# obesidade['baixa'] = fuzz.gaussmf(obesidade.universe, 0, 10)
# obesidade['media'] = fuzz.gaussmf(obesidade.universe, 50, 15)
# obesidade['alta'] = fuzz.gaussmf(obesidade.universe, 100, 15)

# Método Trapezoidal
obesidade['baixa'] = fuzz.trapmf(obesidade.universe, [0, 0, 25, 50])
obesidade['media'] = fuzz.trapmf(obesidade.universe, [25, 50, 75, 100])
obesidade['alta'] = fuzz.trapmf(obesidade.universe, [75, 100, 100, 100])

# Visualizando as variáveis de entrada
dieta.view()
atividade.view()
peso.view()
obesidade.view()

# Criando as regras
rule1 = ctrl.Rule(dieta['boa'] & atividade['alta'] & peso['baixo'], obesidade['baixa'])
rule2 = ctrl.Rule(dieta['media'] & atividade['moderada'] & peso['normal'], obesidade['media'])
rule3 = ctrl.Rule(dieta['ruim'] & atividade['baixa'] & peso['alto'], obesidade['alta'])

# Sistema de controle
obesidade_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Simulação
obesidade_sim = ctrl.ControlSystemSimulation(obesidade_ctrl)

dieta_input = float(input("Informe o nível da dieta (0-10): "))
atividade_input = float(input("Informe o nível da atividade física (0-10): "))
peso_input = float(input("Informe o peso (30-150 kg): "))

obesidade_sim.input['dieta'] = dieta_input
obesidade_sim.input['atividade'] = atividade_input
obesidade_sim.input['peso'] = peso_input

try:
    obesidade_sim.compute()
    print(f"\nDieta: {dieta_input}\nAtividade Física: {atividade_input}\nPeso: {peso_input}\nObesidade calculada: {obesidade_sim.output['obesidade']:.2f}")
except KeyError:
    print("Erro: A saída 'obesidade' não foi calculada corretamente.")

dieta.view(sim=obesidade_sim)
atividade.view(sim=obesidade_sim)
peso.view(sim=obesidade_sim)
obesidade.view(sim=obesidade_sim)

plt.show()
