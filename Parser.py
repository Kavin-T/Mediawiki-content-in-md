import re
import xml.etree.ElementTree as ET

def write_file(title,content_string):
    filename=title+".md"
    with open(filename, 'w' ,encoding='utf-8') as file:
        file.write(content_string)
        
def extract_page_info(xml_file):
    # Define the namespace
    namespace = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}

    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find the 'page' elements using the namespace
    pages = root.findall('.//mw:page', namespace)

    # Initialize an empty string to store the formatted output
    formatted_output = ""

    # Iterate through each 'page' element
    for page in pages:
        title = page.find('./mw:title', namespace).text
        text = page.find('./mw:revision/mw:text', namespace).text

        markdown_output=convert_to_markdown(text)
        write_file(title,markdown_output)

def convert_to_markdown(content_string):
    def handle_headings(match):
        return f'## {match.group(1)}'

    def handle_bullet_points(match):
        return f'* {match.group(1)}'

    def handle_reference_links(match):
        link_text = match.group(1).strip()
        link_target = match.group(2).strip() if match.group(2) else link_text
        link_url = f'http://tamil.wiki/wiki/{link_target}'
        return f'[{link_text}]({link_url})'

    def handle_image_cards(match):
        image_path = match.group(1).strip()
        image_caption = match.group(2).strip() if match.group(2) else ""
        image_url = f'https://tamil.wiki/images/thumb/{image_path}'
        return f'![{image_caption}]({image_url})'

    # Handle headings (e.g., == முகப்பு == to ## முகப்பு)
    content_string = re.sub(r'==\s*(.*?)\s*==', handle_headings, content_string)

    # Handle bullet points starting with '*'
    content_string = re.sub(r'(?m)^\*\s*(.*)$', handle_bullet_points, content_string)

    # Handle reference links (e.g., [[வண்ணதாசன்]] to [வண்ணதாசன்](http://tamil.wiki/wiki/இமையம்))
    content_string = re.sub(r'\[\[(.+?)(?:\|(.+?))?\]\]', handle_reference_links, content_string)

    # Convert [https://vallinam.com.my/version2/?p=732 மா. சண்முகசிவா நேர்காணல், வல்லினம்] to [மா. சண்முகசிவா நேர்காணல், வல்லினம்](https://vallinam.com.my/version2/?p=732)
    content_string = re.sub(r'\[(.*?) (.*?)\]', r'[\2](\1)', content_string)

    return content_string

extract_page_info("C:\\Users\\kavin\\OneDrive\\Desktop\\VPT\\Tamil_Wiki.xml")

# content_string = """
# == முகப்பு ==
# Content for முகப்பு.

# * முகப்பு
# *முகப்பு

# [[வண்ணதாசன்]]
# [[எஸ். ராமகிருஷ்ணன்|எஸ்.ராமகிருஷ்ணன்]]
# [https://vallinam.com.my/version2/?p=732 மா. சண்முகசிவா நேர்காணல், வல்லினம்]
# [[File:மதார்.jpg|thumb]]
# [[File:Mathaar.png|thumb|நன்றி சுருதி டிவி]]
# """
# out=convert_to_markdown(content_string)

# def func(s):
#     a=re.sub(r'\[\[File:(.*).png|.jpg\|thumb\]\]', r'\[\]\(https://tamil.wiki/images/thumb/\1.png\)', out)
#     return a


# print(func(out))


