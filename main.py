from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final

TOKEN: Final ='8158046215:AAFAQK6CjU09OdpZ4pec-ted34B1g0CLR7M'
BOT_USERNAME: Final ='@arabicnamesbot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Спасибо, что выбрал(а) меня. Напиши свое имя на русском или английском и я покажу как оно пишется на одном из самых древних и самых богатых языков мира!')
    

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Спасибо, что выбрал(а) меня')


   









def handle_response(text: str) -> str:
    text = text.lower()
    if 'thank you' in text or 'спасибо' in text:
        return "Welcome"
    mapping = {
        'a': 'ا',
        'b': 'ب',
        'c': 'ك',
        'd': 'د',
        'e': 'ي',
        'f': 'ف',
        'g': 'ج',
        'h': 'ه',
        'i': 'ي',
        'j': 'ج',
        'k': 'ك',
        'l': 'ل',
        'm': 'م',
        'n': 'ن',
        'o': 'و',
        'p': 'ب',
        'q': 'ق',
        'r': 'ر',
        's': 'س',
        't': 'ت',
        'u': 'و',
        'v': 'ف',
        'w': 'و',
        'x': 'كس',
        'y': 'ي',
        'z': 'ز',

        'а': 'ا',
        'б': 'ب',
        'в': 'ف',
        'г': 'ج',
        'д': 'د',
        'е': 'ي',
        'ё': 'ي و',  # approximate "yo"
        'ж': 'ج',
        'з': 'ز',
        'и': 'ي',
        'й': 'ي',
        'к': 'ك',
        'л': 'ل',
        'м': 'م',
        'н': 'ن',
        'о': 'و',
        'п': 'ب',
        'р': 'ر',
        'с': 'س',
        'т': 'ت',
        'у': 'و',
        'ф': 'ف',
        'х': 'خ',
        'ц': 'س',  # closest approximation
        'ч': 'تش',
        'ш': 'ش',
        'щ': 'ش',  # approximate
        'ъ': '',   # hard sign, no sound
        'ы': 'ع ي',  # deep vowel approx.
        'ь': '',   # soft sign, no sound
        'э': 'ا ي',  # approximate "e"
        'ю': 'ي و',
        'я': 'ي ا',
    }
    result = ''
    if text.startswith('a') or text.startswith('а'):
        result += 'ع'
        for ch in text[1:]:
     
            result += mapping.get(ch, ch)  
        return result
    else:
        for ch in text:
     
            result += mapping.get(ch, ch)  
        return result

    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type 
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:

            return 
    else:
        response: str = handle_response(text)
        
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)
    print('Polling...')
    app.run_polling(poll_interval=3)