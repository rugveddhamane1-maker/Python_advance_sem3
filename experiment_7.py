import re

def find_emails(text):
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    emails = re.findall(pattern, text)

    return emails


# Main program
text = """
Hello students.
You can contact us at abc@gmail.com
or support@mit.edu.
For queries, email admin123@yahoo.com.
"""

emails = find_emails(text)

print("Email addresses found:")

for email in emails:
    print(email)