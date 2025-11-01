age<-as.integer(readline("Enter age of person: "))
if(age<18){
  cat("Not eligible, years left to be eligible: ",18-age)
} else{
  print("Eligible to vote")
}