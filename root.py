from numpy import *
from tkinter import *

f=open("input.txt","r")

vertexCount=1;i=0;start=1;end1=1;end2=1;predicates=0;

vertices=[1]

edges=zeros((20,20),int)

lines=[]

for var in f:
    lines.append(var)
while(i<len(lines)):
    if(lines[i].find('if')!=-1):
        vertexCount+=1
        vertices.append(vertexCount)
        start=vertexCount
        edges[vertexCount-1][vertexCount]=1
        vertexCount+=1
        vertices.append(vertexCount)
        edges[vertexCount-1][vertexCount]=1; end1=vertexCount;
        while(lines[i].find('}')==-1):
            i+=1
        i+=1
        if(lines[i].find('else')!=-1):
            vertexCount+=1
            vertices.append(vertexCount)
            end2=vertexCount
            edges[start][end2]=1
            vertexCount += 1
            vertices.append(vertexCount)
            edges[end1][vertexCount]=1
            edges[end2][vertexCount]=1
            while(lines[i].find('}')==-1):
                i+=1
            i+=1
        else:
            vertexCount += 1
            vertices.append(vertexCount)
            edges[end1][vertexCount]=1


    elif(lines[i].find('for')!=-1):
        vertexCount += 1
        vertices.append(vertexCount)
        edges[vertexCount-1][vertexCount]=1
        vertexCount += 1
        vertices.append(vertexCount)
        edges[vertexCount - 1][vertexCount] = 1
        edges[vertexCount-2][vertexCount] = 1
        while(lines[i].find('}')==-1):
            i+=1
        i+=1

    elif(lines[i].find('while')!=-1):
        vertexCount += 1
        vertices.append(vertexCount)
        edges[vertexCount - 1][vertexCount] = 1
        vertexCount += 1
        vertices.append(vertexCount)
        edges[vertexCount - 1][vertexCount] = 1
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




