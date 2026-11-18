from src.mini_biblioteca import Usuario,Emprestimo,Livro

usuario=Usuario("Carlos",555)
livro=Livro("1984","George Orwell",5555)
emprestimo=Emprestimo(usuario,livro)

print(livro.titulo,livro.autor,livro.codigo,livro.disponivel)
emprestimo.devolver(livro)
print(livro.titulo,livro.autor,livro.codigo,livro.disponivel)
