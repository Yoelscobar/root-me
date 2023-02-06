import pytesseract
from PIL import Image
from pip._vendor import requests
import io, base64
from PIL import Image
import time





pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def wreq():
    response = requests.get("http://challenge01.root-me.org/programmation/ch8/").text
    base64_string = response.split()[10]
    base64_string = base64_string[27:]
    #print(base64_string)
    stringTopng(base64_string)
    secret = decode(r"C:\Users\Rudolf\Desktop\rootme\pytesseract\my-image.jpeg")
    print(secret)
    #time.sleep(1)
    postreq("camtu", secret)

def postreq(key, value):
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate', 'Cookie': 
                'PHPSESSID=0741adb4a605b3cd73e294b57dafc72e', 
                'Host': 'challenge01.root-me.org',
                'DNT': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'Referer': 'http://challenge01.root-me.org/programmation/ch8/' }
    payload = {'camtu': value}
    print(payload)

    #req = requests.Request('POST','http://challenge01.root-me.org/programmation/ch8/',headers=headers, json={key : value})
    req = requests.get('http://challenge01.root-me.org/programmation/ch8/',headers=headers, params=payload)
    print(req.text)
    #prepared = req.prepare()
    #pretty_print_POST(req)



    #r = requests.request('POST', 'http://challenge01.root-me.org/programmation/ch8/', headers=headers, json={key: value})



def decode(imagepath):
    return(pytesseract.image_to_string(Image.open(imagepath)))

def stringTopng(string):
# Assuming base64_str is the string value without 'data:image/jpeg;base64,'
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(string, "utf-8"))))
    img.save('my-image.jpeg')
    return img

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))



def main():
    wreq()

main()