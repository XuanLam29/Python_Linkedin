#
# Example file for working with conditional statements
#


'''def main():
    x, y = 10, 100'''

    # conditional flow uses if, elif, else

    # conditional statements let you use "a if C else b"


'''if __name__ == "__main__":
    main()
'''

#giải phương trình bậc 2

from math import sqrt
a = float(input("nhap he so a: "))
b = float(input("nhap he so b: "))
c = float(input("nhap he so c: "))
delta = b**2-4*a*c
if delta<0 : 
    print("Phuong trinh vo nghiem")
elif delta == 0:
   x = -b/2*a
   print("Phuong trinh co mot nghiem kep ",x)
else:
    x1 = (-b + sqrt(delta))/(2*a)
    x2 = (-b - sqrt(delta))/(2*a)
    print("Phuong trinh co 2 nghiem:\n x1= ", x1, "\n x2", x2)