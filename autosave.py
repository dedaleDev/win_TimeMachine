import os 
import TwoRepScanner
import tqdm
import filesAndDirectory


def autosave(disk1 ,disk2):
    filesDisk2 = TwoRepScanner.scanDisk(disk2)
    filesDisk1 = TwoRepScanner.scanDisk(disk1)
    for i in tqdm.tqdm(range(len(filesDisk1))):
        find = False
        for j in range(len(filesDisk2)):
            if filesDisk1[i][1] == filesDisk2[j][1] and filesAndDirectory.isUserFile(filesDisk1[i][1]):  # vérifier si le nom du fichier existe dans le deuxième dictionnaire
                find = True
                if not TwoRepScanner.isIdentique(str(filesDisk1[i][0]), str(filesDisk2[j][0])):
                    print(f"Le fichier {filesDisk1[i][0]} est différent de {filesDisk2[j][0]}")
                    print(f"Le fichier {filesDisk1[i][0]} est en cours de copie ...")
                    os.system(f"cp {filesDisk1[i][0]} {disk2+filesDisk1[i][0] }")
                    print(f"Le fichier {filesDisk1[i][0]} a été copié.")
                    break
        if not find and filesAndDirectory.isUserFile(filesDisk1[i][1]):
            print(f"Le fichier {filesDisk1[i][0]} est en cours de copie ...")
            os.system(f"cp {filesDisk1[i][0]} {disk2+filesDisk1[i][0] }")
            print(f"Le fichier {filesDisk1[i][0]} a été copié.")  
    print("La sauvegarde est terminée.")
