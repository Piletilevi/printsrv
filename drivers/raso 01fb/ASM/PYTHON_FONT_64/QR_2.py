﻿import System
from System import *
import time
#----------------------------------------------------------------------------
oo=Type.GetTypeFromProgID("POS.SA97")
fb=Activator.CreateInstance(oo)
fb.Init("COM3",57600,15)
#----------------------------------------------------------------------------
# Close last receipt (if any is open)
fb.FCancel()
#----------------------------------------------------------------------------
# Print empty line
fb.Print(" ")
# Print note line
fb.Print(" QR code:")
#----------------------------------------------------------------------------
# QR printing position (align: left)
fb.SendEsc("1B6100")
# QR code size
fb.SendEsc("1D286B0300314306")
#fb.SendEsc("1D286B0300314304")
#-----------------------------
# QR code load to printer memory
#                 15+3       L a b a _ d i e n a ! ! ! 
#b.SendEsc("1D286B11003150304c616261206469656e612121210D0A")
#                 69+3       L a b a _ d i e n a ! ! ! 
#b.SendEsc("1D286B48003150304c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121")
#                 138+3
#b.SendEsc("1D286B8D003150304c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121")
#                 276+3
#b.SendEsc("1D286B17013150304c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212145")
#                 552+3
fb.SendEsc("1D286B2B023150304c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121454c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e612121214c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212121204c616261206469656e61212145")
#-----------------------------
# QR print code from memory
fb.SendEsc("1D286B0300315130")
# Printing position (align: left)
fb.SendEsc("1B6100")
#----------------------------------------------------------------------------
# Close not fiscal receipt
fb.NFFinish()
#----------------------------------------------------------------------------
# Close port
fb.Close()