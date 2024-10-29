Command-Line Translator
This is a Python command-line translator that leverages the Reverso Context service to provide translations and contextual examples for words across multiple languages. The script allows users to easily translate words and save the results for future reference.

Features
Multi-language Support: Translate words between various languages including Arabic, German, English, Spanish, French, Hebrew, Japanese, Dutch, Polish, Portuguese, Romanian, Russian, and Turkish.
Error Handling: Informative error messages for unsupported languages and connectivity issues.
Web Scraping: Utilizes requests and BeautifulSoup to extract translations and examples directly from Reverso Context.
Text File Output: Saves translations and examples in a text file named after the word being translated.
Prerequisites
Make sure you have Python installed on your machine. You also need to install the required packages. You can do this using pip:

bash
Skopiuj kod
pip install requests beautifulsoup4
Usage
Run the script using the command line with the following syntax:

bash
Skopiuj kod
python translator.py <native_language> <target_language> <word_to_translate>
native_language: The language of the word you want to translate (e.g., "english").
target_language: The language you want to translate to (e.g., "spanish" or "all" for multiple languages).
word_to_translate: The word you wish to translate.
Example Command:

bash
Skopiuj kod
python translator.py english spanish hello
Output: The translations and example sentences will be displayed in the console and saved in a text file named hello.txt.

Supported Languages
The following languages are supported:

Arabic
German
English
Spanish
French
Hebrew
Japanese
Dutch
Polish
Portuguese
Romanian
Russian
Turkish
Contributing
If you have suggestions or improvements, feel free to create an issue or submit a pull request.

License
This project is open-source and available under the MIT License.

Feel free to modify any section to better fit your preferences or add any additional information you think is necessary!
