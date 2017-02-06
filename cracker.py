import crypt
import sys

def compareHash(hashedPW):
    salt = hashedPW[0:2]
    dictFile = open('cain.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        if (crypt.crypt(word, salt) == hashedPW):
            print ("Found Password: "+word+"\n")
            return
    print ("No password found\n")
    return


def main():
    if len(sys.argv) != 3:
        print('\nUsage: cracker.py [file_of_password] [salt]\n')
        return

    salt = sys.argv[2] 
    filename = sys.argv[1] 
    hashedPWs = 'hashedPWs.txt' 

    hashedPWsFile = open('hashedPWs.txt', 'w')
    passwordFile = open(filename, 'r')

    for password in passwordFile.readlines():
        password = password.strip('\n')
        hashedPWsFile.write("%s\n" % (crypt.crypt(password, salt)))

    passwordFile.close()
    hashedPWsFile.close()

    hashedPWFile = open(hashedPWs, 'r')

    for hashedPW in hashedPWFile.readlines():
        hashedPW = hashedPW.strip('\n')
        compareHash(hashedPW)

    hashedPWFile.close()

if __name__ == "__main__":
    main()