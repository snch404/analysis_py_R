# -----------------------------
# Load Data
# -----------------------------
df <- read.csv("E:\\python\\python_colg_r\\day_6_R\\marks_student2.csv", stringsAsFactors = FALSE)

# -----------------------------
# (a) Number of columns, column names, and number of students
# -----------------------------
cat("Number of columns:", ncol(df), "\n")
cat("Column names:", colnames(df), "\n")
cat("Number of students:", nrow(df), "\n\n")

# -----------------------------
# (b) Count male and female students
# -----------------------------
cat("Number of male students:", sum(df$Gender == "Male", na.rm = TRUE), "\n")
cat("Number of female students:", sum(df$Gender == "Female", na.rm = TRUE), "\n\n")

# -----------------------------
# (c) Replace 'A' with 0 in marks columns
# -----------------------------
marks_cols <- grep("Test", names(df))  # assuming test columns start with "Test"
for (col in marks_cols) {
  df[[col]][df[[col]] == "A"] <- 0
  df[[col]] <- as.numeric(df[[col]])  # convert to numeric
}

# -----------------------------
# (d) Students scoring more than 20 in total (ignoring NA)
# -----------------------------
df$Total <- rowSums(df[marks_cols], na.rm = TRUE)
cat("Number of students with Total > 20:", sum(df$Total > 20, na.rm = TRUE), "\n\n")

# -----------------------------
# (e) Percentage of students > 60% (i.e., > 15 out of 25)
# -----------------------------
threshold <- 0.6 * 25  # 15 marks
above_60 <- sum(df$Total > threshold, na.rm = TRUE)
percentage <- (above_60 / nrow(df)) * 100

cat("Percentage of students scoring > 60%:", percentage, "%\n")
