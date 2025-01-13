#############################################################################
# CLIENT
# Start the Server first, in it's own window: python server.py.
# Then start this client, in it's own window: python client.py.
# Then, in the client window, type m (for menu) to see available commands.
# Type one of the available commands (repeat as desired).
#
# The 'command' (a text string) along with the parameters (a hard coded list
# of two  integers) is sent to the server over a 'multiprocessing.connection'.
#
# The Server processes the command and returns the 'response' to this client.
# The client prints the response in it's own window.
# m (menu) can also be entered at any time.
#
# When done enter q (quit) to terminate server and client.
#############################################################################

from multiprocessing.connection import Client

def openConnection():
    address = ('localhost', 6000)
    conn    = Client(address, authkey='secret password'.encode('utf-8'))
    print()
    return conn
#############################################################################

def sndCmdRcvRsp(connection, cmd):
    connection.send( cmd )                   # <-- 3. call send.
    rcvdRsp = connection.recv()              # <-- 4. call receive.
    return rcvdRsp
#############################################################################

def add( connection, parms ):
    rsp = sndCmdRcvRsp(connection,['add', parms]) # <-- 2. call send/receive driver.
    return rsp

def mul( connection, parms ):
    rsp = sndCmdRcvRsp(connection,['mul', parms]) # <-- 2. call send/receive driver.
    return rsp

def div( connection, parms ):
    rsp = sndCmdRcvRsp(connection,['div', parms]) # <-- 2. call send/receive driver.
    return rsp

def gv( connection, parms ):
    rsp = sndCmdRcvRsp(connection,['gv', parms]) # <-- 2. call send/receive driver.
    return rsp
#############################################################################

if __name__ == '__main__':

    clientConn = openConnection()

    strToFunctDict = {
    'add' : {'func': add, 'parm': [1,5], 'conn': clientConn, 'menu': 'add '},
    'mul' : {'func': mul, 'parm': [2,9], 'conn': clientConn, 'menu': 'mul '},
    'div' : {'func': div, 'parm': [6,3], 'conn': clientConn, 'menu': 'div '},
    'gv'  : {'func':  gv, 'parm': [6,3], 'conn': clientConn, 'menu': 'gv  '},
    }

    while True:
        choice = input( ' ***** Choice (m=menu, q=quit) -> ' )

        if choice in strToFunctDict:
            function = strToFunctDict[choice]['func']
            params   = strToFunctDict[choice]['parm']
            clntConn = strToFunctDict[choice]['conn']
            rtnVal   = function( clntConn, params ) # <-- 1. request a cmd be sent to server.
            print('***',rtnVal)

        elif choice == 'm':
            print()
            for k,v in strToFunctDict.items():
                print('{} - {}'.format(k,v['menu'] ))
            print()

        elif choice == 'q':
            break

    clientConn.send( ['close'] )
    clientConn.close()
