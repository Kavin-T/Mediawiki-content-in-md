import xml.etree.ElementTree as ET
import subprocess

def write_file(title,content):
    filename="content//"+title+".md"
    filename=filename.replace("?","")
    if content!=None:
        with open(filename,'w',encoding='utf-8') as file:
            file.write(content)
    else:
        print("Error converting "+filename)

def convert_to_markdown(mediawiki_text):
    pandoc_command = ["pandoc", "-f", "mediawiki", "-t", "markdown"]
    process = subprocess.Popen(pandoc_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    converted_text, error = process.communicate(input=mediawiki_text.encode("utf-8"))
    
    if process.returncode != 0:
        print(f"Error converting to Markdown: {error.decode('utf-8')}")
        return None
    return converted_text.decode("utf-8")

def extract_page_info(xml_file):
    namespace = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    pages = root.findall('.//mw:page', namespace)
    count=0
    for page in pages:
        title = page.find('./mw:title', namespace).text
        text = page.find('./mw:revision/mw:text', namespace).text
        ct=convert_to_markdown(text)
        write_file(title,ct)
        #count+=1
    #print("Count = ",count)

xml_file_path = "C://Users//kavin//Desktop//VPT//Tamil+Wiki-20231029024626.xml"
extract_page_info(xml_file_path)
print("Process Completed!!!")

