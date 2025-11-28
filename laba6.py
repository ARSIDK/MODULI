import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def solve_investment_problem():
    u_values = np.array([8, 16, 24, 32, 40])
    step3_profit = np.array([55, 94, 131, 175, 214])
    f1_profit = np.array([32, 68, 115, 134, 147])
    
    n = len(u_values)
    L = np.zeros(n)
    decisions = []  
    
    options_8 = [step3_profit[0], f1_profit[0]]
    L[0] = np.max(options_8)
    decision_8 = "3 шаг" if options_8[0] == L[0] else "f1"
    decisions.append(decision_8)
    print(f"L(8) = max({options_8[0]}₃, {options_8[1]}₁) = {L[0]} ({decision_8})")
    
    options_16 = [
        step3_profit[1],                  
        step3_profit[0] + f1_profit[0],    
        f1_profit[1]                       
    ]
    L[1] = np.max(options_16)
    if options_16[0] == L[1]:
        decision_16 = "3 шаг (16)"
    elif options_16[1] == L[1]:
        decision_16 = "3 шаг (8) + f1 (8)"
    else:
        decision_16 = "f1 (16)"
    decisions.append(decision_16)
    print(f"L(16) = max({options_16[0]}₃, {options_16[1]}₃+f₁, {options_16[2]}₁) = {L[1]} ({decision_16})")
    
    options_24 = [
        step3_profit[2],                   
        step3_profit[1] + f1_profit[0],     
        step3_profit[0] + f1_profit[1],   
        f1_profit[2]                       
    ]
    L[2] = np.max(options_24)
    if options_24[0] == L[2]:
        decision_24 = "3 шаг (24)"
    elif options_24[1] == L[2]:
        decision_24 = "3 шаг (16) + f1 (8)"
    elif options_24[2] == L[2]:
        decision_24 = "3 шаг (8) + f1 (16)"
    else:
        decision_24 = "f1 (24)"
    decisions.append(decision_24)
    print(f"L(24) = max({options_24[0]}₃, {options_24[1]}₃+f₁, {options_24[2]}₃+f₁, {options_24[3]}₁) = {L[2]} ({decision_24})")
    
    options_32 = [
        step3_profit[3],                   
        step3_profit[2] + f1_profit[0],    
        step3_profit[1] + f1_profit[1],    
        step3_profit[0] + f1_profit[2],     
        f1_profit[3]                     
    ]
    L[3] = np.max(options_32)
    if options_32[0] == L[3]:
        decision_32 = "3 шаг (32)"
    elif options_32[1] == L[3]:
        decision_32 = "3 шаг (24) + f1 (8)"
    elif options_32[2] == L[3]:
        decision_32 = "3 шаг (16) + f1 (16)"
    elif options_32[3] == L[3]:
        decision_32 = "3 шаг (8) + f1 (24)"
    else:
        decision_32 = "f1 (32)"
    decisions.append(decision_32)
    print(f"L(32) = max({options_32[0]}₃, {options_32[1]}₃+f₁, {options_32[2]}₃+f₁, {options_32[3]}₃+f₁, {options_32[4]}₁) = {L[3]} ({decision_32})")

    options_40 = [
        step3_profit[4],                  
        step3_profit[3] + f1_profit[0],     
        step3_profit[2] + f1_profit[1],    
        step3_profit[1] + f1_profit[2],    
        step3_profit[0] + f1_profit[3],     
        f1_profit[4]                       
    ]
    L[4] = np.max(options_40)
    if options_40[0] == L[4]:
        decision_40 = "3 шаг (40)"
    elif options_40[1] == L[4]:
        decision_40 = "3 шаг (32) + f1 (8)"
    elif options_40[2] == L[4]:
        decision_40 = "3 шаг (24) + f1 (16)"
    elif options_40[3] == L[4]:
        decision_40 = "3 шаг (16) + f1 (24)"
    elif options_40[4] == L[4]:
        decision_40 = "3 шаг (8) + f1 (32)"
    else:
        decision_40 = "f1 (40)"
    decisions.append(decision_40)
    print(f"L(40) = max({options_40[0]}₃, {options_40[1]}₃+f₁, {options_40[2]}₃+f₁, {options_40[3]}₃+f₁, {options_40[4]}₃+f₁, {options_40[5]}₁) = {L[4]} ({decision_40})")
    
    return u_values, L, decisions

def create_optimization_graph(u_values, L, decisions):
    G = nx.DiGraph()
    
    
    for i, u in enumerate(u_values):
        G.add_node(f"L({u})", value=L[i], decision=decisions[i])
    for i in range(len(u_values)-1):
        G.add_edge(f"L({u_values[i]})", f"L({u_values[i+1]})", 
                  weight=L[i+1]-L[i])
    
    return G

def print_numpy_analysis(u_values, L):

    u_np = np.array(u_values)
    L_np = np.array(L)
    
    print(f"Входные данные (u): {u_np}")
    print(f"Оптимальные значения (L): {L_np}")
    print(f"Среднее значение L: {np.mean(L_np):.2f}")
    print(f"Максимальное значение L: {np.max(L_np)}")
    print(f"Минимальное значение L: {np.min(L_np)}")
    print(f"Стандартное отклонение L: {np.std(L_np):.2f}")

    increments = np.diff(L_np)
    print(f"\nПрирост значений L: {increments}")
    print(f"Средний прирост: {np.mean(increments):.2f}")
    
    coefficients = np.polyfit(u_np, L_np, 1)
    linear_fit = np.poly1d(coefficients)
    print(f"\nЛинейная аппроксимация: L(u) = {coefficients[0]:.3f}u + {coefficients[1]:.3f}")
    
    return u_np, L_np, increments

def plot_results(u_values, L, decisions):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    ax1.plot(u_values, L, 'bo-', linewidth=2, markersize=8)
    ax1.set_xlabel('Инвестиции (u)', fontsize=12)
    ax1.set_ylabel('Максимальный доход L(u)', fontsize=12)
    ax1.set_title('Оптимальная функция дохода', fontsize=14)
    ax1.grid(True, alpha=0.3)
    
    for i, (u, l, decision) in enumerate(zip(u_values, L, decisions)):
        ax1.annotate(f'{decision}', (u, l), textcoords="offset points", 
                    xytext=(0,10), ha='center', fontsize=8)

    increments = np.diff(L)
    ax2.bar(u_values[1:], increments, alpha=0.7, color='green')
    ax2.set_xlabel('Инвестиции (u)', fontsize=12)
    ax2.set_ylabel('Прирост доходности', fontsize=12)
    ax2.set_title('Предельная доходность инвестиций', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def main():
   
    u_values, L, decisions = solve_investment_problem()
    u_np, L_np, increments = print_numpy_analysis(u_values, L)

    G = create_optimization_graph(u_values, L, decisions)
    
    print(f"Количество узлов: {G.number_of_nodes()}")
    print(f"Количество ребер: {G.number_of_edges()}")
    print(f"Узлы графа: {list(G.nodes())}")
    
    for u, decision in zip(u_values, decisions):
        print(f"L({u}) = {decision}")
    
    plot_results(u_values, L, decisions)
    
    print(f"Максимальный доход при 40 у.е.: {L[-1]}")
    print(f"Оптимальная стратегия: {decisions[-1]}")
    print(f"Длина оптимального пути: {len(decisions)}")

if __name__ == "__main__":
    main()