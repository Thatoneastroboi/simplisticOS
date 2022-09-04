import tkinter

print("choose what process/domain you want to see: ")
domainRead = input()
processRead = input()
def scheduler(domainRead, processRead):
    domains = ["testdomain","testdomain1","testdomain2","testdomain3"]
    currentProcesses = ["testProcess1","testProcess2","testprocess3"]
    print(domains[int(domainRead)] + " " + currentProcesses[int(processRead)])
    return 0 
    
scheduler(domainRead, processRead)