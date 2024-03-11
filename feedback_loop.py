def analyze_feedback(feedback_file):
    feedback_data = []
    feedback_entry = {}

    try:
        with open(feedback_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('User input:'):
                    feedback_entry['user_input'] = line.split(':', 1)[1].strip()
                elif line.startswith('Input prompt:'):
                    feedback_entry['input_prompt'] = line.split(':', 1)[1].strip()
                elif line.startswith('Generated code:'):
                    feedback_entry['generated_code'] = line.split(':', 1)[1].strip()
                elif line.startswith('Feedback'):
                    feedback_entry['Feedback'] = line.split(':', 1)[1].strip()
                    # Append the feedback entry to the list
                    feedback_data.append(feedback_entry)
                    # Reset the feedback entry dictionary for the next entry
                    feedback_entry = {}
                
    except FileNotFoundError:
        print(f"Error: File '{feedback_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return feedback_data
# Example usage

if __name__ == "__main__":
# Example usage
    feedback_file = 'static/feedback.log'
    feedback_analysis = analyze_feedback(feedback_file)
    print(feedback_analysis)
    
