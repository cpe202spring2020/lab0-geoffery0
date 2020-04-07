def weight_on_planets():
   bounce = input("What do you weigh on earth? \n")
   print("On Mars you would weigh {:.2f} pounds.\nOn Jupiter you would weigh {:.2f} pounds.".format(int(bounce)*.38,int(bounce)*2.34), end = "")
   
   
if __name__ == '__main__':
   weight_on_planets()