from LMotors import Motor

#r = Motor('51FF-7106-4980-4956-5739-1387')
r = Motor('51FF-7B06-4980-4956-2030-1087')
l = Motor('51FF-7406-4980-4956-3330-1087')
#l = Motor('51FF-6F06-4980-4956-2739-1387')

def move(speedl, speedr):
    r.set(speedr)
    l.set(speedl)

def fullfor():
    r.set(400)
    l.set(400)

def fullback():
    r.set(-400)
    l.set(-400)

def stop():
    r.stop()
    l.stop()
