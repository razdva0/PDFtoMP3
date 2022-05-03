from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint
import sys


def pdf_to_mp3(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', ' ')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!\n---Have a good day!---'

    else:
        return 'File not exists, check the file path!'


def main(file_path):
    tprint('PDF>>TO>>MP3', font='univers')
    language = input('Choose language, for example "en" or "ru": ')
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
