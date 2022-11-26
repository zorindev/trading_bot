


# config
CONFIG_MESSAGE_QUEUE        = "message_queue"

CONFIG_SIGNAL_QUEUE         =  "signal_queue"

CONFIG_WEBSOCKET            =     "websocket"

CONFIG_ENCODER              =       "encoder"
####################


# message handler

MSG_HNDLR_ACTION_START              =        "start"

MSG_HNDLR_ACTION_STOP               =         "stop"

MSG_HNDLR_ACTION_PAUSE              =        "pause"

MSG_HNDLR_ACTION_RESUME             =       "resume"

MSG_HNDLR_ACTION_STATUS             =       "status"

MSG_HNDL_CLNT_MESSAGE_ID            =           "id"

MSG_HNDL_CLNT_MESSAGE_TIMESTAMP     =    "timestamp"

MSG_HNDL_CLNT_MESSAGE_VALUE         =        "value"
####################

# transmission
TRANMISSION_FREQUENCEY      =  10

TRANSMISSION_OFF            = -1

TRANSMISSION_NEUTRAL        =  0

TRANSMISSION_GEAR           =  1
#####################


# engine
ENGINE_STATE_OFF                =  -1   # enging has not been started

ENGINE_STATE_SEARCHING          =   0   # engine has been started, it is searching for spot or margin

ENGINE_STATE_BUY                =   1   # a condition to perform a buy order is being determined

ENGINE_STATE_BOUGHT             =   2   # a buy order has been completed

ENGINE_STATE_SELL               =   3   # a sell order is determined 

ENGINE_STATE_SOLD               =   4   # a sold order is completed

ENGINE_STATE_BORROW_SELL        =   5   # a marging borrow_sell order is being determined

ENGINE_STATE_BORROW_SOLD        =   6   # a borrow_sell order has been completed

ENGINE_STATE_BORROW_REPAY       =   7   # a condition to repay the borrowed is being determined

ENGINE_STATE_BORROW_REPAYED     =   8   # a borrowed order is repayed

ENGINE_STATE_PAUSE              =   9   # pauses the engine

ENGINE_FREQUENCY                =   10
#####################
