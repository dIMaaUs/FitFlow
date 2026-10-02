import unittest
from fitflow_logic import Exercise, WorkoutSession, UserProfile


class TestFitFlowLogic(unittest.TestCase):
    
    def setUp(self):
        self.bench_press = Exercise("Жим лежа")
        self.bench_press.add_set(100.0, 10)
        self.bench_press.add_set(105.0, 8)

        self.workout = WorkoutSession("День груди")
        self.workout.add_exercise(self.bench_press)

        self.user = UserProfile(height_m=1.80, weight_kg=85.0)

    def test_exercise_one_rep_max(self):
        self.assertEqual(self.bench_press.calculate_one_rep_max(), 133.0)

    def test_invalid_exercise_data(self):
        with self.assertRaises(ValueError):
            self.bench_press.add_set(-10, 5)
        with self.assertRaises(ValueError):
            Exercise("")

    def test_workout_tonnage(self):
        self.assertEqual(self.workout.calculate_total_tonnage(), 1840.0)

    def test_user_bmi_and_category(self):
        self.assertEqual(self.user.calculate_bmi(), 26.23)
        self.assertEqual(self.user.get_bmi_category(), "Избыточный вес")

    def test_invalid_user_profile(self):
        with self.assertRaises(ValueError):
            UserProfile(height_m=-1.8, weight_kg=80)


if __name__ == '__main__':
    unittest.main()