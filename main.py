
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os cinco níveis do reservatorio
niveis = [
    "Nivel 1 - Muito baixo (CRITICO)",
    "Nivel 2 - Baixo",
    "Nivel 3 - Medio",
    "Nivel 4 - Alto",
    "Nivel 5 - Muito alto (ALERTA)"
]


# Funcao que define a cor de cada nivel
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Exibe a situacao atual do reservatorio
def monitorar_reservatorio(nivel):
    if nivel < 1 or nivel > len(niveis):
        print(Fore.WHITE + "Nivel invalido!" + Style.RESET_ALL)
        return

    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)


# Simulacao dos niveis do reservatorio
print("=== MONITORAMENTO DO RESERVATORIO ===")

for nivel_atual in range(1, 6):
    monitorar_reservatorio(nivel_atual)
