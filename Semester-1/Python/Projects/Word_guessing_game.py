name=input("what is your name?: ")
word=[
    "python", "jumble", "bright", "quick", "flame",
    "spark", "stone", "craft", "whisk", "brink",
    "ghost", "plumb", "drift", "fancy", "shout",
    "brick", "flock", "track", "glove", "swift",
    "grove", "thump", "plank", "crate", "frisk",
    "gamer", "poker", "blunt", "spank", "drove",
    "prick", "jumpy", "thick", "shave", "flare",
    "crown", "plain", "spoke", "grind", "vocal",
    "burst", "clang", "pivot", "frame", "skull",
    "brave", "flint", "stone", "glint", "cloak",
    "trick", "gleam", "shade", "crisp", "whale",
    "snarl", "point", "glare", "skate", "crave",
    "whisk", "pluck", "vapor", "shade", "blare",
    "shrink", "fable", "grace", "blame", "chore",
    "stand", "wharf", "track", "shove", "vault",
    "grasp", "crown", "pride", "froze", "spend",
    "climb", "chart", "grape", "chalk", "swoop",
    "throne", "block", "trend", "cable", "spark",
    "flame", "drape", "shout", "joust", "bride"
]
import random
wl=random.choice(word)
#print("this game is super hard, and i mean it")
print("Good Luck!",name)
print("*hint: \n"
    "try letter which are common like 'a','e','i','o','u')********")
def hint(hints):
    print(' '.join(hints))
count=0
hints=["-"]*len(wl)
while True:
    print("*********************")
    hint(hints)
    print("*********************")
    guess=input("try to guess the word :")
                
    if guess in wl:
        for i in range(len(wl)):
            if wl[i]==guess:
                hints[i]=guess
    if guess==wl:
          print("congrats",name,"you took",count,"counts")
          break
    elif guess not in wl:
        print("             \n"
             " nahh try again\n"
             "                ")
    count+=1
