fib <- function(k) {
  if (k == 1) return(0)
  if (k == 2) return(1)
  return(fib(k - 1) + fib(k - 2))
}

n <- as.integer(readline("Enter n: "))

for (i in 1:n) {
  cat(fib(i), " ")
}
