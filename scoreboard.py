from turtle import Turtle
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("data.txt","r") as fobj:
            self.high_score=int(fobj.read())
        
        self.score=0
        
        self.color("white")
        self.penup()
        self.goto(0,270)
        
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score}  high score:{self.high_score}",align="center",font=("ariel",24,"normal"))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        self.score=0
        self.update_scoreboard()
        fobj=open("data.txt","w")
        f1=fobj.write(f"{self.high_score}")
        fobj.close()
        
        


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center",font=("ariel",30,"normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()



