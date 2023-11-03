class User:
    def __init__(self, username):
        self.username = username
        self.workouts = []
        self.goals = []

    def add_workout(self, workout):
        self.workouts.append(workout)
        self.update_goals()

    def add_goal(self, goal):
        self.goals.append(goal)

    def update_goals(self):
        # Calculate progress towards goals based on the latest workout
        if self.goals:
            latest_workout = self.workouts[-1]
            for goal in self.goals:
                if goal.exercise_name in [exercise.name for exercise in latest_workout.exercises]:
                    goal.update_progress(latest_workout)
class Workout:
    def __init__(self, date, duration, exercises):
        self.date = date
        self.duration = duration
        self.exercises = exercises

class Exercise:
    def __init__(self, name, category, sets, reps, weight):
        self.name = name
        self.category = category
        self.sets = sets
        self.reps = reps
        self.weight = weight

class Goal:
    def __init__(self, exercise_name, target_sets, target_reps, target_weight):
        self.exercise_name = exercise_name
        self.target_sets = target_sets
        self.target_reps = target_reps
        self.target_weight = target_weight
        self.progress = 0  # Progress is initially set to 0

    def update_progress(self, latest_workout):
        for exercise in latest_workout.exercises:
            if exercise.name == self.exercise_name:
                if exercise.sets >= self.target_sets and exercise.reps >= self.target_reps and exercise.weight >= self.target_weight:
                    self.progress = 100  # Goal achieved
                else:
                    self.progress = min(100, (exercise.sets / self.target_sets) * 100)  # Calculate progress percentage