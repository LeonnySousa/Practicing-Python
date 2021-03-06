from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade : int = int(input('Informe o Nivel de dificuldade desejado [1, 2, 3, 4]:'))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação:')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos')

    continuar: int = int(input('Deseja Continuar? [1 - sim, 0 - não]:'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Voce finalizou com {pontos}')
        print('Até a próxima!!')


if __name__ == '__main__':
    main()
