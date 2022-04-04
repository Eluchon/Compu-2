import argparse
import time, os

parser = argparse.ArgumentParser()
parser.add_argument("-n",type=int,help="-n x")
parser.add_argument("-v", "--verboso",help="Modo verboso",action="store_true")
args = parser.parse_args()  

def f_hijo():
    pares  = 0
    for i in range(0,os.getpid(),1):
        if i  %  2 == 0:
            pares += 1
        """time.sleep(1)"""
    print(" %d - %d : %d"  % (os.getpid(),os.getppid(),pares))
    os._exit(0)

for i in range(0,(args.n),1):
        pid = os.fork()
        if args.verboso:
            print("Iniciando proceso %d" % os.getpid())
        if pid==0: 
          f_hijo()
        pid,estado = os.wait()
        if args.verboso:
          print("Finalizando proceso %d" % os.getpid())




