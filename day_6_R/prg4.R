# Compute mean, median, sd, variance for Sub1, Sub2, Sub3
stats <- data.frame(
  Subject   = c("Sub1", "Sub2", "Sub3"),
  Mean      = c(mean(df$Sub1), mean(df$Sub2), mean(df$Sub3)),
  Median    = c(median(df$Sub1), median(df$Sub2), median(df$Sub3)),
  SD        = c(sd(df$Sub1), sd(df$Sub2), sd(df$Sub3)),
  Variance  = c(var(df$Sub1), var(df$Sub2), var(df$Sub3))
)

# Display in tabular format 
print("Statistics Table:")
print(stats)
