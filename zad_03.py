"""
• Izračun mjesečne potrošnje el. struje te cijene el. struje koju potroši 
   mikrovalna pećnica snage 1,3 kW ako se koristi 2 sata dnevno?
"""

power = 1.3  # kW
time = 2  # hours
cost_per_kWh = 0.15  # EUR

monthly_consumption = power * time * 30  # kWh
monthly_cost = monthly_consumption * cost_per_kWh

print(f'Mjesečna potrošnja: {monthly_consumption} kWh')
print(f'Mjesečni trošak: {monthly_cost} EUR')