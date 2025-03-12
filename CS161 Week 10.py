#CS161 Week 10

class SolarObject: #parent class SolarObject
    def __init__(self, name, farthest_distance, spin, average_days): #attributes as in instructions
        self.name = name #name attribute for printing statement at end
        self.farthest_distance = farthest_distance
        self.average_days = average_days
        self.spin = spin

    def colonization(self): #colonization method
        earth_population = 6000000000 #setting default population
        population = earth_population / self.farthest_distance #calculating
        if population < 1000000000:
            return 0
        return round(population / 1000000000) #dividing by 1000000000 for printing results

    def spin(self): #pass spin for now, will change later
        pass

class Planet(SolarObject):
    def __init__(self, name, farthest_distance, average_days):
        #super() for inheriting
        super().__init__(name, farthest_distance, "slightly elliptical", average_days) #setting spin as slightly elliptical
    def spin(self): #polymorphism
        return "slightly elliptical"
#Planet instances
earth = Planet("Earth", 1, 365) #assigning earth as a Planet - 1 AU and 365 days
mars = Planet("Mars", 1.4,687) #assigning mars as a Planet

class Comet(SolarObject):
    def __init__(self, name, farthest_distance, average_days):
        #Comet also inherits
        super().__init__(name, farthest_distance, "like crazy", average_days)
    def spin(self): #polymorphism
        return "like crazy"
#Comet instances
halley = Comet("Halley",35, 76.95*365) #*365 to convert from days to year
hale_bopp = Comet("Hale-Bopp",354, 2397.29 * 365)

#printing all four objects
for entity in [halley, hale_bopp, earth, mars]:
    #isinstance from chatgpt
    if isinstance(entity, Comet): #for comets, using years
        print(f"{entity.name} is {entity.farthest_distance} au from the sun, spins {entity.spin}, "
              f"has an orbit taking {entity.average_days / 365} years and can support a population of: {entity.colonization()} billion.")
    else: #for planets, using days
        print(f"{entity.name} is {entity.farthest_distance} au from the sun, spins {entity.spin}, "
              f"has an orbit taking {entity.average_days} days and can support a population of: {entity.colonization()} billion.")