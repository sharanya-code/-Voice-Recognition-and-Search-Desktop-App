import bs4
import requests
import lxml
import speech_recognition as sr
import pyttsx3 as p
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def recg_text(reg_text): #Function to covert into accepted hyperlink form
    re_list = reg_text.split()
    l = []
    re_text = ""
    for i in re_list:
        l.append(i)
        l.append('_')
    l.pop()
    for j in l:
        re_text = re_text + j
    return re_text


r = sr.Recognizer()
engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 120)
engine.say("Hello tell the name of the topic you need information about ")
engine.runAndWait()


with sr.Microphone() as source:
    text = r.listen(source)

    try:
        recgonised_text = r.recognize_google(text)


    except sr.UnknownValueError:
        engine = p.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty("rate", 120)
        engine.say("An error has occured")
        engine.runAndWait()


    except sr.RequestError as e:
        engine = p.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty("rate", 120)
        engine.say("An error has occured")
        engine.runAndWait()

hyper_text = recg_text(recgonised_text)

try:
    engine = p.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 120)
    engine.say("Close the Image Window to Proceed Towards the Information Section")
    engine.runAndWait()
    res = requests.get('https://en.wikipedia.org/wiki/'+hyper_text)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    image = soup.select('.thumbimage')[0]
    image_link = requests.get('https:' + image['src'])
    f = open('image.jpg', 'wb')
    f.write(image_link.content)
    f.close()

    img = mpimg.imread('image.jpg')
    imgplot = plt.imshow(img)
    plt.show()

except:
    engine = p.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 120)
    engine.say("No Internet")
    engine.runAndWait()


try:
    res = requests.get('https://en.wikipedia.org/wiki/'+hyper_text)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    information_list = soup.select('p')
    information = ""
    for i in range(0,len(information_list)):
        information = information + information_list[i].getText()
    print(information)
    engine = p.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 135)
    engine.say(information)
    engine.runAndWait()

except:
    engine = p.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 120)
    engine.say("No Internet")
    engine.runAndWait()

