# FitTrackPy
**FitTrackPy: Getting Started Guide**
Installation
Before you can start using FitTrackPy, you need to install it. You can do this using pip:
<sub>pip install FitTrackPy</sub>
**Usage**
1. Import the Library
Start by importing the necessary modules from the FitTrackPy library in your Python script:
<sub>from FitTrackPy import User, Workout, Exercise, Goal</sub>
2. Creating a User
Initialize a user by providing their username:
<sub>user1 = User("JohnDoe")</sub>
3. Setting Goals
You can set exercise goals for the user by creating Goal instances and adding them to the user's profile:
<sub>user1.add_goal(Goal("Push-up", 3, 15, 0))</sub>
4. Logging Workouts
Add workout data to the user's profile by creating Workout instances and including exercise details:
<sub>workout1 = Workout("2023-11-01", 60, [])</sub>
<sub>exercise1 = Exercise("Push-up", "Strength", 3, 20, 0)</sub>
<sub>exercise2 = Exercise("Sit-up", "Strength", 3, 20, 0)</sub>
<sub>workout1.exercises.extend([exercise1, exercise2])</sub>

<sub>user1.add_workout(workout1)</sub>

5. Monitoring Progress
To check progress towards goals, use the update_goals() method, which calculates progress based on the latest workout:
<sub>user1.update_goals()</sub>
6. Viewing History and Progress
You can view the user's workout history, goals, and progress with the following code:
<sub>print(f"{user1.username}'s Workout History:")</sub>
<sub>for workout in user1.workouts:</sub>
   <sub>print(f"Date: {workout.date}, Duration: {workout.duration} minutes")</sub>
   <sub>for exercise in workout.exercises:</sub>
        <sub>print(f"Exercise: {exercise.name}, Sets: {exercise.sets}, Reps: {exercise.reps}, Weight: {exercise.weight} lbs")</sub>

<sub>for goal in user1.goals:</sub>
    <sub>print(f"Goal: {goal.exercise_name}")</sub>
    <sub>print(f"Target Sets: {goal.target_sets}, Target Reps: {goal.target_reps}, Target Weight: {goal.target_weight}")</sub>
    <sub>print(f"Progress: {goal.progress}%")</sub>
