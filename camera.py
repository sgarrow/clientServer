#################################
# CAMERA
#################################

from multiprocessing.connection import Listener
import pprint
import time

# Accept a conection from the ccli.
def openConnection():
    address  = ('localhost', 6000)
    listener = Listener(address, authkey=('secret password'.encode('utf-8'))) 
    conn     = listener.accept()
    print (' Connection accepted from', listener.last_accepted)
    return conn,listener
#################################

#  capture1, capture2, calc1, calc2 (tpnf) command handlers.

def capture1( tableStepOrAll, mdDict ):
    rsp = 'capture1 \n'
    if tableStepOrAll == -1:
        for ii in range( mdDict['capture1']['maximum']):
            rsp += '   step-{} complete \n'.format(ii)
    else:
        rsp += '   step-{} complete \n'.format(tableStepOrAll)
    return rsp

def capture2( tableStepOrAll, mdDict ):
    rsp = 'capture2 \n'
    if tableStepOrAll == -1:
        for ii in range( mdDict['capture2']['maximum']):
            rsp += '   step-{} complete \n'.format(ii)
    else:
        rsp += '   step-{} complete \n'.format(tableStepOrAll)
    return rsp

def calc1( tableStepOrAll, mdDict ):
    rsp = 'calc1 \n'
    if tableStepOrAll == -1:
        for ii in range( mdDict['calc1']['maximum']):
            rsp += '   step-{} complete \n'.format(ii)
    else:
        rsp += '   step-{} complete \n'.format(tableStepOrAll)
    return rsp

def calc2( tableStepOrAll, mdDict ):
    rsp = 'calc2 \n'
    if tableStepOrAll == -1:
        for ii in range( mdDict['calc2']['maximum']):
            rsp += '   step-{} complete \n'.format(ii)
    else:
        rsp += '   step-{} complete \n'.format(tableStepOrAll)
    return rsp

#################################

#  get/sewt parm handlers
def getParm():
    return 0
def setParm():
    return 0
#################################

#  gatpm8 command handler.
def gatpm8():
    return 0

# global variables.
capture1_currStep   = 0
capture2_currStep   = 0
calc1_currStep      = 0
calc2_currStep      = 0

capture1_totalSteps = 3
capture2_totalSteps = 4
calc1_totalSteps    = 5
calc2_totalSteps    = 6
#################################

if __name__ == '__main__':

    # Trigger parms to kick off various NUC operations.
    parmMetaDataDict  = \
    {   # Number of steps to execute. e.g., calc2 consist  of 6,  steps and,
        # by default, executes them all  on receipt of a  singel SDK call.
        # This is in contrast to optionally  executing only the specified 
        # step.  The later option provides the option of skipping steps 
        # thereby, for example, allowing one to load a know pattern into a 
        # capture buffer (and skipping the camera's internal capture process).
        'capture1' : { 'defVal': -1, 'minimum': 0, 'maximum': 3 },
        'capture2' : { 'defVal': -1, 'minimum': 0, 'maximum': 4 },
        'calc1'    : { 'defVal': -1, 'minimum': 0, 'maximum': 5 },
        'calc2'    : { 'defVal': -1, 'minimum': 0, 'maximum': 6 }
    }

    conn,listener = openConnection()
    while True:

        recvdCmd = conn.recv()
        #print(recvdCmd)
    
        if   recvdCmd[0] == 'sp8' and recvdCmd[1] == 'capture1':
            camToCcliRsp  = capture1( recvdCmd[2], parmMetaDataDict )

        elif recvdCmd[0] == 'sp8' and recvdCmd[1] == 'capture2':
            camToCcliRsp  = capture2( recvdCmd[2], parmMetaDataDict )
        
        elif recvdCmd[0] == 'sp8' and recvdCmd[1] == 'calc1':
            camToCcliRsp  = calc1(    recvdCmd[2], parmMetaDataDict )
        
        elif recvdCmd[0] == 'sp8' and recvdCmd[1] == 'calc2':
            camToCcliRsp  = calc2(    recvdCmd[2], parmMetaDataDict )
        
        elif recvdCmd == 'close':
            conn.close()
            break

        else:
            camToCcliRsp = 'ERROR'

        conn.send( camToCcliRsp )

    listener.close()

