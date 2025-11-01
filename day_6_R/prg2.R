# -----------------------------
# Part (a) Accept input & create DataFrame
# -----------------------------
cat("Enter number of students: ")
n <- as.integer(readline())

ID <- 1:n
Name <- character(n)
Sub1 <- numeric(n)
Sub2 <- numeric(n)
Sub3 <- numeric(n)

for (i in 1:n) {
  cat("\nEnter name of student", i, ": ")
  Name[i] <- readline()
  
  cat("Enter marks in Sub1: ")
  Sub1[i] <- as.numeric(readline())
  
  cat("Enter marks in Sub2: ")
  Sub2[i] <- as.numeric(readline())
  
  cat("Enter marks in Sub3: ")
  Sub3[i] <- as.numeric(readline())
}

df <- data.frame(ID, Name, Sub1, Sub2, Sub3)
cat("\nOriginal Data Frame:\n")
print(df)

# -----------------------------
# Part (b) Add Total and Average
# -----------------------------
df$Total <- df$Sub1 + df$Sub2 + df$Sub3
df$Average <- df$Total / 3

cat("\nData Frame with Total and Average:\n")
print(df)

# -----------------------------
# Part (c) Add Grade column
# -----------------------------
df$Grade <- with(df, ifelse(Average >= 90, "O",
                            ifelse(Average >= 80, "A",
                                   ifelse(Average >= 70, "B",
                                          ifelse(Average >= 60, "C",
                                                 ifelse(Average >= 50, "D", "F"))))))

cat("\nData Frame with Grades:\n")
print(df)

# -----------------------------
# Part (d) Sort by Grade (Topper first)
# -----------------------------
grade_order <- c("O", "A", "B", "C", "D", "F")
df$Grade <- factor(df$Grade, levels = grade_order, ordered = TRUE)

# Sort first by Grade, then by Average descending
df_sorted <- df[order(df$Grade, -df$Average), ]

cat("\nFinal Data Frame Sorted by Grade & Average:\n")
print(df_sorted)
