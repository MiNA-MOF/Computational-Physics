# test_lorenz.py
from lorenz import lorenz_derivatives

def test_equilibrium_point():
    """Testuje, czy w punkcie (0,0,0) system jest stabilny (pochodne = 0)."""
    state = [0.0, 0.0, 0.0]
    derivatives = lorenz_derivatives(state, 0)
    assert derivatives == [0.0, 0.0, 0.0]

def test_symmetry():
    """Testuje symetrię układu (zmiana znaku x i y nie powinna zmieniać dz/dt)."""
    res1 = lorenz_derivatives([1, 1, 1], 0)
    res2 = lorenz_derivatives([-1, -1, 1], 0)
    assert res1[2] == res2[2] # dz/dt powinno być takie samo