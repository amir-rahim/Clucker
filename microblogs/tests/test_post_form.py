# from microblogs.forms import PostForm
# from django.test import TestCase
# from microblogs.models import Post


# class PostFormTest(TestCase):


#     def setUp(self):
#         self.form_input = {
#             'author':'Jeff',
#             'text' : 'Email jeff@amazon.com for direct attention from Bezos or his Executive Team. Bezos widely'
#                      'advertises his own email address so customers can get in touch with him.',
#         }

#     def test_valid_post_form(self):
#         form = PostForm(data=self.form_input)
#         self.assertTrue(form.is_valid())

#     def test_form_uses_model_validation(self):
#         self.form_input['text'] = 'x' * 281
#         form = PostForm(data=self.form_input)
#         self.assertFalse(form.is_valid())

#     def test_post_must_save_correctly(self):
#         form = PostForm(data=self.form_input)
#         before_count = Post.objects.count()
#         form.save()
#         after_count = Post.objects.count()
#         self.assertEqual(after_count, before_count + 1)
