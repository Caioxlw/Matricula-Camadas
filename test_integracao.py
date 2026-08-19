import unittest
import subprocess
import os

class TestMatriculaIntegracao(unittest.TestCase):
    def setUp(self):
        # Remove o banco de dados antes de cada teste para garantir um estado limpo
        if os.path.exists("escola.db"):
            os.remove("escola.db")

    def tearDown(self):
        # Limpa o banco após o teste
        if os.path.exists("escola.db"):
            os.remove("escola.db")

    def test_sequencia_principal(self):
        entrada = (
            "1\n"          # Matricular
            "42, ES2\n"    # Ana, Eng de Software II
            "1\n"          # Matricular
            "42, ES2\n"    # Ana, Eng de Software II (de novo)
            "1\n"          # Matricular
            "43, ES2\n"    # Bruno (4 faltas), Eng de Software II
            "1\n"          # Matricular
            "42, AS1\n"    # Ana, Arq de Software (0 vagas)
            "2\n"          # Listar
            "42\n"         # Matriculas de Ana
            "3\n"          # Cancelar expiradas
            "4\n"          # Sair
        )

        # Se os alunos renomearem o arquivo principal, basta mudar aqui:
        arquivo_principal = "matricula_monolito.py"

        resultado = subprocess.run(
            ["python3", arquivo_principal],
            input=entrada,
            text=True,
            capture_output=True
        )

        # Verifica se o programa executou com sucesso (código 0)
        self.assertEqual(resultado.returncode, 0, f"O programa falhou com erro:\n{resultado.stderr}")

        saida = resultado.stdout
        
        # 1. Matricular Ana em ES2 (Sucesso)
        self.assertIn(
            "Matricula de Ana Ribeiro em Engenharia de Software II confirmada. Pague ate", 
            saida,
            "Falha ao matricular Ana Ribeiro em ES2 com sucesso."
        )
        
        # 2. Tentar matricular Ana em ES2 novamente (Já matriculado)
        self.assertIn(
            "Ana Ribeiro ja esta matriculado em Engenharia de Software II", 
            saida,
            "Falha na validacao de matricula duplicada."
        )
        
        # 3. Tentar matricular Bruno em ES2 (Barrado por faltas)
        self.assertIn(
            "Bruno Lima tem 4 faltas e nao pode se matricular", 
            saida,
            "Falha na validacao do limite de faltas."
        )
        
        # 4. Tentar matricular Ana em AS1 (Sem vagas)
        self.assertIn(
            "Sem vagas em Arquitetura de Software", 
            saida,
            "Falha na validacao de vagas da turma."
        )
        
        # 5. Listar matrículas da Ana
        self.assertIn(
            "Matriculas do aluno 42:", 
            saida,
            "Falha ao listar as matriculas da Ana (cabecalho)."
        )
        self.assertIn(
            "- ES2 (Engenharia de Software II) — aguardando pagamento ate", 
            saida,
            "Falha ao listar a turma ES2 para a Ana."
        )
        
        # 6. Cancelar expiradas (0 expiradas, pois acabou de ser criada)
        self.assertIn(
            "0 matricula(s) expirada(s) cancelada(s)", 
            saida,
            "Falha ao rodar cancelamento de expiradas."
        )

if __name__ == "__main__":
    unittest.main()
