#################################
# CLIENT
#################################

from multiprocessing.connection import Client
import pprint
import time

def openConnection():
    address = ('localhost', 6000)
    conn    = Client(address, authkey=('secret password'.encode('utf-8')))
    print()
    return conn
#################################

def sndCmdRcvRsp(cmd):
    conn.send( cmd )
    rcvdRsp = conn.recv()
    #print(rcvdRsp) 
    return rcvdRsp 
#################################

def add( parms ):
    rsp = sndCmdRcvRsp( ['add', parms] )
    print(rsp) 
def mul( parms ):
    rsp = sndCmdRcvRsp( ['mul', parms] )
    print(rsp) 
def div( parms ):
    rsp = sndCmdRcvRsp( ['div', parms] )
    print(rsp) 
#################################

if __name__ == '__main__':

    strToFunctDict = {
    'add' : {'func': add, 'parm': [1,3], 'menu': ' add '},
    'mul' : {'func': mul, 'parm': [4,5], 'menu': ' mul '},
    'div' : {'func': mul, 'parm': [6,7], 'menu': ' div '},
    }

    conn = openConnection()

    while(1):
        choice = input( ' ***** Choice (m=menu, q=quit) -> ' )

        if choice in strToFunctDict:
            rtnVal = strToFunctDict[choice]['func'](strToFunctDict[choice]['parm'])
            #print(rtnVal) 

        elif choice == 'm':
            print()
            [ print('{}'.format(strToFunctDict[k]['menu'] )) for k in strToFunctDict.keys() ]
            print()

        elif choice == 'q':
            break

    conn.send( 'close' )
    conn.close()
