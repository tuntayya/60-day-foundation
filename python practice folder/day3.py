foods = ["rice","pasta","chickpea","noodles","salad"]
ratings = {
    "rice":8,
    "pasta":9,
    "chickpea":4,
    "noodles" :10,
    "salad":7
}
def print_foods(foods):
    for food in foods:
        print(food)
def print_ratings(ratings):
    for key, value in ratings.items():
        print(f"{key}:{value}")
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Call the functions
print_foods(foods)

print()

print_ratings(ratings)

print()

print(calculate_average([1, 2, 3]))
print(calculate_average([10, 20, 30]))
print(calculate_average([5, 15, 25, 35]))