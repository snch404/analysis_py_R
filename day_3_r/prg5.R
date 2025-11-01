a <- as.numeric(readline("Enter coefficient a: "))
b <- as.numeric(readline("Enter coefficient b: "))
c <- as.numeric(readline("Enter coefficient c: "))

D <- b**2 - 4*a*c

if (D > 0) {
  root1 <- (-b + sqrt(D)) / (2*a)
  root2 <- (-b - sqrt(D)) / (2*a)
  cat("Roots are real and unequal:\n")
  cat("Root 1 =", root1, "\n")
  cat("Root 2 =", root2, "\n")
  
} else if (D == 0) {
  root <- -b / (2*a)
  cat("Roots are real and equal:\n")
  cat("Root =", root, "\n")
  
} else {
  realPart <- -b / (2*a)
  imagPart <- sqrt(-D) / (2*a)
  cat("Roots are complex conjugates:\n")
  cat("Root 1 =", realPart, "+", imagPart, "i\n")
  cat("Root 2 =", realPart, "-", imagPart, "i\n")
}