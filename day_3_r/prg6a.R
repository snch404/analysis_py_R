# (a) Iterative GCD function
gcd_iter <- function(a, b) {
  while (b != 0) {
    temp <- b
    b <- a %% b
    a <- temp
  }
  return(a)
}

# Take input from user
a <- as.integer(readline("Enter first number: "))
b <- as.integer(readline("Enter second number: "))

cat("Iterative GCD of", a, "and", b, ":", gcd_iter(a, b), "\n")