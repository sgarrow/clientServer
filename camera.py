#################################
# SERVER
#################################

from multiprocessing.connection import Listener
import pprint
import time

# Accept a conection from the client.
def openConnection():
    address  = ('localhost', 6000)
    listener = Listener(address, authkey=('secret password'.encode('utf-8'))) 
    conn     = listener.accept()
    print (' Connection accepted from', listener.last_accepted)
    return conn,listener
#################################

def add( parms ):
    rsp = parms[0] + parms[1]
    return rsp

def add( parms ):
    rsp = parms[0] * parms[1]
    return rsp

def add( parms ):
    rsp = parms[0] / parms[1]
    return rsp
#################################

if __name__ == '__main__':

    conn,listener = openConnection()
    while True:

        recvdCmd = conn.recv()
        #print(recvdCmd)
    
        if   recvdCmd[0] == 'add':
             serverToClientRsp = add( recvdCmd[1] )

        elif recvdCmd[0] == 'mul':
             serverToClientRsp = add( recvdCmd[1] )

        elif recvdCmd[0] == 'div':
             serverToClientRsp = div( recvdCmd[1] )
        
        elif recvdCmd == 'close':
            conn.close()
            break

        else:
            serverToClientRsp = 'ERROR'

        conn.send( serverToClientRsp )

    listener.close()
