import datetime
import random

# User data (hardcoded for this example)
users = {
    'John': {'subjects': ['Math', 'Biology', 'History'], 'goal': 'Score 90% on Biology test', 'available_time': 2, 'deadline': '2024-12-05'}
}

# Task types and priorities
task_list = {
    'Math': ['Solve 5 equations', 'Review calculus notes', 'Practice algebra'],
    'Biology': ['Watch video on digestion', 'Review human body systems', 'Take notes on the immune system'],
    'History': ['Summarize causes of World War II', 'Research key historical figures', 'Write a timeline']
}

# Function to create a study plan
def create_study_plan(user):
    subjects = users[user]['subjects']1
    available_time = users[user]['available_time']
    study_plan = {}

    # Divide available time across subjects
    time_per_subject = available_time / len(subjects)

    for subject in subjects:
        tasks = random.sample(task_list[subject], 2)  # Picking 2 random tasks from each subject
        study_plan[subject] = {'tasks': tasks, 'time': time_per_subject}

    return study_plan

# Function to show the study plan
def show_study_plan(user):
    study_plan = create_study_plan(user)
    print(f"\nStudy Plan for {user}:")
    print(f"Goal: {users[user]['goal']}")
    print(f"Deadline: {users[user]['deadline']}")
    print("------------------------------------------------")
    for subject, details in study_plan.items():
        print(f"\nSubject: {subject}")
        print(f"Time Allocated: {details['time']} hours")
        for i, task in enumerate(details['tasks'], start=1):
            print(f"  Task {i}: {task}")

# Function to track progress
def track_progress(user):
    print("\nProgress Tracker:")
    completed_tasks = random.randint(0, 5)  # Random number of completed tasks for demo
    total_tasks = 6  # Total tasks in a basic study plan
    progress_percentage = (completed_tasks / total_tasks) * 100
    print(f"Completed: {completed_tasks}/{total_tasks} tasks")
    print(f"Progress: {progress_percentage:.2f}%")
    if progress_percentage == 100:
        print("Congratulations! You've completed all tasks for today.")
    else:
        print("Keep going! You're making great progress.")

# Function to simulate the Ask Buddy chatbot
def ask_buddy():
    print("\nAsk Buddy (AI-powered chatbot):")
    question = input("Ask a question: ")
    print(f"Buddy: Let me explain {question}...")
    # Simulate a simple answer
    if "second law" in question.lower():
        print("Buddy: Newton's Second Law states that Force = Mass * Acceleration.")
    else:
        print("Buddy: That's an interesting question! I’ll look up more details for you.")

# Main function to run the app
def main():
    print("Welcome to the Personalized Study Planner\n")
    user = 'John'  # Hardcoded user for demo

    while True:
        print("\nWhat would you like to do?")
        print("1. View Study Plan")
        print("2. Track Progress")
        print("3. Ask Buddy")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_study_plan(user)
        elif choice == '2':
            track_progress(user)
        elif choice == '3':
            ask_buddy()
        elif choice == '4':
            print("Goodbye! Keep studying!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
