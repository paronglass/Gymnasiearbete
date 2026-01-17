import random


# tar emot vilket scenario som sker och slumpar en tid för detta inom tidsintervallet för det scenariot 
def get_time(scenario):
    time_intervals = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8]]

    if scenario >= len(time_intervals):
        return None

    result = random.randint(time_intervals[scenario][0], time_intervals[scenario][1])
    return result

# tar emot de två bilarna och tar med hjälp av detta reda på sannolikheten för varje scenario, utifrån dessa sannolikheter 
# skickar den tillbaka ett slumpmässigt scenario 
def get_scenario(driver1, driver2):
    result = 0 
    prob_list = []

    for scenario in range(8):

        for _ in range(get_prob_scen(scenario, driver1, driver2)):
            prob_list.append(scenario)

    result = random.choice(prob_list)

    return result

def get_prob_scen(scenario, driver1, driver2):
    return 10

def the_cars(driver1, driver2):
    driver1 = yttre_faktorer(*driver1)
    driver2 = yttre_faktorer(*driver2)
    
    return driver1, driver2


# yttre faktorer skickas in inre faktorer (reaktion, uppmärksamhet och aggresivitet) skickas tillbaka
def yttre_faktorer(alkohol, stress, trötthet, erfarenhet):
    uppmärksamhet = 5
    reaktionsförmåga = 5
    aggresivitet = 5
    id = [uppmärksamhet, reaktionsförmåga, aggresivitet]

    if stress >= 8:
        uppmärksamhet -= 2
        reaktionsförmåga -= 2
        aggresivitet += 1
    
    if stress in range(6,8): #kolla så att rangen stämmer med det jag har skrivit på papperet
        uppmärksamhet -= 1
        reaktionsförmåga -= 1
        aggresivitet += 1

    if stress < 3:
        aggresivitet -= 1
       
    if trötthet in range(6,8):
        uppmärksamhet -= 2
        reaktionsförmåga -= 2

    if trötthet in range(3,5):
        uppmärksamhet -= 1
        reaktionsförmåga -= 1

    if erfarenhet in range(6,8):
        uppmärksamhet += 2
        reaktionsförmåga += 2
        aggresivitet -= 1

    if erfarenhet in range(3,5):
        uppmärksamhet += 1
        reaktionsförmåga += 1
        aggresivitet += 1

    if erfarenhet >= 8:
        uppmärksamhet += 3
        reaktionsförmåga += 3
        aggresivitet -= 2

    if erfarenhet >= 2:
        uppmärksamhet -= 1
        reaktionsförmåga -= 2
        aggresivitet += 2

    if trötthet >= 8:
        uppmärksamhet = 1
        reaktionsförmåga = 1

    if alkohol == True:
        uppmärksamhet = 1
        reaktionsförmåga = 1
    
    if uppmärksamhet < 1:
        uppmärksamhet = 1

    if reaktionsförmåga < 1:
        reaktionsförmåga = 1

    if aggresivitet < 1:
        aggresivitet = 1

    id[0] = uppmärksamhet 
    id[1] = reaktionsförmåga 
    id[2] = aggresivitet

    return id  
    

if __name__ == "__main__":

    
   ## print(the_cars([True, 5, 6, 8], [False, 6, 2, 3]))
    result = {}
    for i in range(10000):
        n = get_time(get_scenario([ 5, 6, 3], [3, 5, 7]))
        try:
            result[n] += 1
        except KeyError:
            result[n] = 1

    print(result)