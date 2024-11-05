book = {}

book['tom'] = {
    'name' : 'tom',
    'address': '1 red street, NY ',
    'phone': '92378452857'
}



book['bob'] = {
    'name' : 'bob',
    'address': '1 green street, NY ',
    'phone': '48583454'
}

import json
s= json.dumps(book)

with open ("C:\Vedang\Software\PythonCodes\Ai path//book.txt" , "w") as f:
    f.write(s)
