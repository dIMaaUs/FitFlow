from typing import List, Dict
from utils import validate_positive


class Exercise:

    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Название не может быть пустым.")
        self.name = name
        self.sets: List[Dict[str, float]] = []

    def add_set(self, weight: float, reps: int) -> None:
        validate_positive(weight, "Вес")
        validate_positive(reps, "Повторения")
        self.sets.append({"weight": float(weight), "reps": int(reps)})

    def calculate_one_rep_max(self) -> float:
        if not self.sets:
            return 0.0
        best_set = max(self.sets, key=lambda s: s["weight"])
        if best_set["reps"] == 1:
            return best_set["weight"]
        return round(best_set["weight"] * (1 + best_set["reps"] / 30.0), 2)


class WorkoutSession:

    def __init__(self, user_id: int, title: str):
        self.user_id = user_id
        self.title = title
        self.exercises: List[Exercise] = []

    def add_exercise(self, exercise: Exercise) -> None:
        self.exercises.append(exercise)

    def calculate_total_tonnage(self) -> float:
        return sum(s["weight"] * s["reps"] for ex in self.exercises for s in ex.sets)

    def get_session_data(self, current_user_id: int) -> dict:
        if self.user_id != current_user_id:
            raise PermissionError("403 Forbidden: Доступ запрещен к чужой тренировке")
        return {
            "title": self.title,
            "exercises_count": len(self.exercises),
            "total_tonnage": self.calculate_total_tonnage()
        }