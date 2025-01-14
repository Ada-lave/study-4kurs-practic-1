from django.test import TestCase
from shelter.models import Shelter, Cat, Adoption

class ShelterModelTest(TestCase):
    def setUp(self):
        self.shelter = Shelter.objects.create(
            name="Happy Tails",
            address="123 Cat Lane",
            capacity=50
        )

    def test_shelter_creation(self):
        self.assertEqual(self.shelter.name, "Happy Tails")
        self.assertEqual(self.shelter.address, "123 Cat Lane")
        self.assertEqual(self.shelter.capacity, 50)

    def test_shelter_str(self):
        self.assertEqual(str(self.shelter), "Happy Tails")


class CatModelTest(TestCase):
    def setUp(self):
        self.shelter = Shelter.objects.create(
            name="Happy Tails",
            address="123 Cat Lane",
            capacity=50
        )
        self.cat = Cat.objects.create(
            name="Whiskers",
            age=2,
            shelter=self.shelter
        )

    def test_cat_creation(self):
        self.assertEqual(self.cat.name, "Whiskers")
        self.assertEqual(self.cat.age, 2)
        self.assertEqual(self.cat.shelter, self.shelter)

    def test_cat_str(self):
        self.assertEqual(str(self.cat), "Whiskers")


class AdoptionModelTest(TestCase):
    def setUp(self):
        self.shelter = Shelter.objects.create(
            name="Happy Tails",
            address="123 Cat Lane",
            capacity=50
        )
        self.cat = Cat.objects.create(
            name="Whiskers",
            age=2,
            shelter=self.shelter
        )
        self.adoption = Adoption.objects.create(
            cat=self.cat,
            adopter_name="John Doe",
            adoption_date="2025-01-01"
        )

    def test_adoption_creation(self):
        self.assertEqual(self.adoption.cat, self.cat)
        self.assertEqual(self.adoption.adopter_name, "John Doe")
        self.assertEqual(self.adoption.adoption_date, "2025-01-01")

    def test_adoption_str(self):
        self.assertEqual(str(self.adoption), "John Doe приютил Whiskers")