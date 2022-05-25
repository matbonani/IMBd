from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watch_list.api import serializers
from watch_list import models


class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='example', password='bonani123456')  # normal user
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects\
            .create(name='example', about='just a stream', website='http://www.example.com')

    def test_streamplatform_create(self):
        data = {
            "name": "example",
            "about": "just a streamplatform",
            "webisite": "https://netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_detail(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_delete(self):
        response = self.client.delete(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_update(self):
        data = {
            "name": "examplePUT",
            "about": "just a streamplatformPUT",
            "webisite": "https://netflix.com"
        }
        response = self.client.put(reverse('streamplatform-detail', args=(self.stream.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WatchlistTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='example', password='bonani123456')  # normal user
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects\
            .create(name='example', about='just a stream', website='http://www.example.com')

        self.watchlist = models.WatchList.objects\
            .create(platform=self.stream, title='cruz', storyline='example', active=True)

    def test_watchlist_create(self):
        data = {
            "platform": self.stream,
            "title": "Example",
            "storyline": "Example",
            "active": True
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_detail(self):
        response = self.client.get(reverse('movie-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.get().title, 'cruz')
        self.assertEqual(models.WatchList.objects.count(), 1)

    def test_watchlist_detail_delete(self):
        response = self.client.delete(reverse('movie-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_detail_delete(self):
        data = {
            "platform": self.stream,
            "title": "ExamplePUT",
            "storyline": "ExamplePUT",
            "active": True
        }
        response = self.client.put(reverse('movie-detail', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReviewTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='example', password='bonani123456')  # normal user
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects\
            .create(name='example', about='just a stream', website='http://www.example.com')

        self.watchlist = models.WatchList.objects\
            .create(platform=self.stream, title='cruz', storyline='example', active=True)

        self.watchlist2 = models.WatchList.objects\
            .create(platform=self.stream, title='cruz', storyline='example', active=True)

        self.review = models.Review.objects.create(review_user=self.user, rating=5,
                                                   description="nice movie", watchlist=self.watchlist2,
                                                   active=True)

    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Review Test",
            "active": True

        }
        response = self.client.post(reverse("review-create", args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse("review-create", args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauth(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Review Test",
            "active": True

        }
        self.client.force_authenticate(user=None)  # another user
        response = self.client.post(reverse("review-create", args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Review Test- Update",
            "watchlist": self.watchlist,
            "active": False

        }
        response = self.client.put(reverse("review-detail", args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_detail_delete(self):
        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_detail(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_user(self):
        response = self.client.get('/watch/review/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)