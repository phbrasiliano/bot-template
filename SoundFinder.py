import urllib
import re
from bs4 import BeautifulSoup

def reply_sound(bot, update, args):
    chat_id = update.message.chat_id
    try:
        term = str(' '.join(args))
        if term != "":
            sound_list = sound_finder(term)
        else:
            raise ValueError
        if len(sound_list) != 0:
            sound_name, sound_url = sound_list[0]
            sound = urllib.request.urlopen(sound_url)
            update.message.reply_audio(sound, title=sound_name, quote=True)
        else:
            update.message.reply_text("Não encontrei nada %s" % ("relacionado a " + term))
    except (IndexError, ValueError):
        update.message.reply_text('Use da seguinte forma: /sound "termo a ser pesquisado"')

'''this function returns a list with a maximum of 5 sounds,
 each item contain a tuple with a sound name and their url address'''

def sound_finder(term):
    term = '+'.join(term.split())
    url = 'https://www.myinstants.com/search/?name=%s' % term
    page = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    instants = page.find_all('div', attrs={'class': 'instant'}, limit=5)
    instant_list = []
    for i in instants:
        regex = re.compile("play\('(.*?)'\)")
        address = ('https://www.myinstants.com' + str(regex.search(str(i)).group(1)))
        title = i.find('a').get_text()
        instant_list.append([title, address])
    return instant_list