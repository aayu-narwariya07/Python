# Task1:
# improt the re module and dfine the demonstration function

from ast import main
import re
def demonstrate_metacharacters():
    sample_text = """
The qunik brown fox jumps over the lazy dog. 
Foxes are wild animals. The dog quicly ran away 
my eamil is example@example.com and my number is (123)
"""
# Task2
# Dot(.)
    dot_pattern = r'The .quick'
    print(f"Dot(.)pattern '{{dot_pattern}}:'", re.findall(dot_pattern, sample_text))

    # Caret (^) and dollar sign ($)
    caret_pattern = r'^The'
    dollar_pattern = r'dog.$'
    print(f"Start of string (^) pattern'{{caret_paattern}}':", re.match(caret_pattern, sample_text))
    print(f"End of string ($) pattern '{{dollar_pattern}}':", re.search(dollar_pattern, sample_text))

    # Aterisk (*) and plus(+)
    asterisk_pattern = r'fox*'
    plus_pattern = r'fox+'
    print(f"Asterisk(*) pattern '{{asterisk_pattern}}':", re.findall(asterisk_pattern, sample_text))
    print(f"plus(+) pattern '{{plus_pattern}}':", re.findall(plus_pattern, sample_text))

    # Question mark(?)
    quetion_pattern = r'fox?'
    print(f"question mark (?) pattern'{{question_pattern}}':", re.findall(quetion_pattern, sample_text))

    #5.Braces({})
    braces_pattern = r'fo{2}'
    print(f"Brace({{}}) pattern '{{brace_pattern}}':", re.findall(braces_pattern, sample_text))

    # 6 square brackets([])
    square_brackets_pattern = r'[Ff]ox'
    print(f"square brackets([]) pattern '{{square_brackets_pattern}}':", re.findall(square_brackets_pattern, sample_text))

    # 7 pipe (|). Alteranation
    pipe_pattern = r'fox|dog'
    print(f"pipe(|) pattern '{{ pipe_pattern}}':", re.findall(pipe_pattern, sample_text))

    # Backslash(\) Escaping special characters
    backslash_pattern = r'\.'
    print(f"Backslash (\\)'{{backslash_pattern}}':", re.findall(backslash_pattern, sample_text))

    # 9. Escaped characters and special squences
    email_patter = r'\b\w+@\w+\.\w+\b'
    phone_pattern = r'\(d{3}\) \d{3}-\d{4}'
    print(f"Email pattern '{{email_pattern}}':", re.findall(email_patter, sample_text))
    print(f"phone pattern '{{phone_Pattern}}':", re.findall(backslash_pattern,sample_text))


def main():
    demonstrate_metacharacters()
if __name__ =="__main__":
    main()
