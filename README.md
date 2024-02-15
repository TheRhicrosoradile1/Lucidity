### Design patterns used
We have applied BUILDER pattern to create user ,resturant ,rider  a,customer and order object 
all classes are created with extensiblity and oops in mind
Due to time constraint we haven't implemented complete classes but only which were essential

we have implemented STRATEGY to select the optimal path algorithm 


### Algorithm
for path finding we developed an hueristic greedy algorithm 
we assumed the preparation time to be zero as mention and also that order never get stale 
due to that we can assumable pich all order from a resturant at once
in addition to that as in the begining we can only reach out to a resturant the first hueristic is the first mile distance 
once we have orders we have a choice to make between delivering current order or picking more which will be the basis of our second heuristic algorithm
at the end of each round we pick the one with the min time needed
finally when all are done we print the optimal path

### steps to run 

go to main.py and as given create resturants ,orders and customer object
run the main.py file
