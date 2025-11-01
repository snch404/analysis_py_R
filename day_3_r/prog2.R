# Create data frame
Information <- data.frame(
  ID = c(10, 11, 12, 13),
  Name = c("Sai", "Ram", "Deepika", "Dipesh"),
  DOB = as.Date(c("1990-10-02", "1981-03-24", "1987-06-14", "1985-08-16"))
)

# Check data types of each column
str(Information)

# Print data frame with row numbers
print(Information, row.names = 1:nrow(Information))
