# -*- coding: utf-8 -*-
from collections import Counter
from blake3 import blake3
from pathlib import Path
import shutil
import time
import sys
import os
import re


# Start of Hash Functions
def GetHash():
    while True:
        try:
            os.system('title Get hash')
            os.system('cls')
            resultPath = r'./Hash.txt'

            while True:
                print('This uses Blake8 as the hasher\n')
                print(r'Example: C:\Pixiv')
                pathToHash = input('Enter directory to hash: ')
                print()

                if not os.path.exists(pathToHash) or not os.path.isdir(pathToHash):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a directory\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Hashing...\n')
            pathAndHash = []
            for path in Path(pathToHash).rglob('*'):
                blake = blake3()
                if not Path.is_dir(path):
                    with open(path, 'rb') as f:
                        blake.update(f.read())
                    pathAndHash.append(f'{str(path)}//{str(blake.hexdigest())}\n')
                    print(f'Files hashed: {len(pathAndHash)}', end='\r')
                else:
                    pass

            with open(resultPath, 'w', encoding='utf-8') as f:
                for line in pathAndHash:
                    f.write(line)

            print('\nDone!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            Main()

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            Main()


def GetHashDupeAndUnique():
    while True:
        try:
            os.system('title Get hash duplicate and unique')
            os.system('cls')
            resultUniquePath = r'./HashUnique.txt'
            resultDupePath = r'./HashDupe.txt'

            while True:
                print('Duplicates are counted when same file name and hash, everything else is unique\n')
                print(r'Example: C:\Users\User\Downloads\Hash.txt or Hash.txt')
                hashPath = input('Enter Hash path: ')
                print()

                if not os.path.exists(hashPath) or not os.path.isfile(hashPath):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a file\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            with open(hashPath, encoding='utf-8') as f:
                hashList = f.readlines()

            fileNameAndHash = []
            uniqueHash = []
            duplicateHash = []
            # Make list of only filename//hash
            for line in hashList:
                lineTuple = line.partition('//')
                fileName = os.path.basename(lineTuple[0])
                hash = lineTuple[2]
                fileNameAndHash.append(f'{fileName}//{hash}')

            # Count filename//hash
            fileNameAndHashCountDict = Counter(fileNameAndHash)

            # Find unique and dupe by count
            for index, line in enumerate(hashList):
                fileNameAndHashCount = fileNameAndHashCountDict.get(fileNameAndHash[index])

                if fileNameAndHashCount == 1:
                    uniqueHash.append(line)
                else:
                    duplicateHash.append(line)

            with open(resultUniquePath, 'w', encoding='utf-8') as f:
                for line in uniqueHash:
                    f.write(line)

            with open(resultDupePath, 'w', encoding='utf-8') as f:
                for line in duplicateHash:
                    f.write(line)

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            Main()

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            Main()


def GetHashDifference():
    while True:
        try:
            os.system('title Get hash difference')
            os.system('cls')
            resultPath = r'./HashDifference.txt'

            def Check():
                while True:
                    print(r'Example: C:\Users\User\Downloads\Hash.txt or Hash.txt')
                    hashPath = input('Enter Hash path: ')
                    print()

                    if not os.path.exists(hashPath) or not os.path.isfile(hashPath):
                        os.system('cls')
                        print(f'{bcolors.FAIL}Error: Path does not exist or not a file\n{bcolors.ENDC}')
                    else:
                        return hashPath

            print(f'{bcolors.WARNING}This will lose order{bcolors.ENDC}\n')
            print('First Hash\n')
            file1 = Check()
            print('Second Hash\n')
            file2 = Check()

            os.system('cls')
            print('Thinking...\n')
            with open(file1, encoding='utf-8') as f:
                hashFile1 = f.readlines()

            with open(file2, encoding='utf-8') as f:
                hashFile2 = f.readlines()

            # Find difference between 2 list, get item in list 1 not exist in list 2 and vice versa
            difference = set(hashFile1) ^ set(hashFile2)

            with open(resultPath, 'w', encoding='utf-8') as f:
                for line in difference:
                    f.write(line)

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            Main()

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            Main()


def SortHashByHash():
    while True:
        try:
            os.system('title Sort hash by hash')
            os.system('cls')
            resultPath = r'./HashSortedByHash.txt'

            while True:
                print(r'Example: C:\Users\User\Downloads\Hash.txt or Hash.txt')
                hashPath = input('Enter Hash path: ')
                print()

                if not os.path.exists(hashPath) or not os.path.isfile(hashPath):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a file\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            with open(hashPath, encoding='utf-8') as f:
                hashList = f.readlines()

            def KeySort(hashList):
                # Get hash, positive lookbehind, gets everything after '//'
                hashPattern = re.compile(r'(?<=\/\/).+')
                return list(map(str, hashPattern.findall(hashList)))

            hashList.sort(key=KeySort)

            with open(resultPath, 'w', encoding='utf-8') as f:
                for line in hashList:
                    f.write(line)

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            Main()

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            Main()


def SortHashByPixivID():
    while True:
        try:
            os.system('title Sort hash by Pixiv ID')
            os.system('cls')
            resultPath = r'./HashSortedByPixivID.txt'

            while True:
                print(r'Example: C:\Users\User\Downloads\Hash.txt or Hash.txt')
                hashPath = input('Enter Hash path: ')
                print()

                if not os.path.exists(hashPath) or not os.path.isfile(hashPath):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a file\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            with open(hashPath, encoding='utf-8') as f:
                hashList = f.readlines()

            def KeySort(hashList):
                # Get PixivID, matches '(1234)\', captures 1234
                pixivIDPattern = re.compile(r'\((\d+)\)\\')
                return list(map(str, pixivIDPattern.findall(hashList)))

            hashList.sort(key=KeySort)

            with open(resultPath, 'w', encoding='utf-8') as f:
                for line in hashList:
                    f.write(line)

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            Main()

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            Main()
# End of Hash Functions


# Start of Folder Functions
def RenamePixivFolders():
    while True:
        try:
            os.system('title Rename Pixiv folders')
            os.system('cls')

            while True:
                print("This will append 'old_' to the folders, it will not keep appending it if it startswith 'old_'\n")
                print(r'Example: C:\Pixiv')
                pixivPath = input('Enter directory to rename: ')
                print()

                if not os.path.exists(pixivPath) or not os.path.isdir(pixivPath):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a directory\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            for path in Path(pixivPath).glob('*'):
                if Path.is_dir(path) and not path.name.startswith('old_'):
                    path.rename(os.path.join(pixivPath, f'old_{path.name}'))

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            Main()

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            Main()


def MoveFiles():
    while True:
        try:
            os.system('title Move files to new folders')
            os.system('cls')

            while True:
                print(r'Example: C:\Users\User\Downloads\Hash.txt or Hash.txt')
                hashPath = input('Enter Hash path: ')
                print()

                if not os.path.exists(hashPath) or not os.path.isfile(hashPath):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a file\n{bcolors.ENDC}')
                else:
                    break

            with open(hashPath, encoding='utf-8') as f:
                hashList = f.readlines()

            os.system('cls')
            print('Thinking...\n')
            # Make new list of dupes and only keep one of same filename and hash
            singleDupeHashList = []
            visited = []
            for line in hashList:
                lineTuple = line.partition('//')
                fileName = os.path.basename(lineTuple[0])
                hash = lineTuple[2]
                fileNameAndHash = f'{fileName}//{hash}'

                if fileNameAndHash not in visited:
                    visited.append(fileNameAndHash)
                    singleDupeHashList.append(line)

            # Get PixivID and make list of files that has Pixiv ID, removes files without Pixiv ID
            pixivIDList = []
            moveHashList = []
            # Get PixivID, matches '(1234)\', captures 1234
            pixivIDPattern = re.compile(r'\((\d+)\)\\')
            for line in singleDupeHashList:
                if pixivIDPattern.findall(line):
                    pixivIDList.append(pixivIDPattern.findall(line))
                    moveHashList.append(line)

            # Get Pixiv folder path
            lineTuple = moveHashList[0].partition('//')
            pixivFolder = Path(lineTuple[0]).parents[1]

            # Move files to folder
            def MoveFiles(filePath, folderPath):
                os.makedirs(folderPath, exist_ok=True)
                fullFilePath = os.path.join(folderPath, os.path.basename(filePath))

                # Retry amount
                for i in range(5):
                    try:
                        if os.path.exists(filePath):
                            shutil.move(filePath, folderPath)
                        else:
                            print(f'File not found: {filePath}')
                        break
                    except shutil.Error:
                        fileTime = os.path.getctime(fullFilePath)
                        fileTime = time.strftime(r'%Y%m%d_%H%M%S', time.gmtime(fileTime))
                        os.rename(fullFilePath, f'{fullFilePath}.{fileTime}')

            fanboxPattern = re.compile(r'\\old_FANBOX')
            for index, line in enumerate(moveHashList):
                lineTuple = line.partition('//')
                filePath = lineTuple[0]

                if fanboxPattern.findall(line):
                    fanboxFolderPath = os.path.join(pixivFolder, f'FANBOX ({pixivIDList[index][0]})')
                    MoveFiles(filePath, fanboxFolderPath)
                else:
                    pixivFolderPath = os.path.join(pixivFolder, f'({pixivIDList[index][0]})')
                    MoveFiles(filePath, pixivFolderPath)

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            Main()

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            Main()


def MoveOldFolders():
    while True:
        try:
            os.system("title Move 'old_' folders to a separate folder")
            os.system('cls')

            while True:
                print("Moves folders that startswith 'old_' to '!old_Pixiv'")
                print('You can then delete this folder as it only contains duplicates\n')
                print(r'Example: C:\Pixiv')
                pixivPath = input('Enter Pixiv directory: ')
                print()

                if not os.path.exists(pixivPath) or not os.path.isdir(pixivPath):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a directory\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            oldFolder = '!old_Pixiv'

            os.makedirs(os.path.join(pixivPath, oldFolder), exist_ok=True)

            for path in Path(pixivPath).glob('old_*'):
                if Path.is_dir(path):
                    shutil.move(path, os.path.join(pixivPath, oldFolder))

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            Main()

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            Main()


def GetPixivFolderListAndPixivID():
    while True:
        try:
            os.system('title Get Pixiv folder list and Pixiv ID')
            os.system('cls')
            resultDirectoryPath = r'./PixivFolderDirectory.txt'
            resultIDPath = r'./PixivFolderPixivID.txt'

            while True:
                print('The result does not include folders without a Pixiv ID, keeps folders like ex. test (1234)')
                print(r'Example: C:\Pixiv')
                pixivPath = input('Enter Pixiv directory: ')
                print()

                if not os.path.exists(pixivPath) or not os.path.isdir(pixivPath):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a directory\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            directoryList = []
            pixivIDList = []
            # Get PixivID, matches '(1234)', captures 1234
            pixivIDPattern = re.compile(r'\((\d+)\)')
            for path in Path(pixivPath).glob('*'):
                if Path.is_dir(path) and pixivIDPattern.findall(str(path)):
                    directoryList.append(str(path))
                    pixivIDList.append(pixivIDPattern.findall(str(path)))

            with open(resultDirectoryPath, 'w', encoding='utf-8') as f:
                for line in directoryList:
                    f.write(f'{line}\n')

            with open(resultIDPath, 'w', encoding='utf-8') as f:
                for line in pixivIDList:
                    f.write(f'{line[0]}\n')

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            Main()

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            Main()


def Main():
    os.system('title Menu')
    os.system('cls')
    validOptions = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    while True:
        print(f'''
                        {bcolors.BOLD}Hash Functions{bcolors.ENDC}                          {bcolors.BOLD}Folder Functions{bcolors.ENDC}
                {bcolors.OKGREEN}
                [1] Get hash                             [6] Rename Pixiv folders
                [2] Get hash duplicate and unique        [7] Move files to new folders
                [3] Get hash difference                  [8] Move 'old_' folders to a separate folder
                [4] Sort hash by hash                    [9] Get Pixiv folder list and Pixiv ID
                [5] Sort hash by Pixiv ID

                {bcolors.WARNING}Press [CTRL + C] to exit functions{bcolors.ENDC}
                {bcolors.FAIL}Enter [Q] to Quit{bcolors.ENDC}
                ''')

        selected = input('Input: ')

        if (selected == 'q' or selected == 'Q'):
            sys.exit()
        elif selected not in validOptions:
            os.system('cls')
            print(f'{bcolors.FAIL}Please select a valid option{bcolors.ENDC}')
        elif selected == '1':
            GetHash()
        elif selected == '2':
            GetHashDupeAndUnique()
        elif selected == '3':
            GetHashDifference()
        elif selected == '4':
            SortHashByHash()
        elif selected == '5':
            SortHashByPixivID()
        elif selected == '6':
            RenamePixivFolders()
        elif selected == '7':
            MoveFiles()
        elif selected == '8':
            MoveOldFolders()
        elif selected == '9':
            GetPixivFolderListAndPixivID()


if __name__ == '__main__':
    os.system('color')

    class bcolors:
        HEADER    = '\033[95m'
        OKBLUE    = '\033[94m'
        OKGREEN   = '\033[92m'
        WARNING   = '\033[93m'
        FAIL      = '\033[91m'
        BOLD      = '\033[1m'
        UNDERLINE = '\033[4m'
        ENDC      = '\033[0m'

    Main()
