# Introduce missing values
df$Sub2[df$Name == "BBB"] <- NA
df$Sub3[df$Name == "DDD"] <- NA
df$Sub1[df$Name == "EEE"] <- NA

# Select only subject columns
subjects <- df[, c("Sub1", "Sub2", "Sub3")]

# Compute statistics with NA ignored
stats_na <- data.frame(
  Subject  = colnames(subjects),
  Mean     = sapply(subjects, mean, na.rm = TRUE),
  Median   = sapply(subjects, median, na.rm = TRUE),
  SD       = sapply(subjects, sd, na.rm = TRUE),
  Variance = sapply(subjects, var, na.rm = TRUE)
)

print("Statistics Table (ignoring missing values):")
print(stats_na)
