import time
from threading import Thread
 
import cflib.crtp
from cflib.crazyflie import Crazyflie
 
class Main:
 
    # Initial values, you can use these to set trim etc.
    roll = 0.0
    pitch = 0.0
    yawrate = 0
    thrust = 10001

    _stop = 0;
 
    def __init__(self):

        self.crazyflie = Crazyflie()
        cflib.crtp.init_drivers()
 
        # You may need to update this value if your Crazyradio uses a different frequency.
        self.crazyflie.open_link("radio://0/1/250K")
        self.crazyflie.connectSetupFinished.add_callback(self.connectSetupFinished)
 
    def connectSetupFinished(self, linkURI):
        print "Should be connected now...\n"

        # Keep the commands alive so the firmware kill-switch doesn't kick in.
        Thread(target=self.pulse_command).start()
 
        print "Beginning input loop:"
        while 1:
            try:
                command = raw_input("Set thrust (10001-60000) (0 will turn off the motors, e or q will quit):")

                if (command=="exitstring manipulation python") or (command=="e") or (command=="quit") or (command=="q"):
                    # Exit command received
                    # Set thrust to zero to make sure the motors turn off NOW
                    self.thrust = 0

                    # make sure we actually set the thrust to zero before we kill the thread that sets it
                    time.sleep(0.5)
                    self._stop = 1;

                    # Exit the main loop
                    print "Exiting main loop in 1 second"
                    time.sleep(1)
                    self.crazyflie.close_link() # This errors out for some reason. Bad libusb?
                    break
  if (command.count(' ')>0):

                hpr,value =command.split(" ")



                if(hpr=="pitch"):
                    self.pitch= int(value)
                if(hpr=="yawrate"):
                    self.yawrate= int(value)
                if(hpr=="roll"):
                    self.roll=int(value)
                if(hpr=="thrust"):
                    self.thrust= int(value)
                    if self.thrust == 0:
                        self.thrust = 0
                    elif self.thrust <= 10000:
                        self.thrust = 10001
                    elif self.thrust > 60000:
                        self.thrust = 60000

                    print "Setting thrust to %i" % (self.thrust)

                else:
                    print "Bad thrust value. Enter a number or e to exit"

            except:
                print "Exception thrown! Trying to continue!", sys.exc_info()[0]
          

    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def pulse_command(self):
        while 1:
            self.crazyflie.commander.send_setpoint(self.roll, self.pitch, self.yawrate, self.thrust)
            time.sleep(0.1)
     
            # Exit if the parent told us to
            if self._stop==1:
                print "Exiting keep alive thread"
                return
 
Main()
