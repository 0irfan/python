import logging
import sys
# Printing Value Using print function
print("Hello World!")

print(9)

print(0.5)

# Alternative way of printing value
sys.stdout.write("Day_1 in Coding")
  

logging.basicConfig(level=logging.INFO)
logging.info("Enjoying Day_1")
logging.info(7)
logging.info(3.5)


with open("output.txt",'w') as f:
    f.write("3rd Way of printint value") #this will create new file output.txt 
    # f.write(8) TypeError write function accept str argument only 
    # f.write(5.5)
