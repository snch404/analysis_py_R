factorial_iter <- function(n) {
  result <- 1
  for (i in 1:n) {
    result <- result * i
  }
  return(result)
}

# Take input from user
num <- as.integer(readline("Enter a number: "))
cat("Factorial (iteration) =", factorial_iter(num), "\n")
