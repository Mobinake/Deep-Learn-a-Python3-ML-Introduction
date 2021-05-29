#submodulos para usar: Updater, Dispatcher, commandandler, messagehandler, filters
from telegram import Update
from telegram.ext import Updater, CommandHandler, Dispatcher, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hola bienvenido a mi primer bot beta")   #mensaje de bienvenida

def main():
    updater = Updater('1813549646:AAGu13KKNpZV0mcbd0ICkjePW3JMMzdiRrU') #el token del bot, se le envia al bot
    dispatcher = updater.dispatcher #donde estan los controles para ejecutar

    comienza = CommandHandler('start', start)   #comenzar el comando
    dispatcher.add_handler(comienza)    #reconocer el comando
    updater.start_polling() #inicializar el bot
    updater.idle()  #ejecutar sin termianr

if( __name__ =='__main__'):
    main()

# ejemplos de bots: https://github.com/search?q=bot+telegram
# pagina: https://core.telegram.org/bots/api
# bot para crear bots: @BotFather







