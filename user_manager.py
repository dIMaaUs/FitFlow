from utils import validate_positive

class UserProfile:
    
    def __init__(self, height_m: float, weight_kg: float):
        validate_positive(height_m, "Рост")
        validate_positive(weight_kg, "Вес")
        self.height_m = height_m
        self.weight_kg = weight_kg

    def calculate_bmi(self) -> float:
        return round(self.weight_kg / (self.height_m ** 2), 2)

    def get_bmi_category(self) -> str:
        bmi = self.calculate_bmi()
        if bmi < 18.5: return "Недостаточный вес"
        if 18.5 <= bmi <= 24.9: return "Норма"
        if 25.0 <= bmi <= 29.9: return "Избыточный вес"
        return "Ожирение"