x1<-as.integer(readline("Enter x coordinate 1: "))
y1<-as.integer(readline("Enter y coordinate 1: "))
x2<-as.integer(readline("Enter x coordinate 2: "))
y2<-as.integer(readline("Enter y coordinate 2: "))
d<-((x1-x2)**2+(y1-y2)**2)**0.5
cat("Distance is: ",d)