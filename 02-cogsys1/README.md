# Ian McMullen
## _Cognitive Systems Assignment 1, Pizza Maker and Roombas_
## The Pizza Maker Agent
This pizza maker will randomly select between two pizza options. The two options are a pizza with sauce, mozzarella cheese, and pepperoni or a pizza with bbq sauce, cheddar cheese, and onions. Originally the agent did not make a bbq pizza, but after modifying the code it will now create both types. I was not sure if a new topping needed created for the bbq pizza so I decided to just choose onions as the only possible topping for a bbq cheddar pizza. It also seemed like a better choice than pepperoni for a bbq sauce pizza.

## The (Brute Force) Roomba Agent
The agent  may not function as intended. The agent begins on the green square and slowly works its way inward in a spiral pattern until it reaches the center, or until all the dirt is gone. By ensuring it reaches the center, all dirt will always be picked up if it starts on the green square. I was not able to get the agent to detect if a wall was present so a brute force approach was taken. By calculating the size of the room, I was able to determine at which point the agent needed to turn and created the functions accordingly. In the following sequence, after each number the agent turns ninety degrees to the left, with twelve turns in total: 7, 6, 7, 5, 5, 4, 5, 3, 4, 2, 3, 1, 2
### How To Run The Models

1. Set up your virtual Python environment
2. Install the Python ACT-R library
3. Pip Install AgentSupport
4. In your VEnv type "python filename_here" and press enter!




