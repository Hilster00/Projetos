class Aluno:
    def __init__(self,nome,sexo,notas):
        self.nome=nome
        self.sexo=sexo
        self.notas=notas
    @property
    def notas(self):
        self._notas=notas
    def notas(self):
        return self._notas
        
class Turma:
    def __init__(self,nome):
        self.nome=nome
        self.alunos=list()
        
    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)
    
    def lista_alunos(self):
        return self.alunos
        
    def remover_aluno(self,aluno):
        self.alunos.remove(aluno)
        
    def quantidade_alunos(self):
        return len(self.alunos)
