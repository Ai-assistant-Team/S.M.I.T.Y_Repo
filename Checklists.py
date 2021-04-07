
def checklists():
    checklist = []
    task = ""
    x = 0
    while(task != "end"):
        task = input("Enter the task: ")
        checklist.append(task)
        x=x+1 #Counting the tasks
        if task == "end":
            checklist.remove(task) #Removes the tasks 'end' from the list
            x=x-1
    print("Tasks: ", checklist)

    ans = input("did you finish any tasks? yes/no")
    while(ans == "yes" and x!=0):
        task = ""
        while (task != "end"):
            task = input("What tasks did you accomplish?")
            if task != "end":
                checklist.remove(task)
                x=x-1
        print("Tasks remaining: ", checklist)
        ans = input("did you finish any tasks? yes/no")

checklists()
