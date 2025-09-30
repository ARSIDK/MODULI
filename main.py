import numpy as np
import matplotlib.pyplot as plt
import pulp
import sympy as sp

print("=" * 60)
print("ЗАДАЧА 1: Графическое решение систем неравенств")
print("=" * 60)

# Часть a)
print("\n1a) Система неравенств:")
print("x₁ + x₂ ≤ 5")
print("3x₁ - x₂ ≤ 3")
print("x₁ ≥ 0, x₂ ≥ 0")

def plot_system_a():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # A
    x1 = np.linspace(0, 6, 400)
    
    x2_a1 = 5 - x1
    
    x2_a2 = 3*x1 - 3

    feasible_a = np.zeros_like(x1, dtype=bool)
    for i in range(len(x1)):
        if x2_a1[i] >= 0:  # x₂ ≥ 0
            if x2_a2[i] <= x2_a1[i] and x2_a2[i] >= 0:
                feasible_a[i] = True
    
    ax1.fill_between(x1[feasible_a], x2_a2[feasible_a], x2_a1[feasible_a], 
                    alpha=0.3, color='blue', label='Область решения')
    
    ax1.plot(x1, x2_a1, 'r-', linewidth=2, label='x₁ + x₂ = 5')
    ax1.plot(x1, x2_a2, 'g-', linewidth=2, label='3x₁ - x₂ = 3')
    ax1.axhline(0, color='black', linewidth=1)
    ax1.axvline(0, color='black', linewidth=1)
    
    ax1.set_xlim(0, 6)
    ax1.set_ylim(0, 6)
    ax1.set_xlabel('x₁')
    ax1.set_ylabel('x₂')
    ax1.set_title('Система a)')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # B
    print("\n1b) Система неравенств:")
    print("x₁ + x₂ ≤ 4")
    print("6x₁ + 2x₂ ≥ 6 → 3x₁ + x₂ ≥ 3")
    print("x₁ + 5x₂ ≥ 5")
    print("x₁ ≥ 0, x₂ ≥ 0")
    
    x2_b1 = 4 - x1
    
    x2_b2 = 3 - 3*x1

    x2_b3 = (5 - x1)/5
    
    feasible_b = np.zeros_like(x1, dtype=bool)
    for i in range(len(x1)):
        if x1[i] >= 0:  
            upper_bound = min(x2_b1[i], 6)  
            lower_bound = max(x2_b2[i], x2_b3[i], 0)  
            if lower_bound <= upper_bound and lower_bound >= 0:
                feasible_b[i] = True
    
    ax2.fill_between(x1[feasible_b], 
                    np.maximum(x2_b2[feasible_b], x2_b3[feasible_b]), 
                    x2_b1[feasible_b], 
                    alpha=0.3, color='green', label='Область решения')
    
    ax2.plot(x1, x2_b1, 'r-', linewidth=2, label='x₁ + x₂ = 4')
    ax2.plot(x1, x2_b2, 'g-', linewidth=2, label='3x₁ + x₂ = 3')
    ax2.plot(x1, x2_b3, 'b-', linewidth=2, label='x₁ + 5x₂ = 5')
    ax2.axhline(0, color='black', linewidth=1)
    ax2.axvline(0, color='black', linewidth=1)
    
    ax2.set_xlim(0, 5)
    ax2.set_ylim(0, 5)
    ax2.set_xlabel('x₁')
    ax2.set_ylabel('x₂')
    ax2.set_title('Система b)')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    return fig

# ГРАФИКИ БЛЯЯЯЯЯЯ
fig = plot_system_a()

print("\n" + "=" * 60)
print("ЗАДАЧА 2: Оптимизация производства")
print("=" * 60)

print("\nМатематическая модель:")
print("Пусть:")
print("x₁ - количество пар чулок в день")
print("x₂ - количество пар носков в день")
print("\nЦелевая функция (максимизация прибыли):")
print("P = 10x₁ + 4x₂ → max")
print("\nОграничения:")
print("0.02x₁ + 0.01x₂ ≤ 60  (участок 1)")
print("0.03x₁ + 0.01x₂ ≤ 70  (участок 2)")
print("0.03x₁ + 0.02x₂ ≤ 100 (участок 3)")
print("x₁ ≥ 0, x₂ ≥ 0")

