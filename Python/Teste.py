from datetime import datetime
class Livro:
    livro = []
    def __init__(self,titulo, autor, ano_publicacao, disponivel = True):
        ano_atual = datetime.now().year
        if isinstance(ano_publicacao, int) and 1000 <= ano_publicacao <= ano_atual:
            self._titulo  = titulo.title()
            self._autor = autor.title()
            self._ano_publicacao = ano_publicacao
            self._disponivel = disponivel
        else:
            raise ValueError(f"O ano de publicação deve ser um número inteiro de 4 dígitos e não pode ser maior que {ano_atual}.")
    @property
    def disponivel(self):
        return '✅'if self._disponivel else '❌'
    
livro_Tiago = Livro('Tiago','Tiago', 2000)

print(f'Nome do Livro: {livro_Tiago._titulo}, Autor: {livro_Tiago._autor}, Ano de Publicação: {livro_Tiago._ano_publicacao}, Disponível: {livro_Tiago.disponivel}')