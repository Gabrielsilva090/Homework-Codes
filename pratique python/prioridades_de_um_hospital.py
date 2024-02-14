def organizar_fila_pacientes(N, pacientes):
    prioridades_planos = {'premium': 6, 'diamante': 5, 'ouro': 4, 'prata': 3, 'bronze': 2, 'resto': 1}

    pacientes_ordenados = sorted(pacientes, key=lambda x: (prioridades_planos[x[1]], x[2], x[0]))

    pacientes_ordenados.reverse()

    for paciente in pacientes_ordenados:
        print(paciente[0])


N = int(input())
pacientes = [input().split() for _ in range(N)]
pacientes = [(nome, plano, int(gravidade)) for nome, plano, gravidade in pacientes]

organizar_fila_pacientes(N, pacientes)