from AgentSupport import MotorModule, CleanSensorModule, MyCell
import AgentSupport
import python_actr
from python_actr.lib import grid
import random

class VacuumAgent(python_actr.ACTR):
	goal = python_actr.Buffer()
	body = grid.Body()
	motorInst = MotorModule()
	cleanSensor = CleanSensorModule()

	def init():
		goal.set("rsearch left 0 0 0")
		self.home = None

	#----ROOMBA----#

	def clean_cell(cleanSensor="dirty:True", utility=0.6):
		motorInst.clean()

        #This function handles all forward direction
	def forward_rsearch(goal="rsearch left ?dist ?num_turns ?curr_dist", motorInst="busy:False", body="ahead_cell.wall:False"):
		motorInst.go_forward()
		print(body.ahead_cell.wall)
		dist = str(int(dist) + 1)
		curr_dist = str(int(curr_dist) + 1)
		goal.set("rsearch left ?dist ?num_turns ?curr_dist")

        #Methods to handle agent's turning behavior. The agent spirals inwards, starting from the green square.
        #These methods help the agent decide when to turn based on its current position and how many turns it has made.
        #Each method corresponds to a specific turning point in the agent's path.
        
        #Below are the turn methods for the agent. Each method represents a specific turning point based on the current distance traveled and number of turns made.
        #After making a turn, the distances are reset and the number of turns is incremented.
        #This ensures the agent follows a spiral path.
	def turn0_rsearch(goal="rsearch left 7 0 7", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 1 0")
		
	def turn1_rsearch(goal="rsearch left 6 1 6", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 2 0")

	def turn2_rsearch(goal="rsearch left 7 2 7", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 3 0")
                                  
	def turn3_rsearch(goal="rsearch left 5 3 5", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 4 0")

	def turn4_rsearch(goal="rsearch left 6 4 6", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 5 0")

	def turn5_rsearch(goal="rsearch left 4 5 4", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 6 0")

	def turn6_rsearch(goal="rsearch left 5 6 5", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 7 0")
		
	def turn7_rsearch(goal="rsearch left 3 7 3", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 8 0")

	def turn8_rsearch(goal="rsearch left 4 8 4", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 9 0")

	def turn9_rsearch(goal="rsearch left 2 9 2", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 10 0")

        #The agent will not reach this step because all of the dirty spots will be gone, but in case different dirty spots are added this code ensures all squares are hit on the grid.
	def turn10_rsearch(goal="rsearch left 3 10 3", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 11 0")

	def turn11_rsearch(goal="rsearch left 1 11 1", motorInst="busy:False", utility=0.1):
		motorInst.turn_left(2)
		curr_dist = 0
		goal.set("rsearch left 0 12 0")

world=grid.World(MyCell,map=AgentSupport.mymap)
agent=VacuumAgent()
agent.home=()
world.add(agent,8,1,dir=6,color="black")

python_actr.log_everything(agent, AgentSupport.my_log)
python_actr.display(world)
world.run()
