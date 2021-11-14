import wikipedia

search_topic = input('Enter a search topic: ')

top_result = wikipedia.search(search_topic)[0]

print(wikipedia.summary(top_result))