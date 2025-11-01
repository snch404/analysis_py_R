# Recursive GCD function
gcd <- function(a, b) {
  if (b == 0) {
    return(a)
  }
  return(gcd(b, a %% b))
}

# Input list
l <- c()
n <- as.integer(readline("Enter number of elements: "))
for (i in 1:n) {
  num <- as.integer(readline(paste("Enter element", i, ": ")))
  l <- c(l, num)
}

# Function to find GCD of the list
gcd_num <- function(l) {
  n_val <- gcd(l[1], l[2])
  if (length(l) > 2) {
    for (i in 2:length(l)) {
      n_val <- gcd(n_val, l[i])
    }
  }
  return(n_val)
}

cat("GCD of the list is:", gcd_num(l), "\n")
