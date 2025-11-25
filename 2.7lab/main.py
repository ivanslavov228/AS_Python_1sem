with open('input.txt', 'r', encoding='utf-8') as f_in:
    text = f_in.read()

punctuation = [char for char in text if char in '.,!?;:—-"\'()[]{}']

with open('output.txt', 'w', encoding='utf-8') as f_out:
    f_out.write(''.join(punctuation))
