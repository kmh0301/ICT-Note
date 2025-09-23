import csv
import subprocess
import sys
import os

def install_required_packages():
    """Install required packages if not already installed."""
    packages_to_install = []
    
    # Check for python-docx
    try:
        import docx
        print("✓ python-docx is already installed")
    except ImportError:
        packages_to_install.append('python-docx')
    
    # Check for reportlab
    try:
        import reportlab
        print("✓ reportlab is already installed")
    except ImportError:
        packages_to_install.append('reportlab')
    
    # Install missing packages
    for package in packages_to_install:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package], 
                                capture_output=True, text=True)
            print(f"✓ Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install {package}")
            print("Please try installing manually:")
            print(f"  pip3 install {package}")
            print(f"  or: python3 -m pip install {package}")
            return False
    
    return True

def generate_exercise_markdown():
    """Generates the Exercise.md file from MCQ.csv and LQ.csv with source information."""
    
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

    try:
        with open('Exercise.md', 'w', encoding='utf-8') as md_file:
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
            md_file.write("# **ICT 練習題集**\n\n")
            md_file.write("---\n\n")

            # Write the Multiple-Choice (MCQ) section
            md_file.write('<div class="section-title"><strong>甲部 多項選擇題</strong></div>\n')
            md_file.write('<strong>請選擇最合適的答案。</strong>\n\n')

            # Process MCQ questions
            try:
                with open('MCQ.csv', 'r', encoding='utf-8') as csv_file:
                    reader = csv.DictReader(csv_file)
                    question_counter = 1
                    
                    for row in reader:
                        # Skip empty rows
                        if not row.get('QuestionText', '').strip():
                            continue
                        
                        # Extract source information
                        question_id_with_years = row.get('QuestionIDwithQuestionyears', '')
                        book_chapter = row.get('book_chapter', '')
                        topics = row.get('topics', '')
                        
                        # Parse year from QuestionIDwithQuestionyears (e.g., "2016-1-6" -> "2016")
                        year = question_id_with_years.split('-')[0] if question_id_with_years else ''
                        
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

                        # Write source information and question
                        source_info = f"({year}_{question_id_with_years}_{book_chapter}_{topics})"
                        md_file.write(f'<div class="question-source">{source_info}</div><br>\n')
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
                return False
            except KeyError as e:
                print(f"Error: Missing column in MCQ.csv: {e}")
                return False

            # Write the Long-Answer (LQ) section
            md_file.write('---\n\n')
            md_file.write('<div class="section-title"><strong>乙部 問答題</strong></div>\n')
            md_file.write('<strong>請在適當的答案框內作答。</strong>\n\n')

            # Process LQ questions
            try:
                with open('LQ.csv', 'r', encoding='utf-8') as csv_file:
                    reader = csv.DictReader(csv_file)
                    lq_counter = 1
                    
                    for row in reader:
                        # Skip empty rows
                        if not row.get('QuestionText', '').strip():
                            continue
                        
                        # Extract source information
                        question_id_with_years = row.get('QuestionIDwithQuestionyears', '')
                        book_chapter = row.get('book_chapter', '')
                        topics = row.get('topics', '')
                        
                        # Parse year and question ID
                        year = question_id_with_years.split('-')[0] if question_id_with_years else ''
                        question_id = question_id_with_years.split('-')[-1] if question_id_with_years else str(lq_counter)
                        
                        question_text = row['QuestionText']
                        total_marks = row['Marks']
                        
                        md_file.write('---\n\n')
                        
                        # Write source information and question
                        source_info = f"({year}_{question_id_with_years}_{book_chapter}_{topics})"
                        md_file.write(f'<div class="question-source">{source_info}</div><br>\n')
                        md_file.write(f'<div class="question-item">{lq_counter}. {question_text} <span class="points">({total_marks} 分)</span></div>\n\n')

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

                        # Display all sub-questions found
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
                        
                        lq_counter += 1

            except FileNotFoundError:
                print("Note: 'LQ.csv' not found. Skipping long questions section.")
            except KeyError as e:
                print(f"Error: Missing column in LQ.csv: {e}")

        print("Successfully generated Exercise.md!")
        return True
        
    except Exception as e:
        print(f"Error creating Exercise.md: {e}")
        return False

