import pytest
from src.calculadora import somar, subtrair, multiplicar, dividir, potencia, eh_par


class TestSomar:
    def test_soma_positivos(self):
        assert somar(2, 3) == 5

    def test_soma_negativos(self):
        assert somar(-2, -3) == -5

    def test_soma_com_zero(self):
        assert somar(5, 0) == 5

    def test_soma_floats(self):
        assert somar(1.5, 2.5) == 4.0


class TestSubtrair:
    def test_subtracao_simples(self):
        assert subtrair(10, 4) == 6

    def test_subtracao_resulta_negativo(self):
        assert subtrair(3, 10) == -7


class TestMultiplicar:
    def test_multiplicacao_simples(self):
        assert multiplicar(3, 4) == 12

    def test_multiplicacao_por_zero(self):
        assert multiplicar(5, 0) == 0

    def test_multiplicacao_negativos(self):
        assert multiplicar(-2, 3) == -6


class TestDividir:
    def test_divisao_simples(self):
        assert dividir(10, 2) == 5

    def test_divisao_resulta_float(self):
        assert dividir(7, 2) == 3.5

    def test_divisao_por_zero_levanta_excecao(self):
        with pytest.raises(ValueError, match="Não é possível dividir por zero"):
            dividir(10, 0)


class TestPotencia:
    def test_potencia_simples(self):
        assert potencia(2, 3) == 8

    def test_potencia_zero(self):
        assert potencia(5, 0) == 1

    def test_potencia_um(self):
        assert potencia(7, 1) == 7


class TestEhPar:
    def test_numero_par(self):
        assert eh_par(4) is True

    def test_numero_impar(self):
        assert eh_par(7) is False

    def test_zero_eh_par(self):
        assert eh_par(0) is True
