#Marking up data to send across the network 

#eXtensible Markup language
#primary purpose is to help information system share structured data 
# Key Terminology
# Tags: Help indicate the structure of the data.

# Start Tag: e.g., <person>

# End Tag: e.g., </person>

# Element / Node: A simple element has a header tag, a footer tag, and content between them (e.g., <name>Chuck</name>).

# Attributes: Key-value pairs placed inside the start tag that provide metadata about the element (e.g., <person hide="yes">).

# Self-Closing Tag: A shorthand tag for an element with no text content inside (e.g., <email hide="yes" />).

# Text / Content: The actual data value stored inside an element.  

#XML Schema - Describing a "contract" as to what is acceptable XML

import xml.etree.ElementTree as ET

data = '''
<person>
    <name>MUKUL</name>
    <phone type="intl">
        +91 8651088598
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone:', tree.find('phone').text.strip())
print('Attr:', tree.find('email').get('hide'))