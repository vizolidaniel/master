from config import *
from random import randrange, uniform

class Produto(db.Model):
    # atributos do produto
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    codBarras = db.Column(db.Integer())
    preco = db.Column(db.Float(4))

    # método para expressar o produto em forma de texto
    def __str__(self):
        return f'(id={self.id}) {self.nome}, '+\
               f'{self.codBarras}, {self.preco}'

# teste da classe
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Produto
    p1 = Produto( nome = "prod1", codBarras = randrange(100,200), preco = uniform(1.0,4.0))
    p2 = Produto( nome = "prod2", codBarras = randrange(100,200), preco = uniform(1.0,4.0))        
    
    # persistir
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    
    # exibir o produto
    print(p1,p2)