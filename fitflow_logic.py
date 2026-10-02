def calculate_total_weight(sets):
    if not sets:
        return 0
    return sum(weight * reps for weight, reps in sets)