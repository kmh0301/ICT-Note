import csv

def generate_ut_markdown():
    """Generates the UT.md file from mcq.csv and Lq.csv."""
    
    # Define a dictionary to store specific answer box heights for long questions
    lq_formats = {
        '1': ['answer-space', 'answer-space', 'answer-space'],
        '2': {
            'a': 'answer-space',
            'b': '<div class="answer-box"><div style="height: 3em;"></div></div>',
            'c': '<div class="answer-box"><div style="height: 3em;"></div></div>'
        },
        '3': {
            'a': '<div class="answer-box"><div style="height: 4em;"></div></div>',
            'b': '<div class="answer-box"><div style="height: 4em;"></div></div>',
            'c': '<div class="answer-box"><div style="height: 6em;"></div></div>'
        },
        '4': ['answer-space'],
        '5': ['answer-space']
    }

    with open('UT.md', 'w', encoding='utf-8') as md_file:
        # Write the YAML frontmatter
        md_file.write("---\n")
        md_file.write("marp: true\n")
        md_file.write("theme: UT\n")
        md_file.write("class: title-page\n")
        md_file.write("paginate: false\n")
        md_file.write("backgroundColor: white\n")
        md_file.write("---\n\n")

        # Write the title page
        md_file.write("# **佛教黃鳳翎中學**\n\n")
        md_file.write("# **2025/2026 上學期統測**\n\n")
        md_file.write("---\n\n")

        # Write the Multiple-Choice (MCQ) section
        md_file.write('<div class="section-title"><strong>甲部 多項選擇題（20分）</strong></div>\n')
        md_file.write('<strong>本部共有20題。請選擇最合適的答案。</strong>\n\n')

        try:
            with open('mcq.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    question_id = row['QuestionID']
                    question_text = row['QuestionText']
                    marks = row['Marks']
                    
                    # Add a divider after every 5 questions for visual break
                    if int(question_id) > 1 and int(question_id) % 5 == 1:
                        md_file.write('---\n\n')

                    md_file.write(f'<div class="question-item">{question_id}. {question_text} <span class="points">({marks} 分)</span></div>\n')
                    md_file.write('<ul class="mcq-options">\n')
                    md_file.write(f'<li>{row["OptionA"]}</li>\n')
                    md_file.write(f'<li>{row["OptionB"]}</li>\n')
                    md_file.write(f'<li>{row["OptionC"]}</li>\n')
                    md_file.write(f'<li>{row["OptionD"]}</li>\n')
                    md_file.write('</ul>\n\n')
        except FileNotFoundError:
            print("Error: 'mcq.csv' not found.")
            return

        # Write the Long-Answer (LQ) section
        md_file.write('---\n\n')
        md_file.write('<div class="section-title"><strong>乙部 問答題（30分）</strong></div>\n')
        md_file.write('<strong>本部共有5題。請在適當的答案框內作答。</strong>\n\n')

        try:
            with open('Lq.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    question_id = row['QuestionID']
                    question_text = row['QuestionText']
                    total_marks = row['Marks']
                    
                    md_file.write('---\n\n')
                    md_file.write(f'<div class="question-item">{question_id}. {question_text} <span class="points">({total_marks} 分)</span></div>\n\n')

                    # Handle long questions with sub-questions
                    sub_questions = {
                        'a': {'text': row['SubQuestion1'], 'marks': row['SubMarks1']},
                        'b': {'text': row['SubQuestion2'], 'marks': row['SubMarks2']},
                        'c': {'text': row['SubQuestion3'], 'marks': row['SubMarks3']}
                    }

                    for letter, sub in sub_questions.items():
                        if sub['text']:
                            md_file.write(f'<div class="sub-question-item">({letter}) {sub["text"]} <span class="points">({sub["marks"]}分)</span></div>\n')
                            
                            # Use hardcoded formats for answer spaces
                            if question_id in lq_formats and letter in lq_formats[question_id]:
                                md_file.write(lq_formats[question_id][letter] + '\n')
                            elif question_id in lq_formats and type(lq_formats[question_id]) is list:
                                for _ in range(3): # Default to 3 answer lines
                                    md_file.write('<div class="answer-space"></div>\n')
                            else:
                                md_file.write('<div class="answer-box"><div style="height: 3em;"></div></div>\n')

                            md_file.write('\n')

        except FileNotFoundError:
            print("Error: 'Lq.csv' not found.")
            return

    print("Successfully generated UT.md!")

# Run the script
if __name__ == "__main__":
    generate_ut_markdown()