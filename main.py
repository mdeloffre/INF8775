import random
import math
import sys
import time
import csv
import os

from brute_force import execute_brute_force
from DpR import execute_DpR
from utils import GRID_SIZE

ALGO = sys.argv[1] # Algo à utiliser DPR ou BF
FILE_PATH = sys.argv[2] # Nombre de points à générer
DISPLAY_TIME = sys.argv[3] # 1 si on veut afficher le temps de calcul, 0 sinon
DISPLAY_RESULT = sys.argv[4] # 1 si on veut afficher le résultat, 0 sinon

'''
Un point est représenté par un tuple (position_x, position_y)
La fonction generate_points génère une liste de N points.
'''
def generate_points(N):
    points = [(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE)) for i in range(N)]
    return points

'''
--------------------------------------------------------------------
ATTENTION : Dans votre code vous devez utiliser le générateur gen.py
pour générer des points. Vous devez donc modifier ce code pour importer
les points depuis les fichiers générés.
De plus, vous devez faire en sorte que l'interface du tp.sh soit
compatible avec ce code (par exemple l'utilisation de flag -e, -a, (p et -t)).
--------------------------------------------------------------------
 '''

def get_sample_files(file_path):
    files = []
    for r, d, f in os.walk(file_path):
        for item in f:
            if '.txt' in item:
                files.append(os.path.join(r, item))
    return files
        
def process_single_file(algo, path, display_time, display_result):
    file_object = open(path, "r")
    values = file_object.readlines()
    n = int(values[0])
    POINTS = []

    for i in range(1,n+1):
        temp = values[i].split(" ")
        POINTS.append((int(temp[0]),int(temp[1])))

    sorted_points_x = sorted(POINTS, key=lambda x: x[0])
    sorted_points_y = sorted(POINTS, key=lambda x: x[1])

    if algo == "brute":
        # Exécuter l'algorithme force brute     
        time_BF = execute_brute_force(sorted_points_x, display_result)
        if (int(display_time) == 1):
            print("Temps : ", time_BF)
    
    elif algo == "recursif":
        # Exécuter l'algorithme Diviser pour régner
        time_DPR = execute_DpR(sorted_points_x, sorted_points_y, 2, display_result)
        if (int(display_time) == 1):
            print("Temps : ", time_DPR)
    
    elif algo == "seuil":
        # Exécuter l'algorithme Diviser pour régner avec un seuil expérimental
        time_DPR = execute_DpR(sorted_points_x, sorted_points_y, 16, display_result)
        if (display_time == "1"):
            print("Temps : ", time_DPR)
            
def main(algo, path, display_time, display_result):

    if '.txt' in path:
        process_single_file(algo, path, display_time, display_result)
    else: 
        files = get_sample_files(path)

              

    
main(ALGO, FILE_PATH, DISPLAY_TIME, DISPLAY_RESULT)