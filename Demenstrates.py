# Task1
from json.tool import main
import re
def demonsteate_special_sequences():
    sample_text = """
The quick brown fox jumps over the lazy dog. 
Foxes are wild animals. The dog quicly ran away 
my eamil is example@example.com and my number is (123) 456-7890
Visit us at www.example.com or contact us at info@example.com.
"""

# 1. \d - matches any digit (0-9)
    digit_pattern = r'\d+'
    print(f"Digits(\\d) pattern '{digit_pattern}':", re.findall(digit_pattern, sample_text))

# 2. \D - Matches any non-digit character
    non_digit_pattern = r'\D+'
    print(f"Non-digits (\\D) pattern '{non_digit_pattern}':", re.findall(non_digit_pattern,sample_text))

# 3. \w - Matches any word character (alphanumeric + underscore)
    word_char_pattren = r'\w+'
    print(f"word character (\\w) pattern  '(word_char_pattern)':", re.findall(word_char_pattren, sample_text))

# 4. \W - Matches any non-word character
    non_word_char_pattern = r'W+'
    print(f"Non word character (\\W) pattern '(non_word_char_ pattern)':", re.findall(non_word_char_pattern, sample_text))

# 5. \s - Matches any whitespace character (spaces, tabs, newlines)
    whitespace_pattern = r'\s+'
    print(f"whitespace character (\\s) pattern '(whitespace_pattern)':", re.findall(whitespace_pattern, sample_text))

# 6. \S - matches any non-whitespace character
    non_whitespace_pattern = r'\S+'
    print(f" non-whitespace character (\\s) pattern '(non_whitespace_pattern)':", re.findall(non_whitespace_pattern, sample_text))

# 7. \b - matches a word boundary
    word_boundary_pattern = r'\bfox\b'
    print(f"word boundary (\\b) pattren '(word_boundary_pattern)':", re.findall(word_boundary_pattern, sample_text))

# 8. \B - Matches a non-word boundary
    non_word_boundary_pattern = r'\bfox\b'
    print(f"non-word boundary (\\b) pattren '(non_word_boundary_pattern)':", re.findall(non_word_boundary_pattern, sample_text))
    
# Task3
def main():
    demonsteate_special_sequences()
if __name__ =="__main__":
    main()
