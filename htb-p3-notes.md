# Useful Libraries

## Requests Package
https://requests.readthedocs.io/en/master/
python3 -m pip install requests

---
The two most useful things to know about the requests library are making HTTP requests, and secondly, it has a Session class, which is useful when we need to maintain a certain context during our web activity. For example, if we need to keep track of a range of cookies, we could use a Session object. To get one of these, we import requests and create an object of the Session class like sess = requests.Session(). Alternatively, we can use the requests module (the library itself) to make HTTP requests. However, this will not keep its state automatically.

Consider the following code:

    import requests

    resp = requests.get('http://httpbin.org/ip')
    print(resp.content.decode())

    Prints:

    "origin": "X.X.X.X"

This is a simple example of how to perform a GET request to obtain our public IP address. Since the resp.content variable is a byte-string, a string of bytes that may or may not be printable, we have to call decode() on the object. Decoding the byte-string with the decode() function and no parameters tells Python to interpret the bytes as UTF-8 characters. UTF-8 is the default encoding used when no other encoding is specified. However, other encodings can be used and set as parameter arguments to the decode() function, for example, decode(encoding='UTF-16'). Going back to the resp object, this contains useful information such as the status_code, the numeric HTTP status code of the request we made, and cookies. We will use this library later on, but for now, let us move on with some more food talk.

---
In the requests library, both response.text and response.content.decode() are used to access the body of the HTTP response, but they differ in how they handle encoding:

response.text:

Automatically decodes the response content to a string using the encoding specified in the HTTP headers (e.g., Content-Type).
If the encoding is not specified in the headers, it attempts to guess the encoding using chardet or charset_normalizer.
Example:
response.content.decode():

Gives you more control over the decoding process.
You can specify the encoding explicitly (e.g., resp.content.decode('utf-8')).
If no encoding is specified, it defaults to decoding the raw bytes (response.content) using UTF-8.
Key Difference:
Use response.text for convenience when you trust the encoding provided by the server or guessed by requests.
Use response.content.decode() when you need precise control over the encoding or when the server's encoding is unreliable.
In your code, resp.content.decode() is decoding the raw bytes explicitly, while resp.text would achieve the same result but with automatic encoding detection.
---



## BeautifulSoup
https://www.crummy.com/software/BeautifulSoup/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
python3 pip install beautifulsoup4

---

Another handy package is the BeautifulSoup library (rather beautifulsoup4). This library makes working with HTML a lot easier in Python. BeautifulSoup turns the HTML into Python objects that are much easier to work with and allows us to analyze the content better programmatically.

# Further Improvements

## __main__ block
Recall what we discussed in the beginning about importing modules and that Python scripts are executed from top to bottom, even when imported. This means that if somebody were to import our script, e.g., reuse some of our functions (it could be ourselves), the code would run as soon as imported. The typical way to avoid this is to put all the code that does something into the "main" block. Let us do that:
The "main" Block
Code: python

if __name__ == '__main__':
    page_url = 'http://target:port'
    the_words = get_all_words_from(page_url)
    top_words = get_top_words_from(the_words)

    for i in range(10):
        print(top_words[i][0])
