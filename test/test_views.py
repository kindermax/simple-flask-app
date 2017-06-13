import unittest

from application import app
import models


class ViewsFunctions(unittest.TestCase):

    def setUp(self):

        self.app = app.test_client()
        self.app.testing = True
        self.db = models.db
        with self.app.application.app_context():
            self.db.create_all()
            self.db.session.commit()

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_save_person_status_code(self):
        result = self.app.post('/api/add_person', data={
            'name': "user_for_tests"
        })
        self.assertEqual(result.status_code, 201)

    def test_delete_person_status_code(self):
        result = self.app.post('/api/add_person', data={
            'name': "user_for_tests"
        })
        self.assertEqual(result.status_code, 201)
        result = self.app.post('/api/delete_person', data={
            'name': "user_for_tests"
        })
        self.assertEqual(result.status_code, 200)

    def test_save_person_which_already_existed_status_code(self):
        result = self.app.post('/api/add_person', data={
            'name': "user_for_tests"
        })
        self.assertEqual(result.status_code, 201)

        try_to_save_again = self.app.post('/api/add_person', data={
            'name': "user_for_tests"
        })
        self.assertEqual(try_to_save_again.status_code, 409)

    def tearDown(self):
        with self.app.application.app_context():
            self.db.session.remove()
            self.db.drop_all()

