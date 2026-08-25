from persistence.consultas import (
    consultarTurma, 
    consultarAluno, 
    verificarMatricula,
    salvarMatricula,
    LIMITE_FALTAS
    )

def matricular(entrada_usuario):
    """Recebe o texto digitado no formulário, valida, aplica as regras e grava."""
    partes = [p.strip() for p in entrada_usuario.split(",")]
    if len(partes) != 2:
        print("Formato invalido. Use: <id do aluno>, <codigo da turma>")
        return None
    if not partes[0].isdigit():
        print("O id do aluno precisa ser um numero")
        return None
    aluno_id = int(partes[0])
    turma = partes[1].upper()
    if (consultarAluno(aluno_id) is not None) and (verificarMatricula(aluno_id, turma) is not None) and(consultarTurma(turma) is not None):   
        if consultarAluno(aluno_id)[1] >= LIMITE_FALTAS:
            print("%s tem %d faltas e nao pode se matricular" % (consultarAluno(aluno_id)[0], consultarAluno(aluno_id)[1]))
            return None
        if consultarTurma(turma)[1] <= 1:
            print("Sem vagas em %s" % consultarTurma(turma)[0])
        salvarMatricula(aluno_id, turma)
        
        
    
