# (b) Recursive GCD function
gcd_rec <- function(a, b) {
  if (b == 0) {
    return(a)
  } else {
    return(gcd_rec(b, a %% b))
  }
}

a <- as.integer(readline("Enter first number: "))
b <- as.integer(readline("Enter second number: "))

cat("Recursive GCD of", a, "and", b, ":", gcd_rec(a, b), "\n")
