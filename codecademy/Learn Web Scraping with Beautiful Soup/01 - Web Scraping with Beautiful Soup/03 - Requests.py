import requests

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')
print(webpage_response.text)

webpage = webpage_response.content
print(webpage)