#############################################################################
# SERVER
# See comments at top of client.py,
#############################################################################

from multiprocessing.connection import Listener

# Accept a conection from the client.
def openConnection():
    address  = ('localhost', 6000)
    listener = Listener(address, authkey=('secret password'.encode('utf-8'))) 
    conn     = listener.accept()
    print (' Connection accepted from', listener.last_accepted)
    return conn,listener
#############################################################################

def add( parms ):
    rsp = parms[0] + parms[1]
    return rsp

def mul( parms ):
    rsp = parms[0] * parms[1]
    return rsp

def div( parms ):
    rsp = parms[0] / parms[1]
    return rsp
#############################################################################

if __name__ == '__main__':

    strToFunctDict = { 'add' : add, 'mul' : mul, 'div' : div}

    conn,listener = openConnection()

    while True:
        recvdCmd = conn.recv()
    
        cmd = recvdCmd[0]

        if cmd in strToFunctDict:
            function = strToFunctDict[cmd]
            params   = recvdCmd[1]
            serverToClientRsp = function( params )
        
        elif cmd == 'close':
            listener.close()
            conn.close()
            break

        else:
            serverToClientRsp = 'ERROR'

        conn.send( serverToClientRsp ) # <-- sends a rsp to client
