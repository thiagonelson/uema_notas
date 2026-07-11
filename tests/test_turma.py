from notas.aluno import Aluno
from notas.turma import Turma


def test_criar_turma():
    turma = Turma("Matematica")
    assert turma.nome_disciplina == "Matematica"
    assert turma.alunos == []


def test_adicionar_aluno():
    turma = Turma("Historia")
    aluno = Aluno("Maria", "2024001")

    turma.adicionar_aluno(aluno)

    assert turma.total_alunos() == 1


def test_listar_aprovados():
    turma = Turma("Ciencias")

    aluno1 = Aluno("Ana", "2024002")
    aluno1.adicionar_nota(8.0)

    aluno2 = Aluno("Beto", "2024003")
    aluno2.adicionar_nota(3.0)

    turma.adicionar_aluno(aluno1)
    turma.adicionar_aluno(aluno2)

    aprovados = turma.listar_aprovados()

    assert len(aprovados) == 1
    assert aprovados[0].nome == "Ana"


def test_media_da_turma():
    turma = Turma("Portugues")

    aluno1 = Aluno("Carla", "2024004")
    aluno1.adicionar_nota(6.0)

    aluno2 = Aluno("Diego", "2024005")
    aluno2.adicionar_nota(8.0)

    turma.adicionar_aluno(aluno1)
    turma.adicionar_aluno(aluno2)

    assert turma.media_da_turma() == 7.0


def test_melhor_aluno():
    turma = Turma("Fisica")

    aluno1 = Aluno("Eduarda", "2024006")
    aluno1.adicionar_nota(6.0)

    aluno2 = Aluno("Felipe", "2024007")
    aluno2.adicionar_nota(9.0)

    turma.adicionar_aluno(aluno1)
    turma.adicionar_aluno(aluno2)

    melhor = turma.melhor_aluno()

    assert melhor.nome == "Felipe"


def test_turma_vazia_media():
    turma = Turma("Quimica")
    assert turma.media_da_turma() == 0.0


def test_turma_vazia_melhor_aluno():
    turma = Turma("Biologia")
    assert turma.melhor_aluno() is None