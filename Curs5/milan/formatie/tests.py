from django.test import TestCase

# Create your tests here.
import pycountry

italia = pycountry.countries.get(alpha_2='IT')
print(italia.flag)


formatie = [ ('Dida', 'BR'), 
                ('Oddo', 'IT'),
                ('Nesta', 'IT'),  
                ('Maldini', 'IT'),
                ('Jankulovski', 'CZ') ,
                ('Gattuso', 'IT'),
                ('Pirlo', 'IT'), 
                ('Ambrosini', 'IT') , 
                ('Kaka', 'BR'),
                ('Seedors', 'NL'),
                ('Inzaghi', 'IT')]


formatie = [ (j, pycountry.countries.get(alpha_2=n).flag )  for j,n in formatie  ]

pozitionare = [1, 4, 3, 2]


pozitionare_formatie = []
counter = 0
for i in pozitionare:
    pozitionare_formatie.append(formatie[counter: counter + i])
    counter += i

print(pozitionare_formatie)