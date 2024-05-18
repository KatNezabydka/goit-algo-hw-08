import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # Перетворення списку на мін-купу
    total_cost = 0

    while len(cables) > 1:
        # Витягніть два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Вартість з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost

        # Додайте новий кабель назад до купи
        heapq.heappush(cables, cost)

    return total_cost


# Приклад використання
cables = [8, 4, 6, 12]
result = min_cost_to_connect_cables(cables)
print("Minimum cost to connect all cables:", result)
