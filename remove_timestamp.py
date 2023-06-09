import os
import re
import chardet

def detect_encoding(input_file):
    with open(input_file, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        
        return encoding

def remove_timestamp(input_file):
    output_file = input_file.rsplit('.', 1)[0] + '_no_timestamp.' + input_file.rsplit('.', 1)[1]

    enc = detect_encoding(input_file)

    with open(input_file, 'r', encoding="'latin-1'") as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding="'latin-1'") as file:
        for line in lines:
            #line = re.sub(r'\d{2}/\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+', '', line)
            #line = re.sub(r'\[\d+\] [\dA-Fa-f]+\.[\dA-Fa-f]+\:\: \d{2}/\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+ \[\]', '', line)
            #[0] 0000.0000::03/28/23-12:06:25.4155595 []  
            # line = re.sub(r'\[[\d]+\] [\dA-Fa-f]+\.[\dA-Fa-f]+\:\:[\[\]\w\s]+ \d{2}/\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+', '', line)
            # line = re.sub(r'\[[\d]+\] [\dA-Fa-f]+\.[\dA-Fa-f]+\:\:[\[\]\w\s]+', '', line)
            line = re.sub(r'\d{2}/\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+', '', line)
            line = re.sub(r'\[\d+\] [\dA-Fa-f]+\.[\dA-Fa-f]+\:\:', '', line)    
            line = re.sub(r'\[\d+\][\dA-Fa-f]+\.[\dA-Fa-f]+\:\:', '', line)       
            line = re.sub(r'\[\d+\][\dA-Fa-f]+\.[\dA-Fa-f]+', '', line)
            
            file.write(line)

    print(f"Timestamps removed. Output file: {output_file}")

# Example usage
input_file = 'test.txt'
remove_timestamp(input_file)