def generate_exercise_docx():
    """Generates the Exercise.docx file from MCQ.csv and LQ.csv."""
    
    try:
        # Import docx modules here after installation
        from docx import Document
        from docx.shared import Inches, Pt
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        
        # Create a new Document
        doc = Document()
        
        # Set default font
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Arial'
        font.size = Pt(12)
        
        # Title page
        title = doc.add_heading('佛教黃鳳翎中學', level=1)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        subtitle = doc.add_heading('ICT 練習題集', level=2)
        subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        doc.add_page_break()
        
        # MCQ Section
        doc.add_heading('甲部 多項選擇題', level=1)
        doc.add_paragraph('請選擇最合適的答案。').bold = True
        
        # Process MCQ questions
        try:
            with open('MCQ.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                question_counter = 1
                
                for row in reader:
                    if not row.get('QuestionText', '').strip():
                        continue
                    
                    # Extract source information
                    question_id_with_years = row.get('QuestionIDwithQuestionyears', '')
                    book_chapter = row.get('book_chapter', '')
                    topics = row.get('topics', '')
                    year = question_id_with_years.split('-')[0] if question_id_with_years else ''
                    
                    # Add source info
                    source_info = f"({year}_{question_id_with_years}_{book_chapter}_{topics})"
                    source_para = doc.add_paragraph(source_info)
                    source_para.runs[0].font.size = Pt(10)
                    source_para.runs[0].italic = True
                    
                    # Add question
                    question_text = row['QuestionText']
                    marks = row['Marks']
                    question_para = doc.add_paragraph(f"{question_counter}. {question_text} ({marks} 分)")
                    question_para.runs[0].bold = True
                    
                    # Add options
                    for option_letter, option_key in [('A', 'OptionA'), ('B', 'OptionB'), ('C', 'OptionC'), ('D', 'OptionD')]:
                        option_text = row[option_key]
                        doc.add_paragraph(f"   {option_letter}. {option_text}")
                    
                    doc.add_paragraph()  # Add spacing
                    
                    # Page break every 5 questions
                    if question_counter % 5 == 0:
                        doc.add_page_break()
                    
                    question_counter += 1
                    
        except FileNotFoundError:
            print("Error: 'MCQ.csv' not found.")
            return False
        except KeyError as e:
            print(f"Error: Missing column in MCQ.csv: {e}")
            return False
        
        # LQ Section
        doc.add_page_break()
        doc.add_heading('乙部 問答題', level=1)
        doc.add_paragraph('請在適當的答案框內作答。').bold = True
        
        # Process LQ questions
        try:
            with open('LQ.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                lq_counter = 1
                
                for row in reader:
                    if not row.get('QuestionText', '').strip():
                        continue
                    
                    # Extract source information
                    question_id_with_years = row.get('QuestionIDwithQuestionyears', '')
                    book_chapter = row.get('book_chapter', '')
                    topics = row.get('topics', '')
                    year = question_id_with_years.split('-')[0] if question_id_with_years else ''
                    
                    # Add source info
                    source_info = f"({year}_{question_id_with_years}_{book_chapter}_{topics})"
                    source_para = doc.add_paragraph(source_info)
                    source_para.runs[0].font.size = Pt(10)
                    source_para.runs[0].italic = True
                    
                    # Add main question
                    question_text = row['QuestionText']
                    total_marks = row['Marks']
                    question_para = doc.add_paragraph(f"{lq_counter}. {question_text} ({total_marks} 分)")
                    question_para.runs[0].bold = True
                    
                    # Handle sub-questions
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
                    
                    # Display sub-questions
                    for idx, sub in enumerate(sub_questions):
                        letter = chr(ord('a') + idx)
                        sub_para = doc.add_paragraph(f"{sub['text']} ({sub['marks']}分)")
                        
                        # Add answer space based on marks
                        marks_value = int(sub["marks"]) if sub["marks"] and sub["marks"].isdigit() else 2
                        lines = max(3, marks_value)  # At least 3 lines, more for higher marks
                        
                        for _ in range(lines):
                            doc.add_paragraph("_" * 80)  # Answer lines
                        
                        doc.add_paragraph()  # Spacing after answer area
                    
                    doc.add_page_break()  # New page for each LQ
                    lq_counter += 1
                    
        except FileNotFoundError:
            print("Note: 'LQ.csv' not found. Skipping long questions section.")
        except KeyError as e:
            print(f"Error: Missing column in LQ.csv: {e}")
        
        # Save the document
        doc.save('Exercise.docx')
        print("Successfully generated Exercise.docx!")
        return True
        
    except Exception as e:
        print(f"Error creating Exercise.docx: {e}")
        return False

def convert_docx_to_pdf():
    """Convert DOCX to PDF using various methods."""
    try:
        # Method 1: Try using docx2pdf (Windows/Mac with Word installed)
        try:
            from docx2pdf import convert
            convert("Exercise.docx", "Exercise.pdf")
            print("Successfully generated Exercise.pdf using docx2pdf!")
            return True
        except ImportError:
            print("docx2pdf not available, trying alternative method...")
        
        # Method 2: Try using python-docx2txt and reportlab
        try:
            from reportlab.lib.pagesizes import letter, A4
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from docx import Document
            
            # Read the DOCX file
            doc = Document('Exercise.docx')
            
            # Create PDF
            pdf_doc = SimpleDocTemplate("Exercise.pdf", pagesize=A4)
            styles = getSampleStyleSheet()
            story = []
            
            # Custom styles
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=18,
                alignment=1,  # Center
                spaceAfter=12
            )
            
            question_style = ParagraphStyle(
                'Question',
                parent=styles['Normal'],
                fontSize=12,
                spaceAfter=6,
                fontName='Helvetica-Bold'
            )
            
            # Extract text from DOCX and convert to PDF
            for paragraph in doc.paragraphs:
                if paragraph.text.strip():
                    if paragraph.style.name.startswith('Heading'):
                        story.append(Paragraph(paragraph.text, title_style))
                    elif any(run.bold for run in paragraph.runs):
                        story.append(Paragraph(paragraph.text, question_style))
                    else:
                        story.append(Paragraph(paragraph.text, styles['Normal']))
                    story.append(Spacer(1, 6))
            
            pdf_doc.build(story)
            print("Successfully generated Exercise.pdf using reportlab!")
            return True
            
        except ImportError:
            print("reportlab not available for PDF conversion.")
        
        # Method 3: Instructions for manual conversion
        print("\nPDF conversion libraries not available.")
        print("To convert to PDF, you can:")
        print("1. Install docx2pdf: pip install docx2pdf")
        print("2. Open Exercise.docx in Word and save as PDF")
        print("3. Use online converters like SmallPDF or ILovePDF")
        
        return False
        
    except Exception as e:
        print(f"Error converting to PDF: {e}")
        return False

def main():
    """Main function to generate all formats."""
    print("=== ICT Exercise Generator ===")
    print("Checking required packages...")
    
    # Try to install required packages
    packages_installed = install_required_packages()
    
    print("\nGenerating exercise files...")
    
    # Generate Markdown (this always works)
    if generate_exercise_markdown():
        print("✓ Markdown file generated successfully")
    else:
        print("✗ Failed to generate Markdown file")
        return
    
    # Generate DOCX (only if packages are available)
    if packages_installed:
        try:
            if generate_exercise_docx():
                print("✓ DOCX file generated successfully")
            else:
                print("✗ Failed to generate DOCX file")
        except ImportError as e:
            print(f"✗ Cannot generate DOCX: {e}")
            print("DOCX generation skipped - packages not available")
    else:
        print("⚠ Skipping DOCX generation - packages not installed")
        print("To enable DOCX generation, install manually:")
        print("  pip3 install python-docx")
    
    # Convert to PDF (only if DOCX was created)
    if os.path.exists("Exercise.docx"):
        if convert_docx_to_pdf():
            print("✓ PDF file generated successfully")
        else:
            print("⚠ PDF conversion not available")
    else:
        print("⚠ Skipping PDF generation - no DOCX file available")
    
    print("\n=== Generation Complete ===")
    print("Files created:")
    
    # Check which files were actually created
    files_created = []
    if os.path.exists("Exercise.md"):
        files_created.append("- Exercise.md (Markdown format)")
    if os.path.exists("Exercise.docx"):
        files_created.append("- Exercise.docx (Word format)")
    if os.path.exists("Exercise.pdf"):
        files_created.append("- Exercise.pdf (PDF format)")
    
    if files_created:
        for file_info in files_created:
            print(file_info)
    else:
        print("No files were created successfully.")
        
    # Provide manual installation instructions if needed
    if not packages_installed:
        print("\nTo enable full functionality, please install:")
        print("  pip3 install python-docx reportlab")
        print("Then run the script again.")

# Run the script
if __name__ == "__main__":
    main()