class Time:
    def __init__(self, gp, driver, hours, minutes, seconds, ms):
        self.gp = gp
        self.driver = driver
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.ms = ms

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}.{self.ms}"


class GP:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.drivers = []

    def getGPRanking(self):
        ranked_drivers = sorted(self.drivers, key=lambda driver: driver.getPoints(), reverse=True)
        return ranked_drivers

    def getPosition(self, driver):
        ranked_drivers = self.getGPRanking()
        return ranked_drivers.index(driver) + 1


class Driver:
    def __init__(self, name):
        self.name = name
        self.races = []

    def getRaced(self):
        return [race.get_gp().name for race in self.races]

    def getPoints(self):
        points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        total_points = 0
        for i, race in enumerate(self.races):
            if i < len(points):
                total_points += points[i]
        return total_points


class Championship:
    def __init__(self):
        self.drivers = []

    def getChampionshipRanking(self):
        ranked_drivers = sorted(self.drivers, key=lambda driver: driver.getPoints(), reverse=True)
        return ranked_drivers


gp1 = GP("Grand Prix 1", "2023-10-20")
gp2 = GP("Grand Prix 2", "2023-10-27")
driver1 = Driver("Driver 1")
driver2 = Driver("Driver 2")
time1 = Time(gp1, driver1, 1, 30, 45, 500)
time2 = Time(gp1, driver2, 1, 32, 15, 750)
gp1.drivers = [driver1, driver2]
driver1.races = [time1, time2]
driver2.races = [time2]
championship = Championship()
championship.drivers = [driver1, driver2]
gp1_ranking = gp1.getGPRanking()
championship_ranking = championship.getChampionshipRanking()
print(f"{gp1.name} Ranking:")
for i, driver in enumerate(gp1_ranking):
    print(f"{i + 1}. {driver.name} ({driver.getPoints()} points)")

print("\nChampionship Ranking:")
for i, driver in enumerate(championship_ranking):
    print(f"{i + 1}. {driver.name} ({driver.getPoints()} points)")
