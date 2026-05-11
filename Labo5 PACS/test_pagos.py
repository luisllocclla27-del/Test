import pytest
from unittest.mock import MagicMock
from pagos import ProcesadorPagos, PasarelaExterna

def test_pago_exitoso_dentro_de_limites():
    # 1. ARRANGE
    mock_pasarela = MagicMock()
    mock_pasarela.autorizar.return_value = True
    procesador = ProcesadorPagos(mock_pasarela)

    # 2. ACT
    exito, mensaje = procesador.procesar_transaccion(100)

    # 3. ASSERT
    assert exito is True
    mock_pasarela.autorizar.assert_called_once()

def test_pago_rechazado_por_limite_excedido():
    # Arrange
    mock_pasarela = MagicMock()
    procesador = ProcesadorPagos(mock_pasarela)

    # Act: 1000 * 1.18 = 1180 (Excede el límite de 1000)
    exito, mensaje = procesador.procesar_transaccion(1000)

    # Assert
    assert exito is False
    assert mensaje == "Excede límite diario"
    
    
    
    