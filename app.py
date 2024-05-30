####################### Build-in libraries/ Module #######################
import re
import os
import glob


####################### External libraries/ Module #######################
import fitz
import pandas as pd




######################################## Logical Function ########################################

def get_pdf_files(folder_path):
    pdf_files = []  
    # Use glob to find all PDF files in the specified folder
    pdf_pattern = os.path.join(folder_path, '*.pdf')
    pdf_files.extend(glob.glob(pdf_pattern))
    return pdf_files


def extract_text_from_pdf(pdf_path):
    ''' Function will return extracted text from pdf '''
    doc = fitz.open(pdf_path)                   
    text = ""                                   
    for page_num in range(doc.page_count):      
        page = doc[page_num]                   
        text += page.get_text()
    doc.close()                                 
    return text


def extract_information(text):
    ''' Extract information from text '''
    pattern = re.compile(r'(\d+)\s+(.+?)\s+([\d.]+)')
    matches = re.findall(pattern, text)
    data = {'Sr No.': [], 'College Names': [], 'Cutoff': []}
    for match in matches:
        data['Sr No.'].append(match[0])
        data['College Names'].append(match[1])
        data['Cutoff'].append(match[2])
    return data


def save_file(extracted_data):
    ''' Function will save file in form .csv'''
    data_frame = pd.DataFrame(extracted_data)
    # file_name = input('Enter file name without extension: ')
    for file_name in range(500):
        data_frame.to_csv(f'{file_name}.csv', index=False)
    



######################################## Utility Function ########################################
def main():
    folder_path = input('Enter folder path: ')
    pdf_files = get_pdf_files(folder_path)
    for pdf_path in pdf_files:
        extracted_text = extract_text_from_pdf(pdf_path)
        data = extract_information(extracted_text)
        save_file(data)
    
    

if __name__ == '__main__':
    main()
