import os

def main():

    path = "/Volumes/Seagate Backup Plus Drive/Radio/Promos/"

    for filename in os.listdir(path):

        dst = filename[4:]
        src = path + filename
        dst = path + dst
        os.rename(src, dst)

if __name__ == '__main__':

  main()
