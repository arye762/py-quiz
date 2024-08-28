import ast
import pprint

def remove_duplicates(questions):
    seen_questions = set()
    unique_questions = []

    for question in questions:
        # Create a unique identifier based on the question and options
        question_id = (question['question'].strip().lower(), tuple(sorted(option.strip().lower() for option in question['options'])))

        if question_id not in seen_questions:
            seen_questions.add(question_id)
            unique_questions.append(question)

    return unique_questions

def remove_duplicates_from_file(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    # Extract the list of questions from the content
    try:
        start = content.find('[')
        end = content.rfind(']')
        question_list_str = content[start:end+1]
        questions = ast.literal_eval(question_list_str)  # Using ast.literal_eval instead of json.loads
    except Exception as e:
        print(f"Error parsing the input file: {e}")
        return

    # Remove duplicates
    cleaned_questions = remove_duplicates(questions)

    # Save the cleaned list of questions to a new file with better formatting
    with open(output_file, 'w') as f:
        f.write("questions_701_B = [\n")
        for question in cleaned_questions:
            f.write(pprint.pformat(question, indent=4))
            f.write(",\n")
        f.write("]\n")

    print(f"Removed duplicates. The cleaned question set is saved to {output_file}.")


# Example usage:
input_file = 'questions_701_B.py'  # Replace with your actual file name
output_file = 'cleaned_questions.py'  # This file will contain the deduplicated questions

remove_duplicates_from_file(input_file, output_file)
