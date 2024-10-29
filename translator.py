from itertools import chain
import sys
import requests
from bs4 import BeautifulSoup
from soupsieve.util import lower


class Translator:
    def __init__(self):
        self.is_zero = False
        self.native_language = None
        self.target_language = None
        self.word_to_translate = None
        self.languages = {
            0: "all", 1: "arabic", 2: "german", 3: "english", 4: "spanish",
            5: "french", 6: "hebrew", 7: "japanese", 8: "dutch",
            9: "polish", 10: "portuguese", 11: "romanian",
            12: "russian", 13: "turkish"
        }
        self.args = None

    def parse_command_arguments(self):
        self.args = sys.argv
        if self.args[1] not in self.languages.values():
            print(f"Sorry, the program doesn't support {self.args[1]}")
            sys.exit()
        if self.args[2] not in self.languages.values():
            print(f"Sorry, the program doesn't support {self.args[2]}")
            sys.exit()

    def display_languages(self):
        print("Hello, welcome to the translator.\nTranslator supports:")
        for key, value in self.languages.items():
            if key != 0:
                print(f"{key}. {value}")

    def set_languages(self):
        self.native_language = self.args[1]
        self.target_language = self.args[2]

    def get_word_to_translate(self):
        self.word_to_translate = self.args[3]
        if self.target_language == 'all':
            for n in range(1, 14):
                self.target_language = lower(self.languages[n])
                if lower(self.native_language) != lower(self.target_language):
                    self.fetch_translation()
        else:
            self.fetch_translation()

    def fetch_translation(self):
        url = f'https://context.reverso.net/translation/{self.native_language}-{self.target_language}/{self.word_to_translate}'
        user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        )
        response = requests.get(url, headers={'User-Agent': user_agent})

        if response.status_code == 404:
            print(f"Sorry, unable to find {self.word_to_translate}")
            sys.exit()
        elif response.status_code != 200:
            print("Something wrong with your internet connection")
            sys.exit()

        self.extract_translation(response)

    def extract_translation(self, page):
        soup = BeautifulSoup(page.text, 'html.parser')
        words = soup.find_all('span', {'class': 'display-term'})
        examples = soup.find_all('div', {'class': 'example'})

        word_list = [word.get_text(strip=False) for word in words]
        example_list = [example.get_text(strip=True) for example in examples]

        raw_contents = BeautifulSoup(page.content, 'html.parser')
        translations = raw_contents.find_all('span', {'class': 'display-term'})
        sentences_src = raw_contents.find_all('div', {"class": "src ltr"})
        sentences_target = raw_contents.find_all('div', {
            "class": ["trg ltr", "trg rtl arabic", "trg rtl"]
        })

        translation_texts = set([t.get_text().strip() for t in translations])
        sentences = set([s.get_text().strip() for s in
                         list(chain(*[pair for pair in zip(sentences_src, sentences_target)]))])

        self.display_and_save(list(translation_texts), list(sentences))

    def display_and_save(self, translations, sentences):
        print(f"{self.target_language.capitalize()} Translations:")
        print(translations[0])
        print(f"{self.target_language.capitalize()} Examples:")
        print(sentences[0])
        print(sentences[1])

        with open(f"{self.word_to_translate}.txt", mode="a", encoding="utf-8") as file:
            file.write(f"{self.target_language.capitalize()} Translations:\n")
            file.write(f"{translations[0]}\n")
            file.write(f"{self.target_language.capitalize()} Examples:\n")
            file.write(f"{sentences[0]}\n")
            file.write(f"{sentences[1]}\n")

    def run(self):
        self.parse_command_arguments()
        self.set_languages()
        self.get_word_to_translate()


if __name__ == "__main__":
    translator = Translator()
    translator.run()
