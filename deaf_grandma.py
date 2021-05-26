
def deaf_grandma():
  current_counter = 0
  print("Your grandmather awaits...")
  print("WELL, OUT WITH IT!")
  while current_counter < 2:
    user_input = input("Test your grandmother with your nonsense \n")
    if user_input == "":
      print("WHAT?!")
    elif user_input.upper() != user_input:
      print("SPEAK UP, KID!")
    elif user_input == "GOODBYE!":
      current_counter = current_counter +1    
      if current_counter == 2:
        print("LATER, SKATER!")
        return
      print("LEAVING SO SOON?")
    else:
      print("NO NOT SENSE 1946!")

deaf_grandma()
