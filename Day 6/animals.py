class Animal:
    noise = 'Rrrrr'
    colour = 'Red'
    def make_noise(self):
        print(f'{self.noise}')
    def set_noise (self, new_noise):
        self.noise = new_noise
    def get_noise (self):
        return self.noise
    def set_noise (self, new_noise):
        self.noise = new_noise
        return self.noise
#for the colour
    def get_colour (self):
        return self.colour
    def set_colour (self, new_colour):
        self.colour = new_colour
        return self.colour

class Wolf (Animal):
    noise = 'grrr'

class BabyWolf(Wolf):
    colour = 'Yellow'
    #def rando():
     #   print ('This')