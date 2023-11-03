# FitTrackPy
## FitTrackPy: Getting Started Guide
### Installation
Before you can start using FitTrackPy, you need to install it. You can do this using pip:
pip install FitTrackPy
### Usage
1. Import the Library
Start by importing the necessary modules from the FitTrackPy library in your Python script:</br>
from FitTrackPy import User, Workout, Exercise, Goal
3. Creating a User
Initialize a user by providing their username:</br>
user1 = User("JohnDoe")
4. Setting Goals
You can set exercise goals for the user by creating Goal instances and adding them to the user's profile:</br>
user1.add_goal(Goal("Push-up", 3, 15, 0))
5. Logging Workouts
Add workout data to the user's profile by creating Workout instances and including exercise details:</br>
workout1 = Workout("2023-11-01", 60, [])</br>
exercise1 = Exercise("Push-up", "Strength", 3, 20, 0)</br>
exercise2 = Exercise("Sit-up", "Strength", 3, 20, 0)</br>
workout1.exercises.extend([exercise1, exercise2])</br>

user1.add_workout(workout1)

5. Monitoring Progress
To check progress towards goals, use the update_goals() method, which calculates progress based on the latest workout:</br>
user1.update_goals()
6. Viewing History and Progress
You can view the user's workout history, goals, and progress with the following code:</br>
print(f"{user1.username}'s Workout History:")</br>
for workout in user1.workouts:</br>
   print(f"Date: {workout.date}, Duration: {workout.duration} minutes")</br>
   for exercise in workout.exercises:</br>
        print(f"Exercise: {exercise.name}, Sets: {exercise.sets}, Reps: {exercise.reps}, Weight: {exercise.weight} lbs")</br>

for goal in user1.goals:</br>
    print(f"Goal: {goal.exercise_name}")</br>
    print(f"Target Sets: {goal.target_sets}, Target Reps: {goal.target_reps}, Target Weight: {goal.target_weight}")</br>
    print(f"Progress: {goal.progress}%")</br>
