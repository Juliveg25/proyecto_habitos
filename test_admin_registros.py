import pytest
import admin_registros

@pytest.fixture
def test_guardar_puntajes():
    admin_registros.guardar_puntajes(10)
    assert admin_registros.ver_historial() == 10

def test_borrar_registro():
    historial_puntajes = [10, 20, 30]  # ejemplo de lista de puntajes
    assert admin_registros.borrar_registro(historial_puntajes) == []

