from django.test import TestCase

from .models import *


class GalleryModelTesting(TestCase):

    def setUp(self):
        Category.objects.all().delete()
        Tag.objects.all().delete()
        PhotoGallery.objects.all().delete()
        WebsiteCover.objects.all().delete()
        Comment.objects.all().delete()

    def test_adding_data_to_the_model(self):
        self.assertEqual(Category.objects.count(), 0)
        category = Category.objects.create(
            slug='test-category',
            name='name-category'
        )
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(category.slug, 'test-category')
        self.assertEqual(category.name, 'name-category')
        self.assertEqual(Tag.objects.count(), 0)
        tag = Tag.objects.create(
            slug='test-tag',
            name='name-tag'
        )
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(tag.name, 'name-tag')
        self.assertEqual(tag.slug, 'test-tag')

        self.assertEqual(PhotoGallery.objects.count(), 0)
        gallery = PhotoGallery.objects.create(
            title='Test title gallery',
            slug='slug-gallery',
            content='content gallery',
            price='20.5',
            photo='user/test_img/img_user1.jpg',
            certificate='user/test_img/img_user2.jpg',

        )
        self.assertEqual(PhotoGallery.objects.count(), 1)
        self.assertEqual(gallery.title, 'Test title gallery')
        self.assertEqual(gallery.slug, 'slug-gallery')
        self.assertEqual(gallery.content, 'content gallery')
        self.assertEqual(gallery.price, '20.5')
        self.assertEqual(gallery.photo, 'user/test_img/img_user1.jpg')
        self.assertEqual(gallery.certificate, 'user/test_img/img_user2.jpg')

        self.assertEqual(WebsiteCover.objects.count(), 0)
        cover = WebsiteCover.objects.create(
            title='Website Cover test',
            site_avatar='user/test_img/img_user1.jpg'
        )
        self.assertEqual(WebsiteCover.objects.count(), 1)
        self.assertEqual(cover.title, 'Website Cover test')
        self.assertEqual(cover.site_avatar, 'user/test_img/img_user1.jpg')

        # self.assertEqual(Comment.objects.count(), 0)
        # comment = Comment.objects.create(
        #     text='Comment text test',
        #     photo_gallery=str(gallery[0].id)
        # )
        # self.assertEqual(Comment.objects.count(), 1)
        # self.assertEqual(comment.text, 'Comment text test')
        # self.assertEqual(comment.photo_gallery, str(gallery[0].id))
