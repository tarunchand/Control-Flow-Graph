from numpy import *
from tkinter import *


def CFG():
    f=open("input.txt","r")

    vertexCount=1;i=0;start=1;end1=1;end2=1;predicates=0;

    vertices=[1]

    edgess=[]

    edges=zeros((15,15),int)

    lines=[]

    for var in f:
        lines.append(var)
    while(i<len(lines)):
        if(lines[i].find('if')!=-1):
            vertexCount+=1
            vertices.append(vertexCount)
            start=vertexCount
            edges[vertexCount-1][vertexCount]=1
            edgess.append(str(vertexCount-1)+"-->"+str(vertexCount))
            vertexCount+=1
            vertices.append(vertexCount)
            edges[vertexCount-1][vertexCount]=1; end1=vertexCount;
            edgess.append(str(vertexCount-1)+"-->"+str(vertexCount))
            while(lines[i].find('}')==-1):
                i+=1
            i+=1
            if(lines[i].find('else')!=-1):
                vertexCount+=1
                vertices.append(vertexCount)
                end2=vertexCount
                edges[start][end2]=1
                edgess.append(str(start) + "-->" + str(end2))
                vertexCount += 1
                vertices.append(vertexCount)
                edges[end1][vertexCount]=1
                edgess.append(str(end1) + "-->" + str(vertexCount))
                edges[end2][vertexCount]=1
                edgess.append(str(end2) + "-->" + str(vertexCount))
                while(lines[i].find('}')==-1):
                    i+=1
                i+=1
            else:
                vertexCount += 1
                vertices.append(vertexCount)
                edges[end1][vertexCount]=1
                edgess.append(str(end1) + "-->" + str(vertexCount))

        elif(lines[i].find('for')!=-1):
            vertexCount += 1
            vertices.append(vertexCount)
            edges[vertexCount-1][vertexCount]=1
            edgess.append(str(vertexCount-1)+"-->"+str(vertexCount))
            vertexCount += 1
            vertices.append(vertexCount)
            edges[vertexCount - 1][vertexCount] = 1
            edgess.append(str(vertexCount-1)+"-->"+str(vertexCount))
            edges[vertexCount-2][vertexCount] = 1
            edgess.append(str(vertexCount-2)+"-->"+str(vertexCount))
            while(lines[i].find('}')==-1):
                i+=1
            i+=1

        elif(lines[i].find('while')!=-1):
            vertexCount += 1
            vertices.append(vertexCount)
            edges[vertexCount - 1][vertexCount] = 1
            edgess.append(str(vertexCount-1)+"-->"+str(vertexCount))
            vertexCount += 1
            vertices.append(vertexCount)
            edges[vertexCount - 1][vertexCount] = 1
            edgess.append(str(vertexCount-1)+"-->"+str(vertexCount))
            edges[vertexCount - 2][vertexCount] = 1
            edgess.append(str(vertexCount-2)+"-->"+str(vertexCount))
            while (lines[i].find('}') == -1):
                i += 1
            i += 1

        else:
            i+=1

    print("nodes are ",end='')
    print(vertices)

    print("\nEdges are :- ")
    print(edges)

    f.close()

    g=open("input.txt","r")

    for vars in g:
        if(vars.find('if')!=-1 or vars.find('for')!=-1 or vars.find('while')!=-1):
            predicates+=1

    print("No. of Predicates is " + str(predicates))

    print("No. of Bounded Regions is " + str(predicates))

    print("No. of Independent Paths is " + str(predicates + 1))

    g.close()

    return vertexCount,predicates,vertices,edges,edgess

def Return(frame):
    frame.destroy()
    main()

def Giveninput(frame):
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    f = open("input.txt", "r")
    label = Label(frame, text=f.read(),font='Verdana 10 bold')
    label.grid()
    f.close()
    ret=Button(frame,text='Return',height=5,width=30,font='Verdana 12 bold',command=lambda: Return(frame))
    ret.grid()

def nodes(frame):
    values=CFG()
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    s="Total no. of Vertices are " + str(values[0])
    label = Label(frame,text=s,font='Verdana 30 bold')
    label.grid()
    label = Label(frame, text="They are :- ", font='Verdana 30 bold')
    label.grid()
    label = Label(frame, text=str(values[2]), font='Verdana 30 bold')
    label.grid()
    ret = Button(frame, text='Return', height=5, width=30, font='Verdana 12 bold', command=lambda: Return(frame))
    ret.grid()

