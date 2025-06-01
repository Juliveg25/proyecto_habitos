import pytest
import admin_registros

@pytest.fixture
def test_guardar_puntajes():
    admin_registros.guardar_puntajes(10)
    assert admin_registros.ver_historial() == 10

def test_borrar_registro():
    historial_puntajes = [10, 20, 30]  # ejemplo de lista de puntajes
    assert admin_registros.borrar_registro(historial_puntajes) == []

def test_ver_historial():
    #ver_historial solo recibe valores tipo Array
    historial = []
    historial.append(500)
    admin_registros.ver_historial(historial)
    assert admin_registros.ver_historial(historial) == 500


