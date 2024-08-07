import os
import pyfiglet

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_banner():
    clear_screen()
    if os.name == 'nt':
        fig = pyfiglet.figlet_format("IMG - SECURE", font="banner3-D", width=80)
        print("\n")
        print(fig)
        fig2 = pyfiglet.figlet_format("By - MR.SIDDHESH", font="digital")
        print(fig2)
        print(" - An Image Encryption & Decryption Tool based on Pixel Manipulation")
        print("\n")
    else:
        fig = pyfiglet.figlet_format("IMG - SECURE", font="standard", width=80)
        print("\n")
        print(fig)
        fig2 = pyfiglet.figlet_format("By - MR.SIDDHESH", font="standard")
        print(fig2)
        print(" - An Image Encryption & Decryption Tool based on Pixel Manipulation")
        print("\n")

def encrypt_decrypt_image(path, key):
    try:
        with open(path, 'rb') as file:
            image = bytearray(file.read())

        for index, value in enumerate(image):
            image[index] = value ^ key

        with open(path, 'wb') as file:
            file.write(image)

        print(f'\nOperation completed successfully!')
    except Exception as e:
        print(f'Error: {e}')

def main():
    print_banner()

    path = input(r'Enter path of Image: ')
    key = int(input('\nEnter Key for Encryption/Decryption of Image (0-255): '))

    if key < 0 or key > 255:
        print('\nKey must be in the range 0-255.')
        return

    mode = input('\nEnter mode (encrypt/decrypt): ').strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print('\nInvalid mode selected. Please choose "encrypt" or "decrypt".')
        return

    encrypt_decrypt_image(path, key)

if __name__ == '__main__':
    main()
