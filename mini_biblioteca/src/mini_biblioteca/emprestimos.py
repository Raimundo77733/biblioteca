class Emprestimo:
    def __init__(self,usuario,livro):
        self.livro=livro
        self.usuario=usuario
        self.ativo=True
        if livro.disponivel==False:raise ValueError
        else:livro.disponivel=False
    
    def devolver(self,livro):
        self.ativo=False
        livro.disponivel=True
        return True

