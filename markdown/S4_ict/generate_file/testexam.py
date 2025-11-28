import csv
import subprocess
import sys
import os
import glob
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION_START
from docx import Document # Import Document for DOCX generation

# --- CONFIGURATION ---
CSV_FOLDER = '/Users/sallypang/Documents/GitHub/ICT-Note/markdown/S4_ict/generate_file/csv'
RESULT_FOLDER = '/Users/sallypang/Documents/GitHub/ICT-Note/markdown/S4_ict/generate_file/result'
# --- END CONFIGURATION ---

# --- Utility Functions (keep as is) ---
def choose_csv_file(prompt="Select CSV file"):
    # ... (Implementation remains the same)
    csv_files = glob.glob(os.path.join(CSV_FOLDER, '*.csv'))
    csv_names = [os.path.basename(f) for f in csv_files]
    if not csv_names:
        print("No CSV files found in the folder.")
        sys.exit(1)
    print(f"\n{prompt}:")
    for idx, fname in enumerate(csv_names, 1):
        print(f"  {idx}. {fname}")
    while True:
        choice = input("Enter file name (e.g., MCQ.csv): ").strip()
        if choice in csv_names:
            return os.path.join(CSV_FOLDER, choice)
        print("Not found - please type one of the names above.")

def load_lq_answers(lq_answers_path):
    # ... (Implementation remains the same)
    lq_answers = {}
    if not lq_answers_path or not os.path.exists(lq_answers_path):
        # print("Note: LQ_Answers.csv not found. Long question answers will not be displayed.")
        return lq_answers
    try:
        with open(lq_answers_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                question_id = row.get('QuestionIDwithQuestionyears', '')
                if question_id:
                    answers = {}
                    for i in range(1, 9):
                        answer_key = f'SubAnswer{i}'
                        if answer_key in row and row[answer_key].strip():
                            answers[i] = row[answer_key].strip()
                    if answers:
                        lq_answers[question_id] = answers
    except Exception as e:
        print(f"Error reading LQ answers: {e}")
    return lq_answers

def install_required_packages():
    # ... (Implementation remains the same)
    packages_to_install = []
    try:
        import docx
        print("✓ python-docx is already installed")
    except ImportError:
        packages_to_install.append('python-docx')
    for package in packages_to_install:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install {package}")
            print("Please try installing manually: pip3 install python-docx")
            return False
    return True

# --- CORE FUNCTION 1: Get User Preferences (Updated) ---
def get_user_preferences():
    """Gets user configuration for exercise generation, including exam details."""
    print("\n=== ICT Exercise Generator Configuration ===")
    
    # 1. Output Preferences
    print("\nPlease choose what to include in your exercise files:")
    while True:
        show_source = input("Show source information (year, chapter, topic)? (y/n): ").lower().strip()
        if show_source in ['y', 'yes', 'n', 'no']:
            show_source_info = show_source in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no")
    while True:
        show_answer = input("Show answers? (y/n): ").lower().strip()
        if show_answer in ['y', 'yes', 'n', 'no']:
            show_answers = show_answer in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no")
    if not show_answers:
        while True:
            show_space = input("Show answer spaces for long questions? (y/n): ").lower().strip()
            if show_space in ['y', 'yes', 'n', 'no']:
                show_answer_spaces = show_space in ['y', 'yes']
                break
            print("Please enter 'y' for yes or 'n' for no")
    else:
        show_answer_spaces = False
        
    # 2. Exam Details (NEW INPUTS)
    print("\n--- Exam Paper Details ---")
    exam_duration_input = input("Enter Exam Duration (e.g., 40 分鐘): ").strip()
    exam_date_input = input("Enter Exam Date (e.g., 2024年2月29日): ").strip()
    total_marks_input = input("Enter Total Marks (e.g., 50 分): ").strip()
        
    # 3. Compile Preferences
    preferences = {
        'show_source_info': show_source_info,
        'show_answers': show_answers,
        'show_answer_spaces': show_answer_spaces,
        # Store user input formatted for display
        'exam_duration': f"考試時間：{exam_duration_input}",
        'exam_date': f"考試日期：{exam_date_input}",
        'total_marks': f"總分: {total_marks_input}"
    }
    
    # 4. Print Summary
    print(f"\n📋 Your preferences:")
    print(f"  • Source info: {'Yes' if show_source_info else 'No'}")
    print(f"  • Show answers: {'Yes' if show_answers else 'No'}")
    print(f"  • Answer spaces: {'Yes' if show_answer_spaces else 'No'}")
    print(f"  • Duration: {preferences['exam_duration']}")
    print(f"  • Date: {preferences['exam_date']}")
    print(f"  • Total Marks: {preferences['total_marks']}")
    return preferences

# --- CORE FUNCTION 2: Generate Markdown (Updated) ---
def generate_exercise_markdown(preferences, mcq_csv_path, lq_csv_path, lq_answers_path):
    """
    Generates the Exercise.md file using Marp format, matching the layout of the PDF front page.
    """
    import os
    lq_answers = load_lq_answers(lq_answers_path)
    markdown_path = os.path.join(RESULT_FOLDER, 'Exercise.md')
    
    # --- Configuration (using preferences for dynamic parts) ---
    SCHOOL_NAME = "佛教黃鳳翎中學"
    EXAM_TITLE = "2025/2026 上學期考試"
    SUBJECT = "中四級資訊及通訊科技"
    ANSWER_BOOK = "試題答題簿"
    
    # Static details from PDF source
    EXAM_DATE_LINE = "考試日期:2026年月日"
    EXAM_TIME_LINE = "考試時間:8:30 - 9:30"
    DURATION_LINE = "時限:30分鐘"
    TOTAL_MARKS_LINE = "總分"
    
    # --- End Configuration ---

    try:
        with open(markdown_path, 'w', encoding='utf-8') as md_file:
            # --- YAML frontmatter ---
            md_file.write("---\n")
            md_file.write("marp: true\n")
            md_file.write("theme: testexam\n") # IMPORTANT: Using the new theme name
            md_file.write("class: title-page\n") 
            md_file.write("paginate: false\n")
            md_file.write("backgroundColor: white\n")
            md_file.write("---\n\n")

            # --- Slide 1: Custom Exam Front Page (Matching PDF Structure) ---
            
            title_suffix = ""
            if preferences['show_answers']:
                title_suffix = " (答案版)"

            # 1. Header (School Name)
            md_file.write(f'<div class="school-name">{SCHOOL_NAME}</div>\n') 
            
            # 2. Main Title and Subject
            md_file.write(f'<div class="exam-title-main">{EXAM_TITLE}</div>\n') 
            md_file.write(f'<div class="subject-title">{SUBJECT}</div>\n') 
            md_file.write(f'<div class="answer-book">{ANSWER_BOOK}</div>\n\n') 
            
            # 3. Student Info (Left aligned text)
            md_file.write('<div class="student-info-block">\n')
            md_file.write('  <p class="info-line">班別: _______________</p>\n') 
            md_file.write('  <p class="info-line">班號: _______________</p>\n')
            md_file.write('  <p class="info-line">姓名: _______________</p>\n')
            md_file.write('</div>\n\n')

            # 4. Dates and Total Marks (Right aligned text)
            md_file.write('<div class="date-marks-block">\n')
            md_file.write(f'  <p class="date-line">{EXAM_DATE_LINE}</p>\n')
            md_file.write(f'  <p class="date-line">{EXAM_TIME_LINE}</p>\n')
            md_file.write(f'  <p class="date-line">{DURATION_LINE}</p>\n')
            # Use a two-column structure for Total Marks/Total Score box
            md_file.write('  <table><tr>\n')
            md_file.write(f'    <td class="total-marks-label">{TOTAL_MARKS_LINE}</td>\n')
            md_file.write('    <td class="score-box"></td>\n')
            md_file.write('  </tr></table>\n')
            md_file.write('</div>\n\n')

            # 5. Candidate Instructions Block
            md_file.write('<div class="instructions-title">考生須知:</div>\n')
            md_file.write('<ol class="instructions-list">\n')
            md_file.write('  <li>在本試題簿及答題紙上的適當位置,填寫姓名、班別及班號。</li>\n')
            md_file.write('  <li>本卷分甲、乙兩部。\n')
            md_file.write('    <ul>\n')
            md_file.write('      <li>甲部為多項選擇題</li>\n')
            md_file.write('      <li>乙部為問答題\n')
            md_file.write('    </ul>\n')
            md_file.write('  </li>\n')
            md_file.write(f'  <li>全卷總分為{TOTAL_MARKS_LINE}分。</li>\n')
            md_file.write('  <li>甲部的答案須填畫在多項選擇題的答題紙上，而乙部的答案則須寫在試題答題簿中預留的空位內。</li>\n')
            md_file.write('</ol>\n')
            
            md_file.write("---\n\n") # Start next slide
            
            # --- MCQ Section Title ---
            md_file.write('\n')
            md_file.write('<div class="section-title">**甲部 多項選擇題**</div>\n')
            md_file.write('**請選擇最合適的答案。**\n\n')
            md_file.write("---\n\n") 
            
            # --- MCQ Questions Logic (rest remains the same) ---
            try:
                with open(mcq_csv_path, 'r', encoding='utf-8') as csv_file:
                    reader = csv.DictReader(csv_file)
                    question_counter = 1
                    for row in reader:
                        if not row.get('QuestionText', '').strip():
                            continue
                        # ... (rest of MCQ logic) ...
                        question_id_with_years = row.get('QuestionIDwithQuestionyears', '')
                        book_chapter = row.get('book_chapter', '')
                        topics = row.get('topics', '')
                        year = question_id_with_years.split('-')[0] if question_id_with_years else ''
                        question_text = row['QuestionText']
                        option_a = row['OptionA']
                        option_b = row['OptionB']
                        option_c = row['OptionC']
                        option_d = row['OptionD']
                        marks = row['Marks']
                        correct_answer = row.get('answer', '').upper() if preferences['show_answers'] else ''
                        
                        if question_counter > 1:
                             md_file.write('---\n')
                        
                        if preferences['show_source_info']:
                            source_info = f"({year}_{question_id_with_years}_{book_chapter}_{topics})"
                            md_file.write(f'<p style="font-size: 0.7em; color: gray;">{source_info}</p>\n') 
                        
                        md_file.write(f'## **{question_counter}. {question_text}** <span class="points">({marks} 分)</span>\n')
                        
                        options = [('A', option_a), ('B', option_b), ('C', option_c), ('D', option_d)]
                        md_file.write('<ul>\n') 
                        for letter, option_text in options:
                            if preferences['show_answers'] and letter == correct_answer:
                                md_file.write(f'<li style="color: red; font-weight: bold;">{option_text} ✓</li>\n')
                            else:
                                md_file.write(f'<li>{option_text}</li>\n')
                        md_file.write('</ul>\n\n')
                        
                        question_counter += 1
                        
            except FileNotFoundError:
                print(f"Error: File {mcq_csv_path} not found.")
                return False
            except KeyError as e:
                print(f"Error: Missing column in MCQ file: {e}")
                return False

            # --- LQ Section Title ---
            md_file.write('---\n')
            md_file.write('\n')
            md_file.write('<div class="section-title">**乙部 問答題**</div>\n')
            if preferences['show_answer_spaces']:
                md_file.write('**請在適當的答案框內作答。**\n\n')
            else:
                md_file.write('**請回答以下問題。**\n\n')
            
            # --- LQ Questions Logic (rest remains the same) ---
            try:
                with open(lq_csv_path, 'r', encoding='utf-8') as csv_file:
                    reader = csv.DictReader(csv_file)
                    lq_counter = 1
                    for row in reader:
                        if not row.get('QuestionText', '').strip():
                            continue
                        
                        question_id_with_years = row.get('QuestionIDwithQuestionyears', '')
                        # ... (rest of LQ logic) ...
                        book_chapter = row.get('book_chapter', '')
                        topics = row.get('topics', '')
                        year = question_id_with_years.split('-')[0] if question_id_with_years else ''
                        question_text = row['QuestionText']
                        total_marks = row['Marks']
                        
                        md_file.write('---\n') 
                        
                        if preferences['show_source_info']:
                            source_info = f"({year}_{question_id_with_years}_{book_chapter}_{topics})"
                            md_file.write(f'<p style="font-size: 0.7em; color: gray;">{source_info}</p>\n')
                            
                        md_file.write(f'## **{lq_counter}. {question_text}** <span class="points">({total_marks} 分)</span>\n\n')
                        
                        sub_questions = []
                        for i in range(1, 9): 
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
                            md_file.write(f'### **{sub["text"]}** <span class="points">({sub["marks"]}分)</span>\n')
                            
                            if preferences['show_answers']:
                                answer_text = ""
                                if question_id_with_years in lq_answers and sub['index'] in lq_answers[question_id_with_years]:
                                    answer_text = lq_answers[question_id_with_years][sub['index']]
                                elif question_id_with_years in lq_answers and (idx + 1) in lq_answers[question_id_with_years]:
                                    answer_text = lq_answers[question_id_with_years][idx + 1]
                                
                                if answer_text:
                                    md_file.write(f'<div style="color: red; font-weight: bold; margin: 10px 0; padding: 10px; border-left: 3px solid red;">答案: {answer_text}</div>\n')
                                else:
                                    md_file.write('<div style="color: orange; font-style: italic;">答案: [答案未提供]</div>\n')
                                    
                            elif preferences['show_answer_spaces']:
                                marks_value = int(sub["marks"]) if sub["marks"] and sub["marks"].isdigit() else 2
                                if marks_value >= 4:
                                    height = "5em"
                                elif marks_value >= 2:
                                    height = "4em"
                                else:
                                    height = "3em"
                                md_file.write(f'<div style="border: 1px solid #ccc; margin-top: 5px; margin-bottom: 10px; padding: 5px;"><div style="height: {height};"></div></div>\n')
                                
                            md_file.write('\n')
                            
                        lq_counter += 1
                        
            except FileNotFoundError:
                print(f"Note: File {lq_csv_path} not found. Skipping long questions section.")
            except KeyError as e:
                print(f"Error: Missing column in LQ file: {e}")
        
        print("Successfully generated Exercise.md!")
        return True
    except Exception as e:
        print(f"Error creating Exercise.md: {e}")
        return False

# --- CORE FUNCTION 3: Generate DOCX (Updated) ---
def generate_exercise_docx(preferences, mcq_csv_path, lq_csv_path, lq_answers_path):
    """
    Generates the Exercise.docx file using python-docx.
    (Updated to use user input for exam details and correct school name)
    """
    import os
    
    SCHOOL_NAME = "佛教黃鳳翎中學" 
    EXAM_DURATION = preferences['exam_duration']
    EXAM_DATE = preferences['exam_date']
    TOTAL_MARKS = preferences['total_marks']

    lq_answers = load_lq_answers(lq_answers_path)
    docx_path = os.path.join(RESULT_FOLDER, 'Exercise.docx')
    try:
        doc = Document()
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Arial'
        font.size = Pt(12)
        
        # --- A4 SIZE AND MARGINS SETUP ---
        section = doc.sections[0]
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
        # Title page
        title_suffix = ""
        if preferences['show_answers']:
            title_suffix = " (答案版)"
        elif not preferences['show_answer_spaces']:
            title_suffix = " (純題目版)"
            
        # 1. School Name Header
        title = doc.add_heading(SCHOOL_NAME, level=1)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # 2. Main Title and Subtitle
        subtitle = doc.add_heading(f'ICT 練習題集{title_suffix}', level=2)
        subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # 3. Exam Details Paragraph (DOCX version of the Marp details)
        details_para = doc.add_paragraph(f"{EXAM_DATE} | {EXAM_DURATION} | {TOTAL_MARKS}")
        details_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        doc.add_page_break()

        # ... (MCQ Section Logic) ...
        doc.add_heading('甲部 多項選擇題', level=1)
        doc.add_paragraph('請選擇最合適的答案。').bold = True
        try:
            with open(mcq_csv_path, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                question_counter = 1
                for row in reader:
                    if not row.get('QuestionText', '').strip():
                        continue
                    # ... (MCQ details generation) ...
                    question_id_with_years = row.get('QuestionIDwithQuestionyears', '')
                    book_chapter = row.get('book_chapter', '')
                    topics = row.get('topics', '')
                    year = question_id_with_years.split('-')[0] if question_id_with_years else ''
                    correct_answer = row.get('answer', '').upper() if preferences['show_answers'] else ''
                    if preferences['show_source_info']:
                        source_info = f"({year}_{question_id_with_years}_{book_chapter}_{topics})"
                        source_para = doc.add_paragraph(source_info)
                        source_para.runs[0].font.size = Pt(10)
                        source_para.runs[0].italic = True
                    question_text = row['QuestionText']
                    marks = row['Marks']
                    question_para = doc.add_paragraph(f"{question_counter}. {question_text} ({marks} 分)")
                    question_para.runs[0].bold = True
                    options = [('A', row['OptionA']), ('B', row['OptionB']), ('C', row['OptionC']), ('D', row['OptionD'])]
                    for letter, option_text in options:
                        option_para = doc.add_paragraph(f"   {letter}. {option_text}")
                        if preferences['show_answers'] and letter == correct_answer:
                            for run in option_para.runs:
                                run.font.color.rgb = RGBColor(255, 0, 0)
                                run.bold = True
                            check_run = option_para.add_run(" ✓")
                            check_run.font.color.rgb = RGBColor(255, 0, 0)
                            check_run.bold = True
                    doc.add_paragraph()
                    if question_counter % 5 == 0:
                        doc.add_page_break()
                    question_counter += 1
        except FileNotFoundError:
            return False
        except KeyError:
            return False

        doc.add_page_break()
        # ... (LQ Section Logic) ...
        doc.add_heading('乙部 問答題', level=1)
        if preferences['show_answer_spaces']:
            doc.add_paragraph('請在適當的答案框內作答。').bold = True
        else:
            doc.add_paragraph('請回答以下問題。').bold = True
        try:
            with open(lq_csv_path, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                lq_counter = 1
                for row in reader:
                    if not row.get('QuestionText', '').strip():
                        continue
                    question_id_with_years = row.get('QuestionIDwithQuestionyears', '')
                    book_chapter = row.get('book_chapter', '')
                    topics = row.get('topics', '')
                    year = question_id_with_years.split('-')[0] if question_id_with_years else ''
                    if preferences['show_source_info']:
                        source_info = f"({year}_{question_id_with_years}_{book_chapter}_{topics})"
                        source_para = doc.add_paragraph(source_info)
                        source_para.runs[0].font.size = Pt(10)
                        source_para.runs[0].italic = True
                    question_text = row['QuestionText']
                    total_marks = row['Marks']
                    question_para = doc.add_paragraph(f"{lq_counter}. {question_text} ({total_marks} 分)")
                    question_para.runs[0].bold = True
                    sub_questions = []
                    for i in range(1,9):
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
                        sub_para = doc.add_paragraph(f"{sub['text']} ({sub['marks']}分)")
                        if preferences['show_answers']:
                            answer_text = ""
                            if question_id_with_years in lq_answers and sub['index'] in lq_answers[question_id_with_years]:
                                answer_text = lq_answers[question_id_with_years][sub['index']]
                            elif question_id_with_years in lq_answers and (idx+1) in lq_answers[question_id_with_years]:
                                answer_text = lq_answers[question_id_with_years][idx+1]
                            if answer_text:
                                answer_para = doc.add_paragraph(f"答案: {answer_text}")
                                answer_para.runs[0].font.color.rgb = RGBColor(255, 0, 0)
                                answer_para.runs[0].bold = True
                            else:
                                answer_para = doc.add_paragraph("答案: [答案未提供]")
                                answer_para.runs[0].font.color.rgb = RGBColor(255, 165, 0)
                                answer_para.runs[0].italic = True
                        elif preferences['show_answer_spaces']:
                            marks_value = int(sub["marks"]) if sub["marks"] and sub["marks"].isdigit() else 2
                            lines = max(3, marks_value)
                            for line_num in range(lines):
                                answer_line = doc.add_paragraph()
                                answer_line.add_run("_" * 60)
                                answer_line.paragraph_format.space_before = Pt(6)
                                answer_line.paragraph_format.space_after = Pt(6)
                            doc.add_paragraph()
                    doc.add_page_break()
                    lq_counter += 1
        except FileNotFoundError:
            pass # Handled in load_lq_answers
        doc.save(docx_path)
        print("✓ DOCX file generated successfully!")
        return True
    except Exception as e:
        print(f"✗ Error creating Exercise.docx: {e}")
        return False


# --- Main Execution Block (Updated) ---
def main():
    print("=== ICT Exercise Generator ===")
    
    # 1. Get ALL preferences and exam details
    preferences = get_user_preferences()
    
    print("\nChoosing MCQ and LQ CSV files:")
    mcq_csv_path = choose_csv_file("Select MCQ csv file")
    lq_csv_path = choose_csv_file("Select LQ csv file")
    lq_answers_path = os.path.join(CSV_FOLDER, 'LQ_Answers.csv')

    print("\nGenerating exercise files...")
    
    # 2. Pass the full preferences dictionary to the generator functions
    result_md = generate_exercise_markdown(preferences, mcq_csv_path, lq_csv_path, lq_answers_path)
    print("✓ Markdown file generated successfully" if result_md else "✗ Failed to generate Markdown file")

    # DOCX
    try:
        import docx
        result_docx = generate_exercise_docx(preferences, mcq_csv_path, lq_csv_path, lq_answers_path)
        print("✓ DOCX file generated successfully" if result_docx else "✗ Failed to generate DOCX file")
    except ImportError:
        print("⚠ DOCX file not created: python-docx not installed. Run pip3 install python-docx first.")

    print("\n=== Generation Complete ===")
    markdown_path = os.path.join(RESULT_FOLDER, "Exercise.md")
    docx_path = os.path.join(RESULT_FOLDER, "Exercise.docx")
    files_created = []
    if os.path.exists(markdown_path):
        files_created.append("- Exercise.md (Markdown format)")
    if os.path.exists(docx_path):
        files_created.append("- Exercise.docx (Word format)")
    print('\n'.join(files_created) if files_created else "No files were created successfully.")

if __name__ == "__main__":
    main()