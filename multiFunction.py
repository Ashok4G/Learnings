class Multifunction():
    def Subfields():
        AItopiclist =["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in AItopiclist:
            print(i)
    def oddEven():
        num=int(input("Enter a number: "))
        if num % 2 == 0:
            #print(f" {num} is Even number")
            output = "Even"
        else:
            #print(f" {num} is Odd number")
            output = "Odd"
        return output
    def Eligibility():
        Gender = input("Your Gender: ")
        Age= int(input("Your Age: "))
        if (Age>=18 and Gender.upper() == "FEMALE") or (Age>=20 and Gender.upper() == "MALE"):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        tot=sub1+sub2+sub3+sub4+sub5
        print("Total : ",tot)
        print("Percentage : ",tot/5)
    def triangle():
        height=int(input("Height: "))
        breadth=int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triange: ",(height*breadth)/2)
        height1=int(input("Height1: "))
        height2=int(input("Height2: "))
        breadth=int(input("Breadth: "))
        print("Perimeter formula: Height+Height+Breadth")
        print("Perimeter of Triangle: ",height1+height2+breadth)