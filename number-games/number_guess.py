import random

num = str(random.randrange(10, 100))
guess = "0"
guess_count = 1 # The guess the player is on. Will be used for divisibility.
is_prime = False 

# print(num) --- Used for testing purposes

while guess != num and guess.isdigit():
    if is_prime == False: # Will always be false before 4 guesses.
    
       if guess_count >= 2: 

           # Start giving hints to the player.
          if int(num) % guess_count == 0:
              print("The number is divisible by", guess_count) 
              # Lets them know that the number is divisible by 2, 3, etc.

          else:
              for i in range(2, int(num)):
              # Checks for a prime number.

                  if int(num) % i == 0:
                      print("The number is not divisible by", guess_count)
                      # The number is not divisible by guess_count but is not prime
                      break
                  else:
                      if guess_count >= 3:
                          print("The number is a prime number")
                          is_prime = True # From now on, the loop will follow prime rules
                          break
                      else:
                          print("The number is not divisible by", guess_count) 
                          # They won't know it is a prime number until after 3 guesses     
                          break   
                                   
    else: # Hints to help the player guess the prime number
        if (int(num) - 1) % guess_count == 0:
            print("The number before the prime is divisible by", guess_count)
        elif (int(num) + 1) % guess_count == 0:
            print("The number after the prime is divisible by", guess_count)
        else:
            print("The numbers before and after the prime are not divisible by", guess_count)
   
    guess = input("Try to guess the 2-digit number or type a string to exit: ")
    
    guess_count += 1

if guess == num:
    print("You guessed it right! It took you", guess_count - 1, "guesses.") 

  
