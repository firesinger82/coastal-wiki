"""Check the transcribed linear solution, not ADCIRC or physical validity."""
from pathlib import Path
import cmath
import json
import math

g, r1, r2, h1 = 9.81, 60960.0, 152400.0, 3.048
omega, amplitude = 0.0001405257, 0.3048
h0 = h1 / r1**2
reports = []
for tau in [0.0, 1.0e-5, 1.0e-4]:
    beta2 = (omega**2 - 1j * omega * tau) / (g * h0)
    root = cmath.sqrt(1 - beta2)
    plus, minus = -1 + root, -1 - root

    def b(x):
        return minus * x**plus - plus * x**minus

    scale = amplitude / b(r2 / r1)

    def z(r):
        return scale * b(r / r1)

    def dz(r):
        x = r / r1
        return scale * plus * minus * (x**(plus - 1) - x**(minus - 1)) / r1

    def u(r):
        return -g * dz(r) / (tau + 1j * omega)

    def flux(r):
        return r * (h0 * r**2) * u(r)

    residuals = []
    # Independent finite differences of flux check the harmonic continuity equation.
    for r in [r1 * 1.2, (r1 + r2) / 2, r2 * 0.9]:
        step = r * 1.0e-3
        divergence = (-flux(r + 2 * step) + 8 * flux(r + step) - 8 * flux(r - step) + flux(r - 2 * step)) / (12 * step * r)
        residual = abs(1j * omega * z(r) + divergence) / abs(omega * z(r))
        if residual > 1.0e-8:
            raise ValueError(f'Harmonic continuity transcription mismatch: {residual}')
        residuals.append(residual)
    if abs(z(r2) - amplitude) > 1e-12 or abs(u(r1)) > 1e-12:
        raise ValueError('Boundary condition mismatch')
    reports.append({'tau_for_algebra_check_only': tau, 'outer_boundary_error': abs(z(r2) - amplitude),
                    'inner_normal_velocity': abs(u(r1)), 'continuity_relative_residuals': residuals})

result = {'purpose': 'Source-derived formula transcription and boundary-condition check only',
          'time_convention': 'real(Z * exp(+i*omega*t))', 'formula_checks': reports,
          'forcing_period_seconds': 2 * math.pi / omega,
          'actual_adcirc_execution': False, 'physical_acceptance_tolerance_selected': False}
Path(__file__).with_name('analytic-expression-check.json').write_text(json.dumps(result, indent=2) + '\n')
print('PASS: harmonic continuity and both radial boundary conditions in three algebraic cases; no ADCIRC execution')