def edges(frame):
    values = CFG()
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    s = "Edges represented as adjacency matrix is "
    label = Label(frame, text=s, font='Verdana 30 bold')
    label.grid()
    label = Label(frame, text=str(values[3]), font='Verdana 30 bold')
    label.grid()
    ret = Button(frame, text='Return', height=5, width=30, font='Verdana 12 bold', command=lambda: Return(frame))
    ret.grid()

def edgess(frame):
    values = CFG()
    r=1;c=0;
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    s = "Edges of the Control Flow Graph are "
    label = Label(frame, text=s, font='Verdana 30 bold')
    label.grid()
    for i in values[4]:
        label = Label(frame, text=i, font='Verdana 30 bold')
        label.grid(row=r,column=c)
        c+=1
        if(c>3):
            r+=1
            c=0

    ret = Button(frame, text='Return', height=5, width=30, font='Verdana 12 bold', command=lambda: Return(frame))
    ret.grid()

def predicateNodes(frame):
    values = CFG()
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    s = "Total no. of Predicate Nodes are " + str(values[1])
    label = Label(frame, text=s, font='Verdana 30 bold')
    label.grid()
    ret = Button(frame, text='Return', height=5, width=30, font='Verdana 12 bold', command=lambda: Return(frame))
    ret.grid()

def boundedregions(frame):
    values = CFG()
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    s = "Total no. of Bounded Regions are " + str(values[1])
    label = Label(frame, text=s, font='Verdana 30 bold')
    label.grid()
    ret = Button(frame, text='Return', height=5, width=30, font='Verdana 12 bold', command=lambda: Return(frame))
    ret.grid()

def idpaths(frame):
    values = CFG()
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    s = "Total no. of independent paths are " + str(values[1]+1)
    label = Label(frame, text=s, font='Verdana 30 bold')
    label.grid()
    ret = Button(frame, text='Return', height=5, width=30, font='Verdana 12 bold', command=lambda: Return(frame))
    ret.grid()

def gr(frame):
    frame.destroy()
    frame=Frame(root)
    frame.pack(fill=X)


def main():


    frame=Frame(root)

    frame.pack(fill=X)

    label=Label(frame,text='CONTROL FLOW GRAPH',fg='red',bg='light green',font='Verdana 20 bold')

    label.pack(side='top',fill=X)

    inputtext=Label(frame,text='Enter your input in the file input.txt located in this directory',fg='blue',font='Helvetica 12 bold italic')

    inputtext.pack()

    givenInput=Button(frame,text='Given Input',height=5,width=30,font='Verdana 12 bold',command=lambda: Giveninput(frame))

    givenInput.pack(side='top')

    Nodes=Button(frame,text='Nodes',height=5,width=30,font='Verdana 12 bold',command=lambda: nodes(frame))

    Nodes.pack(side='top')

    Edges=Button(frame,text='Edges',height=5,width=30,font='Verdana 12 bold',command=lambda: edgess(frame))

    Edges.pack(side='top')

    PredicateNodes=Button(frame,text='Predicate Nodes',height=4,width=30,font='Verdana 12 bold',command=lambda: predicateNodes(frame))

    PredicateNodes.pack(side='top')

    BoundedRegions=Button(frame,text='BoundedRegions',height=4,width=30,font='Verdana 12 bold',command=lambda: boundedregions(frame))

    BoundedRegions.pack(side='top')

    IndependentPaths=Button(frame,text='Independent Paths',height=4,width=30,font='Verdana 12 bold',command=lambda: idpaths(frame))

    IndependentPaths.pack(side='top')

    Refresh=Button(frame,text='Adjacency Matrix',height=5,width=30,font='Verdana 12 bold',command=lambda: edges(frame))

    Refresh.pack(side='top')

    GR=Button(frame,text='Graphical Representation',height=5,width=30,font='Verdana 12 bold',command=lambda:gr(frame))

    GR.pack(side='top')

root = Tk()

root.title('Control Flow Graph')

main()

root.mainloop()
