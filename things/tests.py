from django.test import TestCase

from things.forms import ThingForm
from things.models import Thing

from django import forms

# Create your tests here.
class ThingTest(TestCase):

    """Unit tests for the things form"""
    def setUp(self):
        self.form_input = {
            'name' : 'my car',
            'description' : 'a brown suv',
            'quantity' : '1'
        }

    def test_valid_thing_form(self):
        form = ThingForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = ThingForm()

        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('quantity', form.fields)

    def test_form_uses_model_validation(self):
        self.form_input['name'] = ''
        form = ThingForm(data = self.form_input)
        self.assertFalse(form.is_valid())


    def test_form_cannot_have_quantity_less_than_zero(self):
        self.form_input['quantity'] = '-1'
        form = ThingForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_cannot_have_quantity_more_than_50(self):
        self.form_input['quantity'] = '51'
        form = ThingForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_cannot_have_name_greater_than_35_letters(self):
        self.form_input['name'] = 'a' * 36
        form = ThingForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_can_have_blank_description(self):
        self.form_input['description'] = ''
        form = ThingForm(data = self.form_input)
        self.assertTrue(form.is_valid())
