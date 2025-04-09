from InquirerPy import inquirer

def escolher_categoria():
    categorias = ["Japonesa", "Brasileira", "Italiana", "Mexicana", "Árabe"]
    categoria_escolhida = inquirer.select(
        message="Escolha a categoria do restaurante:",
        choices=categorias,
        default=categorias[0]  # opcional
    ).execute()

    print(f"Categoria escolhida: {categoria_escolhida}")
    return categoria_escolhida
