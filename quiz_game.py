print("Welcome to  my computer quiz!..")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! Lets play :)")
score = 0

answer = input("what does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect..!!")

answer = input("What does GPU stand for ? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect..!!")

answer = input("What does RAM standard for ? ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print("incorrect..!!")


answer = input("What does PSU stand for ? ")
if answer.lower() == "power supply unit":
    print('correct!')
    score += 1
else:
    print("incorrect..!!")

print(" You got " + str(score) + " marks and " +
      str((score/4)*100)+'% ' " questions coreect!")
