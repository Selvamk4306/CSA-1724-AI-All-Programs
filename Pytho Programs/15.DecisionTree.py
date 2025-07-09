# Simple decision tree using if-else

def decide_umbrella(weather, wind):
    if weather == 'rainy':
        if wind == 'strong':
            return "Don't bring umbrella (it might break)"
        else:
            return "Bring umbrella"
    else:
        return "No need for umbrella"

# Test the decision tree
weather = input("Is it rainy or sunny? ")
wind = input("Is the wind strong or weak? ")

decision = decide_umbrella(weather, wind)
print("Decision:", decision)
