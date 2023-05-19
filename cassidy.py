# Define the features to be rated
features = ["Face", "Figure", "Personality", "Career Prospective"]

# Define the rating scale (in this example, we'll use a 1-100 scale)
rating_scale = list(range(1, 101))

# Define a dictionary to store Cassidy's ratings
cassidy_ratings = {"Face": 92, "Figure": 98, "Personality": 90, "Career Prospective": 95}

# Allow the user to input their ratings for each feature
user_ratings = {}
for feature in features:
    print(f"Please rate your {feature} on a scale of 1-100:")
    while True:
        rating = input()
        if rating.isdigit() and int(rating) in rating_scale:
            user_ratings[feature] = int(rating)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 100.")

# Calculate the total scores for Cassidy and the user
cassidy_score = sum(cassidy_ratings.values())
user_score = sum(user_ratings.values())

# Compare the results
print(f"Cassidy's score: {cassidy_score}")
print(f"Your score: {user_score}")
if user_score > cassidy_score:
    print("Congratulations! Your stats are better than Cassidy's.")
elif user_score < cassidy_score:
    print("Sorry, your stats are not as good as Cassidy's.")
else:
    print("You and Cassidy have the same stats!")    
