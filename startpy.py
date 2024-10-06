import pandas as pd
import time
import sys
def fashion(duration=5, length=40):
    time.sleep(1)
    print("The test is thinking...")
    time.sleep(1)
    starttime = time.time()
    endtime = duration + starttime
    while time.time() < endtime:
        for i in range(length + 1):
            bar = ("#" * i).ljust(length)
            percent = (i / length) * 100
            sys.stdout.write(f'\r[{bar}] {percent:.2f}%')
            sys.stdout.flush()
            time.sleep(duration / length)
    sys.stdout.write(f'\r[{"#" * length}] 100.00% Complete!\n')
    sys.stdout.flush()
def main():
    print("Welcome to the Python Calibration Quiz 🐍.")
    print("Please be honest for accurate results.")
    print("This quiz is an estimate of your programming level.")
    print("Note: This doesn't include specializations. Good luck!")
def rank(rank, stuff, sources):
    print(f"\nCongrats! The test concludes that you are currently a {rank}.")
    print("To improve further, we highly recommend:")
    print(stuff)
    print("Where do you learn these things?")
    print(sources)
    print("Good luck on your programming journey!")
mcq = {
    'Question': [
        'How much experience do you have with Python?', 
        'How many projects have you completed?', 
        'How comfortable are you with Data Structures and Algorithms (DSA)?', 
        'How familiar are you with working with data in Python (e.g., CSV, Pandas)?', 
        'How familiar are you with Object-Oriented Programming (OOP)?', 
        'How much experience do you have with version control tools like Git?', 
        'How would you rate your overall Python skills?'
    ],
    'Option1': [
        'Just started', 
        'None, just rawdog Python', 
        'DSA?', 
        'Just used a lot of strings and lists', 
        'OOP?', 
        'Nah, never did it', 
        'Horrible'
    ],
    'Option2': [
        'Learnt only through school', 
        'Max 1', 
        'I did like a few questions', 
        'SQL', 
        'I know only the definition', 
        'Did it like once or twice but know the gist of it', 
        'Below average'
    ],
    'Option3': [
        'I learnt my preferred programming language for a few weeks', 
        'Every time 1 or 2', 
        'A decent amount', 
        'CSV files', 
        'Aware of it and used it once or twice', 
        'Very aware of it', 
        'Average'
    ],
    'Option4': [
        'I spent a few months', 
        'Min 3', 
        'A lot', 
        'Pandas', 
        'Good at it', 
        'Did a lot of it', 
        'Above average'
    ],
    'Option5': [
        'I no-lifed it', 
        'Every time 3 or above', 
        'A LOT', 
        'JSON, CSV.. name it, I can use it', 
        'Learnt it when I was in 3rd grade', 
        'Know everything about it', 
        'Way above average'
    ],
    'Score1': [1, 1, 1, 1, 1, 1, 1],
    'Score2': [2, 2, 2, 2, 2, 2, 2],
    'Score3': [3, 3, 3, 3, 3, 3, 3],
    'Score4': [4, 4, 4, 4, 4, 4, 4],
    'Score5': [5, 5, 5, 5, 5, 5, 5]
}
df = pd.DataFrame(mcq)
main()
sinput = input("\nEnter 'start' if you would like to start: ").lower()
if sinput in ["start","s","y","continue"]:
    tscore = 0
    totalq = len(mcq['Question'])
    for i in range(totalq):
        print(f"\nQ{i+1}: {df.loc[i, 'Question']}")
        print(f"1. {df.loc[i, 'Option1']}")
        print(f"2. {df.loc[i, 'Option2']}")
        print(f"3. {df.loc[i, 'Option3']}")
        print(f"4. {df.loc[i, 'Option4']}")
        print(f"5. {df.loc[i, 'Option5']}")
        
        ans = input("Enter the option number: ")
        while ans not in ["1", "2", "3", "4", "5"]:
            print("Invalid input! Please enter a number between 1 and 5.")
            ans = input("Enter the option number: ")
        
        ans = int(ans)
        score_column = f"Score{ans}"
        tscore += df.loc[i, score_column]
    
    print(f"\nYour total score is: {tscore}")

    fashion(5, 40)

    if tscore <= totalq * 1.5:
        rank(
            "Novice", 
            "Focus on basic syntax of your preferred programming language (loops, conditionals, etc.)", 
            "I recommend w3schools for learning the basics."
        )
    elif tscore <= totalq * 2.5:
        rank(
            "Intermediate", 
            "Master basic concepts and start learning Data Structures and Algorithms (DSA). Do more projects.", 
            "Check out algomap.io or search for beginner projects."
        )
    elif tscore <= totalq * 3.5:
        rank(
            "Advanced", 
            "Focus on mastering OOP and advanced libraries. You should have completed DSAs and projects by now.", 
            "Check out Corey Schafer's Python OOP YouTube series."
        )
    else:
        rank(
            "Expert", 
            "You seem to have a solid grip on Python. Work on advanced projects or contribute to open-source.", 
            "Explore advanced topics through real-world projects and GitHub contributions."
        )
else:
    print("Quiz canceled.")
