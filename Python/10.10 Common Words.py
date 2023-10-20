"""Imports a book. Then counts for looks to see how much times the work 'the' appears with and without variations"""
from pathlib import Path


path = Path("The language of flowers.rtf")
contents = path.read_text()

long_text = ''
for content in contents:
    long_text += content
    
print(long_text.count("the"))
print(long_text.lower().count("the"))
print(long_text.lower().count("the "))
