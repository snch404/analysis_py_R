gcd<-function(a,b){
  if(b==0) {
    return(a)
  }
  else {
    return(gcd(b,a%%b))
  }
}
l<-c()
n<-as.integer(readline("Enter the no. of elements:"))
for(i in 1:n){
  num<-as.integer(readline("Enter element:"))
  l<-c(l,num)
}

gcd_num<-function(l){
  v=gcd(l[1],l[2])
  for(i in 3:length(l)){
    v=gcd(v,l[i])
  }
  return(v)
}
cat("GCD of list is:",gcd_num(l))