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
    conn    = Client(address, authkey=('secret password'.encode('utf-8')))
    print()
    return conn
#############################################################################

def sndCmdRcvRsp(cmd):
    conn.send( cmd )                   # <-- 3. call send.
    rcvdRsp = conn.recv()              # <-- 4. call receive.
    return rcvdRsp 
#############################################################################

def add( parms ):
    rsp = sndCmdRcvRsp(['add', parms]) # <-- 2. call send/receive driver. 
    return(rsp) 
def mul( parms ):
    rsp = sndCmdRcvRsp(['mul', parms]) # <-- 2. call send/receive driver. 
    return(rsp)
def div( parms ):
    rsp = sndCmdRcvRsp(['div', parms]) # <-- 2. call send/receive driver.
    return(rsp) 
#############################################################################

if __name__ == '__main__':

    strToFunctDict = {
    'add' : {'func': add, 'parm': [1,5], 'menu': ' add '},
    'mul' : {'func': mul, 'parm': [2,9], 'menu': ' mul '},
    'div' : {'func': div, 'parm': [6,3], 'menu': ' div '},
    }

    conn = openConnection()

    while(1):
        choice = input( ' ***** Choice (m=menu, q=quit) -> ' )

        if choice in strToFunctDict:
            function= strToFunctDict[choice]['func']
            params  = strToFunctDict[choice]['parm']
            rtnVal  = function(params) # <-- 1. request a cmd be sent to server.
            print(rtnVal)

        elif choice == 'm':
            print()
            for k in strToFunctDict.keys():
                print('{}'.format(strToFunctDict[k]['menu'] ))
            print()

        elif choice == 'q':
            break

    conn.send( ['close'] )
    conn.close()
