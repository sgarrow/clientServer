#############################################################################
# SERVER
# See comments at top of client.py,
#############################################################################

from multiprocessing.connection import Listener

# Accept a conection from the client.
def openConnection():
    address  = ('localhost', 6000)
    aListener = Listener(address, authkey='secret password'.encode('utf-8'))
    conn     = aListener.accept()
    print (' Connection accepted from', aListener.last_accepted)
    return conn,aListener
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

ver = ' v0.1.1 - 12-Jan-2025'
def gv( parms ):
    rsp = parms[0] / parms[1]
    return ver
#############################################################################

if __name__ == '__main__':

    strToFunctDict = { 'add' : add, 'mul' : mul, 'div' : div,'gv' : gv}

    connection,listener = openConnection()

    while True:
        recvdCmd = connection.recv()

        cmd = recvdCmd[0]

        if cmd in strToFunctDict:
            function = strToFunctDict[cmd]
            params   = recvdCmd[1]
            serverToClientRsp = function( params )

        elif cmd == 'close':
            listener.close()
            connection.close()
            break

        else:
            serverToClientRsp = 'ERROR'

        connection.send( serverToClientRsp ) # <-- sends a rsp to client
