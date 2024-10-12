import random
import os
import time
import subprocess
from PIL import Image
from questions_set_A import questions_set_A
from questions_set_B import questions_set_B
from questions_set_C import questions_set_C
from questions_set_D import questions_set_D
from questions_set_images import questions_set_images

def ask_question(question_num, total_questions, question, options, correct_answer, description, image=None):
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
    
    answer = input("Choose the correct option (e.g., '1 4' for multiple answers), '0' to go back, or 'x' to exit: ").strip()
    
    if answer.lower() == 'x':
        return 'x', True  # Indicate exit
    if answer.lower() == '0':
        return None, False

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

    input("Press Enter to continue...")

    if image_enabled:
        subprocess.call(["osascript", "-e", 'tell application "Preview" to quit'])

    return answer, is_correct

def select_questions_set():
    print("Select the set of questions you want to answer:")
    print("1. Question Set set_A")
    print("2. Question Set set_B")
    print("3. Question Set set_C")
    print("4. Question Set set_Images")
    print("5. All Sets of Questions")
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
        questions_set_A + questions_set_B + questions_set_C + questions_set_D + questions_set_images
    else:
        print("Invalid choice. Defaulting to all sets of questions.")
        return questions_set_A + questions_set_B + questions_set_C + questions_set_D +  questions_set_images

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
    
    # Get the start question number
    start = input("Enter the starting question number (leave blank for 1): ").strip()
    if start == "":
        start = 1  # Default to the first question
    else:
        try:
            start = int(start)
            if start < 1 or start > total_questions:
                raise ValueError
        except ValueError:
            print(f"Invalid input. Starting with question 1.")
            start = 1

    # Get the end question number
    end = input(f"Enter the ending question number (leave blank for {total_questions}): ").strip()
    if end == "":
        end = total_questions  # Default to the last question
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

def main():
    global score
    global image_enabled
    score = 0
    wrong_questions = []
    global start_time
    start_time = time.time()

    selected_questions = select_questions_set()

    randomize_order = choose_ordering()
    image_enabled = enable_images()

    if randomize_order:
        random.shuffle(selected_questions)

    total_questions = len(selected_questions)
    start, end = select_question_range(total_questions)
    selected_questions = selected_questions[start-1:end]

    answers = [None] * len(selected_questions)
    current_question = 0 

    while current_question < len(selected_questions):
        q = selected_questions[current_question]
        answer, is_correct = ask_question(
            current_question + 1, 
            len(selected_questions), 
            q["question"], 
            q["options"], 
            q["correct_answer"], 
            q["description"],
            q.get("image", None)
        )
        
        if answer == 'x':
            break  # Exit the session
        
        if answer is not None:
            if answers[current_question] is None:
                if is_correct:
                    score += 1
                else:
                    wrong_questions.append(current_question)
            elif answers[current_question] != answer:
                previous_correct = answers[current_question] == str(q["correct_answer"])
                if is_correct and not previous_correct:
                    score += 1
                elif not is_correct and previous_correct:
                    score -= 1

            answers[current_question] = answer
            current_question += 1
        elif current_question > 0:
            current_question -= 1

    print(f"\nYour final score is {score}/{len(selected_questions)}")

    if wrong_questions:
        print(f"\nYou got {len(wrong_questions)} questions wrong. Would you like to try them again? (y/n)")
        retry = input().strip().lower()
        if retry == 'y':
            print("\nRepeating wrong questions...\n")
            for i in wrong_questions:
                q = selected_questions[i]
                answer, is_correct = ask_question(
                    i + 1, 
                    len(selected_questions), 
                    q["question"], 
                    q["options"], 
                    q["correct_answer"], 
                    q["description"],
                    q.get("image", None)
                )
                
                if answer == 'x':
                    break  # Exit the session
                
                if answer is not None:
                    previous_answer = answers[i]
                    previous_correct = previous_answer == str(q["correct_answer"])
                    if previous_answer != answer:
                        if is_correct and not previous_correct:
                            score += 1
                        elif not is_correct and previous_correct:
                            score -= 1
                    answers[i] = answer

            print(f"\nYour final score after retry is {score}/{len(selected_questions)}")

if __name__ == "__main__":
    main()
