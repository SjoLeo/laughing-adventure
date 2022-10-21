class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand

    def set_color(self, new_color):
        self.color = new_color

    def set_mileage(self, new_mileage):
        self.mileage = new_mileage

    def get_mileage(self):
        return self.mileage

# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587)
a_car.get_brand()
a_car.set_brand('Renault')
a_car.get_brand()

b_car = Car('Ford', 'Svart', 2)
b_car.get_brand()
b_car.set_brand("porsche")
b_car.get_brand()
print(b_car.color)
b_car.set_mileage(3)

the_mileage = b_car.get_mileage()
print(the_mileage)

c_car = Car("volvo", "röd", 123)
d_car = Car("mercedes", "röd", 543)
my_cars = [a_car, b_car, c_car, d_car]

for i in my_cars:
    i.get_brand()

               

