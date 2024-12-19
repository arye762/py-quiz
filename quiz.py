import random
import os
import datetime
import time
import json
import subprocess
#from PIL import Image
from questions_set_A import questions_set_A
from questions_set_B import questions_set_B
from questions_set_C import questions_set_C
from questions_set_D import questions_set_D
from questions_set_images import questions_set_images

SAVE_FILE = "quiz_save.json"
FLAGGED_FILE = "flagged_questions.json"

def ask_question(question_num, total_questions, question, options, correct_answer, description, image=None, flagged_questions=None):
    os.system('clear')  # Clear the screen before each question

    print(f"Score: {score} | Time: {time_elapsed()}")

    indices = list(range(len(options)))
    random.shuffle(indices)
    shuffled_options = [options[i] for i in indices]

    if isinstance(correct_answer, list):
        shuffled_correct_answer = [indices.index(ans - 1) + 1 for ans in correct_answer]
    else:
        shuffled_correct_answer = indices.index(correct_answer - 1) + 1

    print(f"\nQuestion {question_num} of {total_questions}\n")
    print(f"{question}\n")

    if image and image_enabled:
        try:
            print(f"Loading image: {image}")

            subprocess.call(["osascript", "-e", 'tell application "Preview" to quit'])
            subprocess.call(["open", image])
            time.sleep(1)
            subprocess.call(["osascript", "-e", 'tell application "Terminal" to activate'])

        except Exception as e:
            print(f"Error loading image: {e}")

    for idx, option in enumerate(shuffled_options, 1):
        print(f"{idx}. {option}")
    print()

    answer = input("Choose the correct option (e.g., '1 4' for multiple answers), '0' to go back, 'x' to exit, 'f' to flag: ").strip()

    if answer.lower() == 'x':
        return 'x', False  # Indicate exit without saving here
    if answer.lower() == '0':
        return None, False  
    if answer.lower() == 'f':  # Flag question
        flagged_questions.append({
            "question": question,
            "options": options,
            "correct_answer": correct_answer,
            "description": description,
            "image": image
        })
        with open("flagged_questions.json", "w") as f:
            json.dump(flagged_questions, f)
        print("Question flagged and saved!\n")
        input("Press Enter to continue to the next question...")  # Ensures it continues after flagging
        return 'f', False  # Return flag indicator without marking answer as correct or wrong

    try:
        user_answers = list(map(int, answer.split()))
    except ValueError:
        print("\nInvalid input. Please enter numbers separated by spaces.\n")
        return None, False

    correct_text = [options[i - 1] for i in correct_answer] if isinstance(correct_answer, list) else options[correct_answer - 1]
    is_correct = sorted(user_answers) == sorted(shuffled_correct_answer) if isinstance(correct_answer, list) else user_answers == [shuffled_correct_answer]
    
    if is_correct:
        print("\nCorrect!\n")
    else:
        print("\nWrong!\n")
        print(f"The correct answer is: {correct_text}\n")
    
    print(f"Description: {description}\n")

    input("Press Enter to continue to the next question...")  # Ensures it moves to the next question

    if image_enabled:
        subprocess.call(["osascript", "-e", 'tell application "Preview" to quit'])

    return answer, is_correct



def select_questions_set():
    print("Select the set of questions you want to answer:")
    print("1. Question Set A")
    print("2. Question Set B")
    print("3. Question Set C")
    print("4. Question Set D")
    print("5. Question Set Images")
    print("6. All Sets of Questions")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        return questions_set_A
    elif choice == '2':
        return questions_set_B
    elif choice == '3':
        return questions_set_C
    elif choice == '4':
        return questions_set_D
    elif choice == '5':
        return questions_set_images
    elif choice == '6':
        return questions_set_A + questions_set_B + questions_set_C + questions_set_D + questions_set_images
    else:
        print("Invalid choice. Defaulting to all sets of questions.")
        return questions_set_A + questions_set_B + questions_set_C + questions_set_D + questions_set_images

def choose_ordering():
    print("\nHow would you like the questions to be ordered?")
    print("1. Randomized")
    print("2. In Order")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        return True  # Randomize
    elif choice == '2':
        return False  # In order
    else:
        print("Invalid choice. Defaulting to in order.")
        return False

