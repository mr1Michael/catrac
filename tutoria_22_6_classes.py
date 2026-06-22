

class Planet:
    def __init__(self, mass, radius, population, speed = 10):
        self.mass = mass
        self.radius = radius
        self.population = population
        self.speed = speed

    def increase_population(self):
        self.population = self.population + 1

    def decrease_population(self):
        self.population = self.population - 1

Earth = Planet(20, 1, 8)
Mars = Planet(20, 2, 0)
Jupiter = Planet(20, 3, 0)

class car:
    def __init__(self, top_speed, torque, mass, accel, doors, colours, rims, tyres):
        self.mass = mass
        self.torque = torque
        self.top_speed = top_speed
        self.torque = torque
        self.colours = colours
        self.rims = rims
        self.tyres = tyres
        self.current_speed = 0

    def current_speed(self, current_speed):
        if current_speed>self.top_speed:
            self.current_speed = self.top_speed
        else:
            self.current_speed = (current_speed)

    def increase_speed(self, acceleration_time):
        self.current_speed = self.current_speed + acceleration_time * self.accel

BMW = car(240, 300, 800, 10, 2, "blue", 22, "dunlop")
print(type (BMW))


