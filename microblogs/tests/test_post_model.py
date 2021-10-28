from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import User, Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name= 'John',
            last_name= 'Doe',
            email= 'johndoe@example.org',
            password= 'Password123',
            bio= 'The quick brown fox jumps over the lazy dog.'
        )

        self.post = Post.objects.create(
            author='@johndoe',
            text='The quick brown fox jumps over the lazy dog.'
        )

    def test_author_foreign_key_invalid(self):
        if self.post.author == self.user.username:
            self._assert_post_is_valid()
        else:
            self._assert_post_is_invalid()

    def test_text_may_not_be_blank(self):
        self.post.text = ''
        self._assert_post_is_invalid()

    def test_text_need_not_be_unique(self):
        second_user = self.create_second_user()
        second_post = self.create_second_post()
        self.post.text = second_post.text
        self._assert_post_is_valid()

    def test_text_may_contain_280_characters(self):
        self.post.text = 'x' * 280
        self._assert_post_is_valid()

    def test_text_must_not_contain_more_than_280_characters(self):
        self.post.text = 'x' * 281
        self._assert_post_is_invalid()

    def _assert_post_is_valid(self):
        try:
            self.post.full_clean()
        except (ValidationError):
            self.fail('Test post should be valid.')

    def _assert_post_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.post.full_clean()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid.')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def create_second_user(self):
        user = User.objects.create_user(
            '@janedoe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.org',
            password='Password123',
            bio='The quick yellow fox jumps over the lazy dog.'
        )

        return user

    def create_second_post(self):

        post = Post.objects.create(
            author='@janedoe',
            text='The quick yellow fox jumps over the lazy dog.'
        )

        return post
