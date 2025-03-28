from django.test import TestCase

# Create your tests here.


dictionar = {
    'culoare':'verde'
}

print(dictionar['culoare'])
print(dictionar.get('culoare'))
print(dictionar.get('color'))

print(dictionar.get('color', 'nemaiintalnita'))

