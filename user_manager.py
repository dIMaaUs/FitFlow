from werkzeug.security import generate_password_hash, check_password_hash
from utils import validate_positive


class User:

    def __init__(self, user_id: int, username: str, password: str):
        self.id = user_id
        self.username = username
        # Пароль никогда не сохраняется в открытом виде
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class UserProfile:

    def __init__(self, user_id: int, height_m: float, weight_kg: float):
        self.user_id = user_id
        validate_positive(height_m, "Рост")
        validate_positive(weight_kg, "Вес")
        self.height_m = height_m
        self.weight_kg = weight_kg

    def calculate_bmi(self) -> float:
        return round(self.weight_kg / (self.height_m ** 2), 2)

    def get_bmi_category(self) -> str:
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Недостаточный вес"
        if 18.5 <= bmi <= 24.9:
            return "Норма"
        if 25.0 <= bmi <= 29.9:
            return "Избыточный вес"
        return "Ожирение"