def enable_images():
    print("\nWould you like to enable images in the questions?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        return True
    elif choice == '2':
        return False
    else:
        print("Invalid choice. Defaulting to images disabled.")
        return False

def select_question_range(total_questions):
    print(f"\nSelect the range of questions you want to be asked (1-{total_questions}):")
    
    start = input("Enter the starting question number (leave blank for 1): ").strip()
    if start == "":
        start = 1
    else:
        try:
            start = int(start)
            if start < 1 or start > total_questions:
                raise ValueError
        except ValueError:
            print(f"Invalid input. Starting with question 1.")
            start = 1

    end = input(f"Enter the ending question number (leave blank for {total_questions}): ").strip()
    if end == "":
        end = total_questions
    else:
        try:
            end = int(end)
            if end < start or end > total_questions:
                raise ValueError
        except ValueError:
            print(f"Invalid input. Ending with question {total_questions}.")
            end = total_questions

    return start, end

def time_elapsed():
    elapsed_time = time.time() - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def save_session(wrong_questions=None):
    """
    Save the session to a file, including wrong questions if provided.
    """
    session_data = {
        "score": score,
        "current_question": current_question,
        "answers": answers,
        "start_time": start_time,
        "selected_questions": selected_questions,  # Save the selected questions
        "image_enabled": image_enabled,  # Save the image setting
    }
    if wrong_questions is not None:
        session_data["wrong_questions"] = wrong_questions  # Save wrong questions for retry

    with open(SAVE_FILE, "w") as f:
        json.dump(session_data, f)
    print("\nSession saved successfully!\n")



def load_session():
    global score, current_question, answers, start_time, selected_questions, image_enabled
    try:
        with open(SAVE_FILE, "r") as f:
            session_data = json.load(f)
        score = session_data["score"]
        current_question = session_data["current_question"]
        answers = session_data["answers"]
        start_time = session_data["start_time"]
        selected_questions = session_data["selected_questions"]
        image_enabled = session_data.get("image_enabled", False)  # Load the image setting
        print("\nSession loaded successfully!\n")
        return True
    except FileNotFoundError:
        print("\nNo saved session found.\n")
        return False


def load_session():
    global score, current_question, answers, start_time, selected_questions, image_enabled
    try:
        with open(SAVE_FILE, "r") as f:
            session_data = json.load(f)
        score = session_data["score"]
        current_question = session_data["current_question"]
        answers = session_data["answers"]
        start_time = session_data["start_time"]
        selected_questions = session_data["selected_questions"]
        image_enabled = session_data.get("image_enabled", False)
        print("\nSession loaded successfully!\n")
        return session_data  # Return session data for flexibility
    except FileNotFoundError:
        print("\nNo saved session found.\n")
        return None

def retry_flagged_questions(flagged_questions):
    """
    Allows the user to retry flagged questions and remove them if desired.
    """
    global score

    if not flagged_questions:
        print("\nNo flagged questions to retry.\n")
        return

    for idx, q in enumerate(flagged_questions):
        print(f"\nReviewing flagged question {idx + 1} of {len(flagged_questions)}")
        answer, is_correct = ask_question(
            idx + 1,
            len(flagged_questions),
            q["question"],
            q["options"],
            q["correct_answer"],
            q["description"],
            q.get("image", None),
        )

        if answer.lower() == 'x':
            break

        if is_correct:
            score += 1
            print("Correct! Well done!")
            remove_flagged_question(flagged_questions, idx)  # Remove from flagged list
        else:
            print("Still incorrect. Keep practicing!")

    with open("flagged_questions.json", "w") as f:
        json.dump(flagged_questions, f)

def remove_flagged_question(flagged_questions, index):
    """
    Removes a flagged question from the list if the user chooses to.
    """
    print("Do you want to remove this question from the flagged list? (y/n): ", end="")
    if input().strip().lower() == 'y':
        flagged_questions.pop(index)


def save_flagged_questions(flagged_questions):
    with open(FLAGGED_FILE, "w") as f:
        json.dump(flagged_questions, f)
    print("\nFlagged questions saved successfully!\n")

def load_flagged_questions():
    try:
        with open(FLAGGED_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

<<<<<<< Updated upstream
    # Initialize variables
    score = 0
    current_question = 0
    answers = []
    start_time = time.time()
    selected_questions = []
    image_enabled = False
    flagged_questions = []

    print("Welcome to the Quiz!")
    print("1. Start a New Quiz")
    print("2. Retry Wrong Answers")
    print("3. Resume Last Session")
    print("4. Retry Flagged Questions")  # New option to retry flagged questions
    print("5. Exit")
    
    choice = input("Choose an option: ").strip()
    
    if choice == '2':  # Retry wrong answers
        session_data = load_session()
        if session_data and "wrong_questions" in session_data:
            retry_wrong_answers(session_data["wrong_questions"])
        else:
            print("\nNo saved wrong questions found. Starting a new session.\n")
        return

    elif choice == '3':  # Resume the last session
        session_data = load_session()
        if session_data:
            score = session_data["score"]
            current_question = session_data["current_question"]
            answers = session_data["answers"]
            start_time = session_data["start_time"]
            selected_questions = session_data["selected_questions"]
            image_enabled = session_data.get("image_enabled", False)
        else:
            print("\nNo saved session found. Starting a new session.\n")

    elif choice == '4':  # Retry flagged questions
        with open("flagged_questions.json", "r") as f:
            flagged_questions = json.load(f)
        
        if flagged_questions:
            retry_flagged_questions(flagged_questions)
        else:
            print("\nNo flagged questions found.\n")
        return

    elif choice == '5':  # Exit
        print("Goodbye!")
        return

    else:  # Start a new quiz
        selected_questions = select_questions_set()
        randomize_order = choose_ordering()
        image_enabled = enable_images()

        if randomize_order:
            random.shuffle(selected_questions)

        total_questions = len(selected_questions)
        start, end = select_question_range(total_questions)
        selected_questions = selected_questions[start - 1:end]
        answers = [None] * len(selected_questions)

    # Initialize wrong questions list
    wrong_questions = []

    # Main quiz loop
    while current_question < len(selected_questions):
        q = selected_questions[current_question]
=======
def retry_flagged_questions():
    flagged_questions = load_flagged_questions()
    if not flagged_questions:
        print("\nNo flagged questions to review.\n")
        return

    print("\nReviewing flagged questions:\n")
    for idx, q in enumerate(flagged_questions[:]):
        print(f"\nQuestion {idx + 1} of {len(flagged_questions)}:")
>>>>>>> Stashed changes
        answer, is_correct = ask_question(
            idx + 1,
            len(flagged_questions),
            q["question"],
            q["options"],
            q["correct_answer"],
            q["description"],
            q.get("image", None),
            flagged_questions  # Pass the flagged_questions list
        )

        if input("Remove this question from flagged list? (y to remove, Enter to keep): ").strip().lower() == 'y':
            flagged_questions.remove(q)

    save_flagged_questions(flagged_questions)
    print("\nFlagged questions updated.\n")

def retry_wrong_answers(wrong_questions):
    global score

    if not wrong_questions:
        print("\nGreat job! You didn't get any questions wrong.\n")
        return

    flagged_questions = load_flagged_questions()

    print("\nRetrying wrong answers:\n")
    for idx, q in enumerate(wrong_questions):
        print(f"\nRetrying question {idx + 1} of {len(wrong_questions)}:")
        answer, is_correct = ask_question(
            idx + 1,
            len(wrong_questions),
            q["question"],
            q["options"],
            q["correct_answer"],
            q["description"],
            q.get("image", None),
        )

        if is_correct:
            score += 1
            print("Correct! Well done!")
        else:
            print("Still incorrect. Keep practicing!")

            if input("Flag this question for later review? (y/n): ").strip().lower() == 'y':
                if q not in flagged_questions:
                    flagged_questions.append(q)

    save_flagged_questions(flagged_questions)

def main():
    global score, current_question, answers, start_time, image_enabled, selected_questions

    score = 0
    current_question = 0
    answers = []
    start_time = time.time()
    selected_questions = []
    image_enabled = False

    while True:
        print("\nWelcome to the Quiz!")
        print("1. Start a New Quiz")
        print("2. Retry Wrong Answers")
        print("3. Resume Last Session")
        print("4. Retry Flagged Questions")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '2':  # Retry wrong answers
            session_data = load_session()
            if session_data and "wrong_questions" in session_data:
                retry_wrong_answers(session_data["wrong_questions"])
            else:
                print("\nNo saved wrong questions found.\n")

        elif choice == '3':  # Resume the last session
            session_data = load_session()
            if session_data:
                score = session_data["score"]
                current_question = session_data["current_question"]
                answers = session_data["answers"]
                start_time = session_data["start_time"]
                selected_questions = session_data["selected_questions"]
                image_enabled = session_data.get("image_enabled", False)
            else:
                print("\nNo saved session found.\n")

        elif choice == '4':  # Retry flagged questions
            retry_flagged_questions()

        elif choice == '5':  # Exit
            print("Goodbye!")
            break

        else:  # Start a new quiz
            selected_questions = select_questions_set()
            randomize_order = choose_ordering()
            image_enabled = enable_images()

            if randomize_order:
                random.shuffle(selected_questions)

            total_questions = len(selected_questions)
            start, end = select_question_range(total_questions)
            selected_questions = selected_questions[start - 1:end]
            answers = [None] * len(selected_questions)

            wrong_questions = []
            while current_question < len(selected_questions):
                q = selected_questions[current_question]
                answer, is_correct = ask_question(
                    current_question + 1,
                    len(selected_questions),
                    q["question"],
                    q["options"],
                    q["correct_answer"],
                    q["description"],
                    q.get("image", None),
                )

                if answer == 'x':  # Exit
                    save_session(wrong_questions)
                    return

                if not is_correct:
                    wrong_questions.append(q)

                current_question += 1

            save_session(wrong_questions)




if __name__ == "__main__":
    main()