#################################
# CCLI
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

def sndCmsRcvRsp(cmd):
    conn.send( cmd )
    rcvdRsp = conn.recv()
    #print(rcvdRsp) 
    return rcvdRsp 
#################################

def twoPointNuc( manuallyStepping ):

    print()
    if not manuallyStepping:
        rsp = sndCmsRcvRsp( [ 'sp8', 'capture1', -1 ] )
        print(rsp) 
        rsp = sndCmsRcvRsp( [ 'sp8', 'capture2', -1 ] )
        print(rsp) 
        rsp = sndCmsRcvRsp( [ 'sp8', 'calc1',    -1 ] )
        print(rsp) 
        rsp = sndCmsRcvRsp( [ 'sp8', 'calc2',    -1 ] )
        print(rsp) 
    else:

        proceed = True
        while proceed:
            process = None
            while process not in [ 'cp1', 'cp2', 'cl1', 'cl2', 'q' ]:
                print()
                print( ' Which command table do you want to execute from,' )
                print( ' capt1, capt2, calc1, calc2, quit' )
                process = input( ' cp1, cp2, cl1, cl2, q    --> '       )
            if process == 'q': return 0
    
            step = None
            while True:
                print( ' Which step in the command table do you want to execute,' )
                step = input( ' 1 thru N or q --> '       )
                try: 
                    step = int(step)
                    break
                except: 
                    if step == 'q': return 0
    
            if   process == 'cp1': 
                rsp = sndCmsRcvRsp([ 'sp8', 'capture1', step ])
                print(rsp) 
            elif process == 'cp2': 
                rsp = sndCmsRcvRsp([ 'sp8', 'capture2', step ])
                print(rsp) 
            elif process == 'cl1': 
                rsp = sndCmsRcvRsp([ 'sp8', 'calc1',    step ])
                print(rsp) 
            elif process == 'cl2': 
                rsp = sndCmsRcvRsp([ 'sp8', 'calc2',    step ])
                print(rsp) 
            else: print( ' ERROR' )

            while proceed not in [ 'c', 'q' ]:
                proceed = input( ' Continue or Quit (c/q)  --> '       )
            if proceed == 'q': return 0
#################################
    
def getParm():
    return 0
def setParm():
    return 0
#################################

if __name__ == '__main__':

    strToFunctDict = {
    'tpnf'   : {'func': twoPointNuc, 'parm': False, 'menu': '   tpnf - Two Point NUC. '},
    'tpns'   : {'func': twoPointNuc, 'parm': True,  'menu': '   tpns - Two Point NUC - Step. '},
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
