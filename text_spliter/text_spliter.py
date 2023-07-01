import os
import html2text
from bs4 import BeautifulSoup


# Function to convert Html to text

def html_txt(f2name):
    soup = BeautifulSoup(open(file_path,encoding='utf-8'), "html.parser")
    txt = soup.get_text()

    with open(s_name, "w", encoding='utf-8') as f:
        f.write(txt)


# Function to open text file and to read it

def open_transcript1(f1name):
    with open(s_name, "r",encoding='utf-8') as f1:
        transcript1 = f1.read()
    return (transcript1)


# Function's to extract words from text

def transcript1_seprate(transcript1):
    transcript1 = transcript1.split("\n")
    return(transcript1)

def clean_transcript1(transcript1):
    if " \n" in transcript1:
        transcript1 = transcript1.replace(",", " ")
        transcript1 = transcript1.split("\n") 
    return(transcript1)


for k in range(1,2):
    # This part is regarding file names and file imports
    file_path = "html_files\Gray_s Anatomy The Anatomical Basis of Clinical Practice-41st\P_00" + str(k) + ".html"
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    s1_name = "./FINAL Files/Gray_s Anatomy The Anatomical Basis of Clinical Practice-41st/" + str(file_name) + ".txt"
    s_name = "./Text Files/" + str(file_name) + ".txt"
    
    try:
        text_file = html_txt(file_path)
        transcript1 = open_transcript1(s_name)
        transcript1 = clean_transcript1(transcript1)
        transcript1 = transcript1_seprate(transcript1)
        length = len(transcript1)
        list1 = []
    except:
        text_file = html_txt(file_path)
        transcript1 = open_transcript1(s_name)
        # transcript1 = clean_transcript1(transcript1)
        transcript1 = transcript1_seprate(transcript1)
        length = len(transcript1)
        list1 = []
    
    while("" in transcript1):
        transcript1.remove("")
    
    
    # This loop extracts Index words from text file
    for i in transcript1:
        trans = i.split(",")
        
        if trans[0][0].isupper():
            list1.append(trans[0])
    
    # To write the Index words in text
    with open(s1_name, 'w', encoding='utf-8') as out_f:
        for j in list1:
            out_f.write(j + "\n")