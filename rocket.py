from time import sleep

def printRocket():
    print(
            """
            
            
                    -
                  /   \\
                  | - |
                  |   |
                 /     \\
                /       \\
                    
            """ )
    
def printPlatform():
    print(
        """

        ___________________________

        """ )
 

printRocket()
printPlatform()

delay = 300
for i in range(60):
    print()
    sleep(delay/1000)
    delay = delay * 0.9
