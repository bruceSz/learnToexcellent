class GreekGetter:
    def __init__(self):
        self.trans = dict(dog='fdfd',cat='fdfdfdfdkfjei')
        
    def get(self,msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglishGetter:
    def get(self,msgid):
        return str(msgid)

def get_localizer(language = 'english'):
    languages = dict(English=EnglishGetter,Greek=GreekGetter)
    return languages[language]()

e,g = get_localizer("English"),get_localizer('Greek')
for msgid in "dog parrot cat bear".split():
    print (e.get(msgid),g.get(msgid))
