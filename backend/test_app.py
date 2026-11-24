import unittest

from app import app


class SubmitRouteTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_submit_processes_registration(self):
        response = self.client.post(
            "/submit",
            json={
                "name": "jane doe",
                "email": "JANE@example.com",
                "course": "docker",
                "message": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["processed_data"],
            {
                "student_name": "Jane Doe",
                "contact_email": "jane@example.com",
                "enrolled_course": "DOCKER",
                "remarks": "None provided",
            },
        )

    def test_submit_rejects_missing_required_fields(self):
        response = self.client.post(
            "/submit",
            json={"name": "Jane Doe", "email": "jane@example.com"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("Course", response.get_json()["error"])


if __name__ == "__main__":
    unittest.main()
