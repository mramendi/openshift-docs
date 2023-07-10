import os.path

errlines=open("out").readlines()
actions=open("actions.sh","w")

for line in errlines:
    if line.find("not found")==-1:
        continue

    # find the file name
    (head,fname)=os.path.split(line.split()[-1])

    # record the directory, which should be modules/snippets/images
    (head,fdir)=os.path.split(head)


    fpathname=os.path.join(fdir,fname)
    action="cp /home/mramendi/repos/openshift-docs/"+fpathname+" "+fdir+"\n"
    actions.write(action)

actions.close()


    # find the file directory from the right level



#    fdir=""
#    fdir_added=""
#    while not fdir_added in ["modules","snippets","images","_attributes"]:
#        if head=="": # this should never happen...
#            print("Expected directory name not found for line: ")
#            print(line)
#            exit(1)
#        (head,fdir_added)=os.path.split(head)
#        fdir=os.path.join(fdir_added,fdir)
