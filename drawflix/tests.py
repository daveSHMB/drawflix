from django.test import TestCase
from django.core.urlresolvers import reverse
from drawflix.models import Drawing
from drawflix.forms import DrawingForm

class DrawingMethodTests(TestCase):

    def test_ensure_likes_are_positive(self):

        """
        ensure_likes_are_positive should result in True for Drawings where
        likes are zero or positive
        """

        draw = Drawing(film='test',likes=-1)
        draw.save()
        self.assertEqual((draw.likes >= 0), True)


class MostRecentViewTestCase(TestCase):

    def test_most_recent_displays_drawing(self):

        """
        test_most_recent_displays_drawing should result in True if drawing
        is added and displayed on page
        """

        add_film('Rocky')

        response = self.client.get(reverse('most_recent'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Rocky")

def add_film(film):
    f = Drawing.objects.get_or_create(film=film)[0]
    f.save()
    return f
