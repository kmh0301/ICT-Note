import csv

def generate_ut_markdown():
    """Generates the UT.md file from mcq.csv and Lq.csv."""
    
    # Define a dictionary to store specific answer box heights for long questions
    lq_formats = {
        '1': {
            'a': '<div class="answer-box"><div style="height: 4em;"></div></div>',
            'b': '<div class="answer-box"><div style="height: 3em;"></div></div>',
            'c': '<div class="answer-box"><div style="height: 3em;"></div></div>'
        },
        '2': {
            'a': '<div class="answer-box"><div style="height: 4em;"></div></div>',
            'b': '<div class="answer-box"><div style="height: 3em;"></div></div>',
            'c': '<div class="answer-box"><div style="height: 3em;"></div></div>'
        },
        '3': {
            'a': '<div class="answer-box"><div style="height: 4em;"></div></div>',
            'b': '<div class="answer-box"><div style="height: 3em;"></div></div>',
            'c': '<div class="answer-box"><div style="height: 3em;"></div></div>',
            'd': '<div class="answer-box"><div style="height: 3em;"></div></div>'
        },
        '4': {
            'a': '<div class="answer-box"><div style="height: 3em;"></div></div>',
            'b': '<div class="answer-box"><div style="height: 4em;"></div></div>'
        },
        '5': {
            'a': '<div class="answer-box"><div style="height: 6em;"></div></div>'
        }
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
            with open('MCQ.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                question_counter = 1
                
                for row in reader:
                    # Skip empty rows
                    if not row.get('QuestionText', '').strip():
                        continue
                    
                    # Extract data from the CSV format
                    question_text = row['QuestionText']
                    option_a = row['OptionA']
                    option_b = row['OptionB']
                    option_c = row['OptionC']
                    option_d = row['OptionD']
                    marks = row['Marks']
                    
                    # Add a divider after every 5 questions for visual break
                    if question_counter > 1 and question_counter % 5 == 1:
                        md_file.write('---\n\n')

                    md_file.write(f'<div class="question-item">{question_counter}. {question_text} <span class="points">({marks} 分)</span></div>\n')
                    md_file.write('<ul class="mcq-options">\n')
                    md_file.write(f'<li>{option_a}</li>\n')
                    md_file.write(f'<li>{option_b}</li>\n')
                    md_file.write(f'<li>{option_c}</li>\n')
                    md_file.write(f'<li>{option_d}</li>\n')
                    md_file.write('</ul>\n\n')
                    
                    question_counter += 1
                    
        except FileNotFoundError:
            print("Error: 'MCQ.csv' not found.")
            return
        except KeyError as e:
            print(f"Error: Missing column in MCQ.csv: {e}")
            return

        # Write the Long-Answer (LQ) section
        md_file.write('---\n\n')
        md_file.write('<div class="section-title"><strong>乙部 問答題（30分）</strong></div>\n')
        md_file.write('<strong>本部共有5題。請在適當的答案框內作答。</strong>\n\n')

        try:
            with open('LQ.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    # Skip empty rows
                    if not row.get('QuestionText', '').strip():
                        continue
                    
                    # Extract question ID from QuestionIDwithQuestionyears (e.g., "2016-1-1" -> "1")
                    question_id_full = row['QuestionIDwithQuestionyears']
                    question_id = question_id_full.split('-')[-1] if question_id_full else '1'
                    question_text = row['QuestionText']
                    total_marks = row['Marks']
                    
                    md_file.write('---\n\n')
                    md_file.write(f'<div class="question-item">{question_id}. {question_text} <span class="points">({total_marks} 分)</span></div>\n\n')

                    # Handle long questions with sub-questions (up to 8 sub-questions)
                    sub_questions = []
                    for i in range(1, 9):  # SubQuestion1 to SubQuestion8
                        sub_text = row.get(f'SubQuestion{i}', '') or ''
                        sub_marks = row.get(f'SubMarks{i}', '') or ''
                        sub_text = sub_text.strip() if sub_text else ''
                        sub_marks = sub_marks.strip() if sub_marks else ''
                        
                        if sub_text:
                            sub_questions.append({
                                'text': sub_text,
                                'marks': sub_marks,
                                'index': i
                            })

                    for idx, sub in enumerate(sub_questions):
                        # Use letters for sub-question labeling (a, b, c, d, e, f, g, h)
                        letter = chr(ord('a') + idx)
                        
                        md_file.write(f'<div class="sub-question-item">{sub["text"]} <span class="points">({sub["marks"]}分)</span></div>\n')
                        
                        # Use hardcoded formats for answer spaces
                        if question_id in lq_formats and letter in lq_formats[question_id]:
                            md_file.write(lq_formats[question_id][letter] + '\n')
                        else:
                            # Default answer box based on marks
                            marks_value = int(sub["marks"]) if sub["marks"] and sub["marks"].isdigit() else 2
                            if marks_value >= 4:
                                height = "5em"
                            elif marks_value >= 2:
                                height = "4em"
                            else:
                                height = "3em"
                            md_file.write(f'<div class="answer-box"><div style="height: {height};"></div></div>\n')

                        md_file.write('\n')

        except FileNotFoundError:
            print("Note: 'LQ.csv' not found. Skipping long questions section.")
        except KeyError as e:
            print(f"Error: Missing column in LQ.csv: {e}")

    print("Successfully generated UT.md!")

# Run the script
if __name__ == "__main__":
    generate_ut_markdown()