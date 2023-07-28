import hashlib
import tkinter as tk
from tkinter import filedialog

def calc_blake2b(palabra):
    return hashlib.blake2b(palabra.encode()).hexdigest()

def calc_blake2s(palabra):
    return hashlib.blake2s(palabra.encode()).hexdigest()

def calc_md5(palabra):
    return hashlib.md5(palabra.encode()).hexdigest()

def calc_sha256(palabra):
    return hashlib.sha256(palabra.encode()).hexdigest()

def calc_sha512(palabra):
    return hashlib.sha512(palabra.encode()).hexdigest()

def calculate_hashes(words, function):
    hashes = {}

    if function == 1:
        hashing_func = calc_blake2b
    elif function == 2:
        hashing_func = calc_blake2s
    elif function == 3:
        hashing_func = calc_md5
    elif function == 4:
        hashing_func = calc_sha256
    elif function == 5:
        hashing_func = calc_sha512
    else:
        print("Invalid input. Please choose a valid option (1 to 5).")
        return

    for word in words:
        hash_value = hashing_func(word)
        hashes[word] = hash_value

    for word, hash_value in hashes.items():
        print(f"Hash of '{word}': {hash_value}")

def open_file_and_calculate_hashes():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select File")
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()

    function = int(input("Select one option\n"
                        "[1]calculate blake2b hash\n"
                        "[2]calculate blake2s hash\n"
                        "[3]calculate md5 hash\n"
                        "[4]calculate sha256 hash\n"
                        "[5]calculate sha512 hash\n"
                        ))

    calculate_hashes(words, function)

if __name__ == "__main__":
    option = int(input("Select an option: \n"
                       "[1]Mass Hasher\n"
                       "[2]Normal Hasher\n"))

    if option == 1:
        open_file_and_calculate_hashes()
    elif option == 2:
        wanted = input("Enter the words that you want to get encoded: ")
        function = int(input("Select one option\n"
                             "[1]calculate blake2b hash\n"
                             "[2]calculate blake2s hash\n"
                             "[3]calculate md5 hash\n"
                             "[4]calculate sha256 hash\n"
                             "[5]calculate sha512 hash\n"
                            ))

        words = wanted.split()
        calculate_hashes(words, function)
    else:
        print("Invalid input. Please choose a valid option (1 or 2).")


