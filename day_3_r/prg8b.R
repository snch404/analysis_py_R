factorial_rec <- function(n) {
  if (n == 0 || n == 1) {
    return(1)
  } else {
    return(n * factorial_rec(n - 1))
  }
}

# Take input from user
num <- as.integer(readline("Enter a number: "))
cat("Factorial (recursion) =", factorial_rec(num), "\n")
