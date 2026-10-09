def information(**Kwargs):
    print("Your information is \n")
    for i in Kwargs:
        print(f"{i} : {Kwargs[i]}")

information(name = "Priyansh" , age = 20 , specialization = "AI/Ml")