from workout import User, Goal, Exercise, Workout

if __name__ == "__main__":
    username = input("Enter your name: ")
    workout_date = input("Date of workout yyyy-mm-dd: ")
    user1 = User(username)
    user1.add_goal(Goal("Push-up", 3, 15, 0))
    user1.add_goal(Goal("Sit-up", 3, 15, 0))
    user1.add_goal(Goal("Barbell Bench Press", 3, 12, 50))

    workout1 = Workout(workout_date, 60, [])
    exercise1 = Exercise("Push-up", "Strength", 3, 20, 0)
    exercise2 = Exercise("Sit-up", "Strength", 3, 20, 0)
    exercise3 = Exercise("Barbell Bench Press", "Strength", 2, 10, 45)
    
    workout1.exercises.extend([exercise1, exercise2, exercise3])

    user1.add_workout(workout1)

    print(f"{user1.username}'s Workout History:")
    for workout in user1.workouts:
        print(f"Date: {workout.date}, Duration: {workout.duration} minutes")
        for exercise in workout.exercises:
            print(f"Exercise: {exercise.name}, Sets: {exercise.sets}, Reps: {exercise.reps}, Weight: {exercise.weight} lbs")

    for goal in user1.goals:
        print(f"Goal: {goal.exercise_name}")
        print(f"Target Sets: {goal.target_sets}, Target Reps: {goal.target_reps}, Target Weight: {goal.target_weight}")
        print(f"Progress: {goal.progress}%")