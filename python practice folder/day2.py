foods = ["rice", "pasta", "chickpea","noodles","salad"]
ratings = {
    "rice":8,
    "pasta":9,
    "chickpea":4,
    "noodles" :10,
    "salad":7
}
for key,value in ratings.items():
    print(f"{key}:{value}")