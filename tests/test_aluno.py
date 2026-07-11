import pytest
from notas.aluno import Aluno


# ── Testes ja existentes ──────────────────────────────────────────────────

def test_criar_aluno():
    aluno = Aluno("Maria Silva", "2024001")
    assert aluno.nome == "Maria Silva"
    assert aluno.matricula == "2024001"
    assert aluno.notas == []


def test_adicionar_nota_valida():
    aluno = Aluno("Joao Santos", "2024002")
    aluno.adicionar_nota(8.0)
    assert 8.0 in aluno.notas


def test_adicionar_nota_invalida_acima_de_10():
    aluno = Aluno("Ana Costa", "2024003")
    with pytest.raises(ValueError):
        aluno.adicionar_nota(11.0)


def test_calcular_media_com_duas_notas():
    aluno = Aluno("Pedro Lima", "2024004")
    aluno.adicionar_nota(6.0)
    aluno.adicionar_nota(8.0)
    assert aluno.calcular_media() == 7.0


# ── Novos testes ──────────────────────────────────────────────────────────

def test_adicionar_nota_zero():
    aluno = Aluno("Carlos", "2024005")
    aluno.adicionar_nota(0)
    assert 0 in aluno.notas


def test_adicionar_nota_negativa():
    aluno = Aluno("Carlos", "2024006")
    with pytest.raises(ValueError):
        aluno.adicionar_nota(-1)


def test_calcular_media_sem_notas():
    aluno = Aluno("Carlos", "2024007")
    assert aluno.calcular_media() == 0.0


def test_aprovado_media_maior_que_cinco():
    aluno = Aluno("Carlos", "2024008")
    aluno.adicionar_nota(6.0)
    assert aluno.aprovado() is True


def test_aprovado_media_igual_a_cinco():
    aluno = Aluno("Carlos", "2024009")
    aluno.adicionar_nota(5.0)
    assert aluno.aprovado() is True


def test_situacao_aprovado():
    aluno = Aluno("Carlos", "2024010")
    aluno.adicionar_nota(8.0)
    assert aluno.situacao() == "Aprovado"


def test_situacao_reprovado():
    aluno = Aluno("Carlos", "2024011")
    aluno.adicionar_nota(3.0)
    assert aluno.situacao() == "Reprovado"


def test_str_aluno():
    aluno = Aluno("Maria", "2024001")
    aluno.adicionar_nota(8.0)

    texto = str(aluno)

    assert texto == (
        "Aluno: Maria | Matricula: 2024001 | "
        "Media: 8.0 | Situacao: Aprovado"
    )