import time
from flyt_python import api

def main():
    drone = api.navigation(timeout=120000)  # instance of flyt navigation class
    
    time.sleep(3)
    
    print 'Taking off to 10m'
    drone.take_off(10.0)
    
    print 'Moving in a triangular trajectory of side length 10m at a height of 10m'
    
    print 'Moving from Point A to B of triangle ABC'
    drone.position_set(8.0, 6.0, 10, relative=True)
    
    print 'Moving from Point B to C of triangle ABC'
    drone.position_set(-8.0, 6.0, 10, relative=True)
    
    print 'Moving back to Point A of triangle ABC'
    drone.position_set(0, -12, 10, relative=True)
    
    print 'Landing'
    drone.land(async=False)
    
    # Shutdown the instance
    drone.disconnect()



