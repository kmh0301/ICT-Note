import re

def extract_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by double newlines or lines starting with a number followed by a dot
    # Use regex to find lines starting with "Number."
    questions = []
    current_q = []
    
    lines = content.split('\n')
    for line in lines:
        if re.match(r'^\d+\.', line.strip()):
            if current_q:
                questions.append("\n".join(current_q).strip())
            current_q = [line]
        elif current_q and line.strip():
            current_q.append(line)
        elif not line.strip() and current_q:
            # Maybe end of question? But some questions have options in new lines.
            pass
            
    if current_q:
        questions.append("\n".join(current_q).strip())
        
    return questions

def normalize(text):
    # Remove leading number and dot
    text = re.sub(r'^\d+\.\s*', '', text)
    # Remove options and common filler words
    text = re.sub(r'\s+[A-D]\..*', '', text, flags=re.DOTALL)
    text = re.sub(r'\s+\(\d\).*', '', text, flags=re.DOTALL)
    # Keep only Chinese characters and alphanumeric
    text = "".join(re.findall(r'[\u4e00-\u9fffA-Za-z0-9]', text))
    return text

file1 = "/Users/sallypang/Documents/GitHub/ICT-Note/markdown/S4_ict/已出題目/2526下學期UTMC.md"
file2 = "/Users/sallypang/Documents/GitHub/ICT-Note/markdown/S4_ict/已出題目/25-26上學期UT+ExamMC.md"

qs1 = extract_questions(file1)
qs2 = extract_questions(file2)

print(f"File 1 has {len(qs1)} questions.")
print(f"File 2 has {len(qs2)} questions.")

print("\n--- Detailed Comparison ---")
duplicates = []
for i, q1 in enumerate(qs1):
    n1 = normalize(q1)
    for j, q2 in enumerate(qs2):
        n2 = normalize(q2)
        
        # Calculate a simple similarity score or check for overlap
        if n1 in n2 or n2 in n1:
            duplicates.append((i+1, q1, j+1, q2, "Substantial Overlap"))
        elif len(n1) > 15 and len(n2) > 15:
            # Check for high overlap in characters
            common = set(n1) & set(n2)
            score = len(common) / max(len(set(n1)), len(set(n2)))
            if score > 0.8:
                duplicates.append((i+1, q1, j+1, q2, f"High Similarity ({score:.2f})"))

if duplicates:
    print("\nPotential duplicates or highly similar questions found:")
    for d in duplicates:
        print(f"\n[F1 Q{d[0]}] vs [F2 Q{d[2]}] - {d[4]}")
        print(f"F1: {d[1].splitlines()[0]}")
        print(f"F2: {d[3].splitlines()[0]}")
else:
    print("\nNo close duplicates found.")
