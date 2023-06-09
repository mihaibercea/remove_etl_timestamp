
import re

import typer

import chardet
from tqdm import tqdm

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        
        return encoding

app = typer.Typer()

@app.command()
def file(input_file: str):
    output_file = input_file.rsplit('.', 1)[0] + '_no_timestamp.' + input_file.rsplit('.', 1)[1]

    enc = detect_encoding(input_file)

    with open(input_file, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='latin-1') as file:
        total_lines = len(lines)
        with tqdm(total=total_lines, desc="Parsing", unit="line") as pbar:
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
                pbar.update(1)

    print(f"Timestamps removed. Output file: {output_file}")

if __name__ == "__main__":
    app()



