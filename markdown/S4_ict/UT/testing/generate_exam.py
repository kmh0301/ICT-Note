import csv
import re

def generate_mcq_latex(data):
    """
    Generates LaTeX code for multiple-choice questions from a dictionary list.
    Handles special characters and formatting for LaTeX.
    """
    mcq_latex = ""
    for row in data:
        question_text = row['QuestionText']
        option_a = row['OptionA']
        option_b = row['OptionB']
        option_c = row['OptionC']
        option_d = row['OptionD']
        marks = row['Marks']
        
        # Escape any special characters for LaTeX
        def format_text_for_latex(text):
            text = re.sub(r'([_^%#&{}])', r'\\\1', text)
            # Handle unicode subscripts and superscripts for math mode
            text = text.replace('₀', '$_{0}$').replace('₁', '$_{1}$').replace('₂', '$_{2}$').replace('₃', '$_{3}$').replace('₄', '$_{4}$').replace('₅', '$_{5}$').replace('₆', '$_{6}$').replace('₇', '$_{7}$').replace('₈', '$_{8}$').replace('₉', '$_{9}$')
            text = text.replace('⁰', '$^{0}$').replace('¹', '$^{1}$').replace('²', '$^{2}$').replace('³', '$^{3}$').replace('⁴', '$^{4}$').replace('⁵', '$^{5}$').replace('⁶', '$^{6}$').replace('⁷', '$^{7}$').replace('⁸', '$^{8}$').replace('⁹', '$^{9}$')
            text = text.replace('≈', '$\\approx$')
            return text

        question_text = format_text_for_latex(question_text)
        option_a = format_text_for_latex(option_a)
        option_b = format_text_for_latex(option_b)
        option_c = format_text_for_latex(option_c)
        option_d = format_text_for_latex(option_d)
        
        # Generate the LaTeX string for a single MCQ item
        latex_item = f"""
    \\item {question_text} ({marks} 分)
    \\begin{{enumerate}}[label=\\Alph*.]
        \\item {option_a}
        \\item {option_b}
        \\item {option_c}
        \\item {option_d}
    \\end{{enumerate}}
    """
        mcq_latex += latex_item
    return mcq_latex

def generate_qa_latex(data):
    """
    Generates LaTeX code for long questions (Q&A) from a dictionary list.
    """
    qa_latex = ""
    # Wrap the entire long question section in a single enumerate environment
    qa_latex += """\\begin{enumerate}\n"""
    
    for row in data:
        question_text = row['QuestionText']
        marks = row['Marks']
        
        # Generate the main question item
        qa_latex += f"\\item {question_text} ({marks} 分)\n"
        
        # Start a single enumerate environment for all sub-questions within this main question
        qa_latex += """\\begin{enumerate}[label=(\\alph*)]\n"""
        
        # Iterate through sub-questions (assuming a maximum of 5 sub-questions)
        for i in range(1, 6):
            sub_question_key = f'SubQuestion{i}'
            sub_marks_key = f'SubMarks{i}'
            
            if row.get(sub_question_key):
                sub_question_text = row[sub_question_key]
                sub_marks = row[sub_marks_key]
                
                qa_latex += f"    \\item {sub_question_text} ({sub_marks}分)\n"

        # End the sub-question enumerate environment
        qa_latex += "\\end{enumerate}\n"
    
    # End the main enumerate environment for all long questions
    qa_latex += """\\end{enumerate}\n"""
    
    return qa_latex


def generate_exam_file(template_file, mcq_csv, qa_csv, output_file):
    """
    Main function to read two CSVs, generate LaTeX content, and create the final exam file.
    """
    try:
        with open(mcq_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            mcq_data = list(reader)
        mcq_latex_content = generate_mcq_latex(mcq_data)

        with open(qa_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            qa_data = list(reader)
        qa_latex_content = generate_qa_latex(qa_data)

        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()

        final_latex_content = template_content.replace("\\questionsplacehodler", mcq_latex_content)
        final_latex_content = final_latex_content.replace("\\qaquestionsplacehodler", qa_latex_content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_latex_content)
        
        print(f"✅ 成功生成 {output_file}")
        
    except FileNotFoundError:
        print("❌ 錯誤：找不到其中一個文件。請檢查文件路徑和檔名。")
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    generate_exam_file(
        template_file='exam_template.tex',
        mcq_csv='mcq.csv',
        qa_csv='Lq.csv',
        output_file='exam_generated.tex'
    )