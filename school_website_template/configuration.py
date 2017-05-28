class Link:

    hyperlinks = {
        'STRONA GŁÓWNA': '/',
        'O NAS': '/aboutUs',
        'KONTAKT': '/contact',
        'GALERIA': '/gallery/all',
      #  'DODAJ POST': '/addPost'
    }
    links = {
        'STRONA GŁÓWNA': 'dropdown1',
        'O NAS': 'dropdown2',
        'KONTAKT': '0',
        'GALERIA': '0',
       # 'DODAJ POST': '0'
    }

    schoolName = "Z-SAT ROPCZYCE"

    links_footer = {
        "tutorial python": "https://www.learnpython.org/pl/",
        "tutorial django": "http://django-maly-bar.readthedocs.io/en/latest/index.html",
        "tutorial linux": "http://sequoia.ict.pwr.wroc.pl/~witold/linuxuwr/",
        "ZSA-T ROPCZYCE": "http://www.zsat-ropczyce.pl/"
    }

    chief = "Paweł Paśko"

    dropdown1 = {
        "MISJA I WIZJA SZKOŁY" : "#",
        "HISTORIA SZKOŁY": "#"
    }

    dropdown2 = {
        "PLIKI": "#",
        "E-LEARNING": "#"
    }

    def header(self):
        return self.links, self.hyperlinks, self.schoolName, self.links_footer, self.chief, self.dropdown1, self.dropdown2