def solve_production_problem_pulp():
    
    model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)
    
    x1 = pulp.LpVariable("x1", lowBound=0, cat='Continuous')  
    x2 = pulp.LpVariable("x2", lowBound=0, cat='Continuous')  
    
    # Целевая функция
    model += 10*x1 + 4*x2, "Total_Profit"
    
    # Ограничения
    model += 0.02*x1 + 0.01*x2 <= 60, "Workshop1_Constraint"
    model += 0.03*x1 + 0.01*x2 <= 70, "Workshop2_Constraint"
    model += 0.03*x1 + 0.02*x2 <= 100, "Workshop3_Constraint"

    model.solve()
    
    print(f"\nСтатус решения: {pulp.LpStatus[model.status]}")
    
    if model.status == pulp.LpStatusOptimal:
        x1_opt = x1.varValue
        x2_opt = x2.varValue
        max_profit = pulp.value(model.objective)
        
        print(f"\nОптимальное решение:")
        print(f"Количество пар чулок (x₁): {x1_opt:.2f}")
        print(f"Количество пар носков (x₂): {x2_opt:.2f}")
        print(f"Максимальная прибыль: {max_profit:.2f} руб. в день")
        
        print(f"\nИспользование ресурсов:")
        resource1 = 0.02*x1_opt + 0.01*x2_opt
        resource2 = 0.03*x1_opt + 0.01*x2_opt
        resource3 = 0.03*x1_opt + 0.02*x2_opt
        
        print(f"Участок 1: {resource1:.2f} ч из 60 ч ({resource1/60*100:.1f}%)")
        print(f"Участок 2: {resource2:.2f} ч из 70 ч ({resource2/70*100:.1f}%)")
        print(f"Участок 3: {resource3:.2f} ч из 100 ч ({resource3/100*100:.1f}%)")
        
        print(f"\nТеневые цены (двойственные переменные):")
        print(f"Участок 1: {model.constraints['Workshop1_Constraint'].pi:.4f}")
        print(f"Участок 2: {model.constraints['Workshop2_Constraint'].pi:.4f}")
        print(f"Участок 3: {model.constraints['Workshop3_Constraint'].pi:.4f}")
        
        print(f"\nДопустимые изменения правых частей:")
        print(f"Участок 1: [{model.constraints['Workshop1_Constraint'].slack:.2f}]")
        print(f"Участок 2: [{model.constraints['Workshop2_Constraint'].slack:.2f}]")
        print(f"Участок 3: [{model.constraints['Workshop3_Constraint'].slack:.2f}]")
        
    else:
        print("Оптимальное решение не найдено")
    
    return model, x1, x2
model, x1, x2 = solve_production_problem_pulp()

print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ")
print("=" * 60)

def find_corner_points():
    print("\nУравнения ограничений ")
    print("1) 0.02x₁ + 0.01x₂ = 60")
    print("2) 0.03x₁ + 0.01x₂ = 70") 
    print("3) 0.03x₁ + 0.02x₂ = 100")
    
    x1_sym, x2_sym = sp.symbols('x1 x2')
    
    eq1 = sp.Eq(0.02*x1_sym + 0.01*x2_sym, 60)
    eq2 = sp.Eq(0.03*x1_sym + 0.01*x2_sym, 70)
    sol1 = sp.solve((eq1, eq2), (x1_sym, x2_sym))
    
    eq3 = sp.Eq(0.03*x1_sym + 0.02*x2_sym, 100)
    sol2 = sp.solve((eq1, eq3), (x1_sym, x2_sym))
    
    sol3 = sp.solve((eq2, eq3), (x1_sym, x2_sym))
    
    print(f"\nУгловые точки:")
    print(f"Пересечение огр. 1 и 2: x₁ = {sol1[x1_sym]}, x₂ = {sol1[x2_sym]}")
    print(f"Пересечение огр. 1 и 3: x₁ = {sol2[x1_sym]}, x₂ = {sol2[x2_sym]}")
    print(f"Пересечение огр. 2 и 3: x₁ = {sol3[x1_sym]}, x₂ = {sol3[x2_sym]}")
    
    print(f"\nПрибыль в угловых точках:")
    profit1 = 10*sol1[x1_sym] + 4*sol1[x2_sym]
    profit2 = 10*sol2[x1_sym] + 4*sol2[x2_sym]
    profit3 = 10*sol3[x1_sym] + 4*sol3[x2_sym]
    
    print(f"В точке 1: {profit1:.2f} руб.")
    print(f"В точке 2: {profit2:.2f} руб.")
    print(f"В точке 3: {profit3:.2f} руб.")

find_corner_points()

print("\n" + "=" * 60)
print("АНАЛИЗ ЧУВСТВИТЕЛЬНОСТИ")
print("=" * 60)

def sensitivity_analysis():
    print("\nАнализ чувствительности для целевой функции:")
    print("Диапазоны, в которых коэффициенты целевой функции могут изменяться")
    print("без изменения оптимального решения:")
    
    print(f"\nКоэффициент для x₁ (чулки):")
    print(f"Текущее значение: 10 руб.")
    