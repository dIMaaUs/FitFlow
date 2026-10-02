from typing import List, Dict


class Exercise:
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Название упражнения не может быть пустым.")
        self.name = name
        self.sets: List[Dict[str, float]] = []

    def add_set(self, weight: float, reps: int) -> None:
        if weight < 0 or reps <= 0:
            raise ValueError("Вес >= 0, повторения > 0.")
        self.sets.append({"weight": float(weight), "reps": int(reps)})

    def calculate_one_rep_max(self) -> float:
        if not self.sets:
            return 0.0
        best_set = max(self.sets, key=lambda s: s["weight"])
        if best_set["reps"] == 1:
            return best_set["weight"]
        one_rm = best_set["weight"] * (1 + best_set["reps"] / 30.0)
        return round(one_rm, 2)


class WorkoutSession:
    def __init__(self, title: str):
        self.title = title
        self.exercises: List[Exercise] = []

    def add_exercise(self, exercise: Exercise) -> None:
        self.exercises.append(exercise)

    def calculate_total_tonnage(self) -> float:
        total = 0.0
        for ex in self.exercises:
            for s in ex.sets:
                total += s["weight"] * s["reps"]
        return total


class UserProfile:
    def __init__(self, height_m: float, weight_kg: float):
        if height_m <= 0 or weight_kg <= 0:
            raise ValueError("Рост и вес должны быть положительными числами.")
        self.height_m = height_m
        self.weight_kg = weight_kg

    def calculate_bmi(self) -> float:
        return round(self.weight_kg / (self.height_m ** 2), 2)

    def get_bmi_category(self) -> str:
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Недостаточный вес"
        elif 18.5 <= bmi <= 24.9:
            return "Норма"
        elif 25.0 <= bmi <= 29.9:
            return "Избыточный вес"
        return "Ожирение"
