print("\nwelcome to the show 'WHO WILL BE A MILLIONAIRE' ")
name=input("\nEnter ur name to Participate : ").upper()
print(f"\nHELLO {name}..!")
print(f"Let's start the show..!\nHere ur Questions...\n")

questions=[
    {
      "question":"1. Which of the following material is used to made pencil..?",
      "options":[f"(a) Graphite\n(b) Silicon\n(c) Charcoal\n(d) Phosphorus"],
      "answer":"a",
      "wrong":["c","b","d"],
      "score":1000
    },
    {
      "question":"2. What is unit of current..?",
      "options":[f"(a) Ohm\n(b) Watt\n(c) Ampere\n(d) None of the above"],
      "answer":"c",
      "wrong":["a","b","d"],
      "score":5000
    },
    {
      "question":"3. Which is the Biggest Flower in the world..?",
      "options":[f"(a) sunflower\n(b) Jade wine\n(c) Rafflesia\n(d) cactus"],
      "answer":"c",
      "wrong":["a","b","d"],
      "score":10000
    },
    {
      "question":"4. What is the Natural Satelite of Earth..?",
      "options":[f"(a) Sun\n(b) Moon\n(c) Mars\n(d) Jupiter"],
      "answer":"b",
      "wrong":["a","c","d"],
      "score":20000
    },
    {
      "question":"5. Where is the Walt Disney World is Located..?",
      "options":[f"(a) Florida,US\n(b) Paris,France\n(c) Colombia,South America\n(d) China,Asia"],
      "answer":"a",
      "wrong":["b","c","d"],
      "score":50000
    },
    {
      "question":"6. Jimmy's father has 3 sons - Paul I and Paul II.\nCan u Guess the name of the Third Person..?",
      "options":[f"(a) Paul III\n(b) Jerin\n(c) Jimmy\n(d) None"],
      "answer":"c",
      "wrong":["a","b","d"],
      "score":100000
    },
    {
      "question":"7. What is the Largest Forest in the World..?",
      "options":[f"(a) Siberian Taiga, Russia\n(b) Atlantic Forest, Atlantic\n(c) Amazon, South America\n(d) Daintree Rainforest, Australia"],
      "answer":"c",
      "wrong":["a","d","b"],
      "score":2000000
    },
    {
      "question":"8. Which planet is known as RED PLANET..?",
      "options":[f"(a) Neptune\n(b) Mars\n(c) Jupiter\n(d) Earth"],
      "answer":"b",
      "wrong":["a","c","d"],
      "score":3000000
    },
    {
      "question":"9. What is the Longest River in India..?",
      "options":[f"(a) Ganga\n(b) Indus\n(c) Godhavari\n(d) Brahmaputra"],
      "answer":"b",
      "wrong":["a","c","d"],
      "score":5000000
    },
    {
      "question":"10. Who is the author of book 'ROMEO AND JULIET'..?",
      "options":[f"(a) Rabindranath Tagore\n(b) Percy Bysshe Shelly\n(c) Francis Bacon\n(d) William Shakespeare"],
      "answer":"d",
      "wrong":["a","c","b"],
      "score":10000000
    }
]

cash=0 # starting with empty hands

# i am selecting the first dict from list
for question in questions: 
    # i am calling the key(question) from selected dict
    print(question["question"])

    # now i am getting the options one by one using loop
    for option in question["options"]:
        print(option)
        print("\nIf u want to quit the show.. then type 'quit'... ")

        # getting a input from user and converting into lower
    user_answer=input(f"\nEnter your answer[a,b,c or d]: ").lower()

# user input is in key(answer)
    if user_answer==question["answer"]:
        print(f"\nCorrect Answer... {name}...! :)")
        cash=question["score"]
        print(f"u won the amount..\nNow u have the amount Rs.{cash}")
        if question in questions[-2::-1]: print(f"\nlets move on to the further questions..\n")

# if the user input is not in the key(answer) then it go to check in key(wrong)
    elif user_answer in question["wrong"]:
        print(f"\nIncorrect Answer...!")
        break # to stop the loop whenever the userinput in wrong

# if user input is equal to "quit" then also stop
    elif user_answer == "quit":
        print(f"\nu r quit from this show\n")
        break
    
# or else if user gives any other output then also stop the loop
    else:
        print(f"\nInvalid Input...!")
        break

# if user got entire amout then...
if cash==10000000: print(f"\nHurry...! U got the JACKPOT.. :)")

# if user lost at first question then...
if cash==0: print("You Lost..  : (")

# if use have any amout then....
else:print(f"u recieved the reward of Rs.{cash}....!")
print("Thank You.... for being a part in Game...!")