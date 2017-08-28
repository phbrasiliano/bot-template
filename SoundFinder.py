# import urllib.request
# import urllib.parse
import urllib
import re
from bs4 import BeautifulSoup

def reply_sound(bot, update, args):
    """Adds a job to the queue"""
    chat_id = update.message.chat_id
    try:
        term = str(' '.join(args))
        if term != "":
            sound = sound_finder(term)
        else:
            sound = False

        if sound:
            update.message.reply_audio(sound, title="your sound", quote=True)
        else:
            update.message.reply_text("Não encontrei nada %s" % ("relacionado a " + term))
    except (IndexError, ValueError):
        update.message.reply_text('Use da seguinte forma: /sound "termo a ser pesquisado"')


def sound_finder(term):
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"
    term = urllib.parse.quote(term)
    opener = AppURLopener()
    screen1 = (opener.open('https://www.myinstants.com/search/?name=%s' % term)).read()
    m = re.search('/instant/(.+?)/', str(screen1))
    if m:
        key1 = m.group(1)
        screen2 = opener.open('https://www.myinstants.com/instant/%s/' % key1).read()
        m = re.search('href="/media/sounds(.+?)mp3" d', str(screen2))
        if m:
            key2 = m.group(1)
            final_url = 'https://www.myinstants.com/media/sounds/%smp3' % key2
            print('audio link: ', final_url)
            final_file = opener.open(final_url)
            return final_file


'''this function returns a list with a maximum of 5 sounds,
 each item contain a sound name and their url address'''

def sound_finder2(term):
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