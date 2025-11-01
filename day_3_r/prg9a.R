fib_iterative <- function(n) {
  if (n <= 0) {
    return((0))  # Empty vector for non-positive n
  }
  if (n == 1) {
    return(c(0))
  }
  
  fib <- numeric(n)
  fib[1] <- 0
  fib[2] <- 1
  
  for (i in 3:n) {
    fib[i] <- fib[i-1] + fib[i-2]
  }
  return(fib)
}

n <- as.integer(readline("Enter n: "))
result <- fib_iterative(n)
print(result)
