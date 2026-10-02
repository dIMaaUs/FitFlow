import unittest
from user_manager import User, UserProfile
from workout_manager import Exercise, WorkoutSession


class TestFitFlowSecurityAndLogic(unittest.TestCase):

    def setUp(self):
        self.user_alice = User(user_id=1, username="alice", password="SecurePassword123")
        self.user_bob = User(user_id=2, username="bob", password="PasswordBob456")

        self.alice_workout = WorkoutSession(user_id=1, title="День спины")
        self.bench_press = Exercise("Тяга штанги")
        self.bench_press.add_set(100.0, 10)
        self.alice_workout.add_exercise(self.bench_press)

        self.profile = UserProfile(user_id=1, height_m=1.80, weight_kg=85.0)


    def test_password_hashing(self):
        self.assertNotEqual(self.user_alice.password_hash, "SecurePassword123")
        self.assertTrue(self.user_alice.check_password("SecurePassword123"))
        self.assertFalse(self.user_alice.check_password("WrongPassword"))

    def test_access_control_success(self):
        data = self.alice_workout.get_session_data(current_user_id=1)
        self.assertEqual(data["title"], "День спины")
        self.assertEqual(data["total_tonnage"], 1000.0)

    def test_access_control_forbidden_403(self):
        with self.assertRaises(PermissionError):
            self.alice_workout.get_session_data(current_user_id=self.user_bob.id)


    def test_exercise_one_rep_max(self):
        self.assertEqual(self.bench_press.calculate_one_rep_max(), 133.33)

    def test_invalid_exercise_data(self):
        with self.assertRaises(ValueError):
            self.bench_press.add_set(-10, 5)

    def test_user_bmi(self):
        self.assertEqual(self.profile.calculate_bmi(), 26.23)
        self.assertEqual(self.profile.get_bmi_category(), "Избыточный вес")


if __name__ == '__main__':
    unittest.main()