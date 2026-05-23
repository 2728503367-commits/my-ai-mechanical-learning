import math

def cylinder_force(pressure_mpa, bore_diameter_mm, rod_diameter_mm=0, efficiency=0.85):
    """
    Calculate pneumatic cylinder push and pull force.

    pressure_mpa: air pressure in MPa
    bore_diameter_mm: cylinder bore diameter in mm
    rod_diameter_mm: piston rod diameter in mm
    efficiency: mechanical efficiency, default 0.85
    """

    push_area = math.pi * bore_diameter_mm ** 2 / 4
    pull_area = math.pi * (bore_diameter_mm ** 2 - rod_diameter_mm ** 2) / 4

    push_force_n = pressure_mpa * push_area * efficiency
    pull_force_n = pressure_mpa * pull_area * efficiency

    push_force_kgf = push_force_n / 9.80665
    pull_force_kgf = pull_force_n / 9.80665

    return push_force_n, pull_force_n, push_force_kgf, pull_force_kgf


# Example
pressure = 0.5
bore = 50
rod = 20

push_n, pull_n, push_kgf, pull_kgf = cylinder_force(pressure, bore, rod)

print("Cylinder Force Calculator")
print("-------------------------")
print(f"Pressure: {pressure} MPa")
print(f"Bore diameter: {bore} mm")
print(f"Rod diameter: {rod} mm")
print()
print(f"Push force: {push_n:.2f} N, about {push_kgf:.2f} kgf")
print(f"Pull force: {pull_n:.2f} N, about {pull_kgf:.2f} kgf")
