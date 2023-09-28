# Prompts the user to enter a value to convert seconds into minutes
dur = int(input("Enter a number to convert into minutes: "))
seconds = dur % 60
minutes = dur // 60
print(dur, "seconds is", minutes, "minutes and", seconds, "seconds.")
