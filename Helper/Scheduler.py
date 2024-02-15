from Classes.Types import SchedulingMethod
class Scheduler():
    optimal_path = []
    scheduler = None
    time = None
    def get_scheduler(self,func):
        self.scheduler = func
    
    def get_optimal_path(self,orders,rider):
        if self.scheduler is None:
            raise Exception("No scheduler available")
            exit()
        self.optimal_path,self.time = self.scheduler(orders,rider)
    
    def display_path(self):
        print("================================================================================================")
        print("Minimum cost :", self.time)  
        print("Path Taken : ")
        s = "START-> "
        if self.optimal_path:
            j=0
            for i in self.optimal_path:
                if j//2==0:
                    s+=" "+str(i)+"  "
                else:
                    s+=" ("+str(i)+") ->   "
                j=j+1
        print(s+"->DONE")
        # return path
        