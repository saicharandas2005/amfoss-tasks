import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 


bot = telebot.TeleBot("5646624555:AAEKIJRn1M7t_99LMO6k7rGar7zo-6H5d6U")

csvheader=["Title", "Year", "Released", "imdbRating"]
with open('movies.csv','w',newline='') as  csvfile:
     writer=csv.writer(csvfile)
     writer.writerow(csvheader)
     
@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message,'1.0 You can u0se \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    
    a=str(message.text)
    b=a.replace('/movie ','')
    
    # TODO: 1.2 Get movie information from the API
    details=[]
    r=requests.get(f"https://www.omdbapi.com/?apikey=9aacc207&t={b}")
    # TODO: 1.3 Show the movie information in the chat window
    data=json.loads(r.text)
    details.append(data['Title'])
    details.append(data['Year'])
    details.append(data['Released'])
    details.append(data['imdbRating'])
    
    bot.send_photo(message.chat.id,data['Poster'],caption="Title:"+details[0]+ "\n"+"Year of release:"+details[1]+ "\n"+"Released: "+details[2]+ "\n"+"imdbRating: "+details[3])
    
    with open('movies.csv','a+',newline='') as csvfile:
         writer=csv.writer(csvfile)
         
         writer.writerow(details)
         
         
details=[]

    # TODO: 2.1 Create a CSV file and dump the movie information in it

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    doc = open('movies.csv', 'rb')
    bot.send_document(message.chat.id, doc)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
