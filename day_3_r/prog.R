# Create the Employees data frame
Employees <- data.frame(
  Age    = c(23, 21, 34, 44, 32),
  Height = c(76, 62, 63, 69, 72),
  Weight = c(50, 52, 80, 65, 70),
  Gender = c("Female", "Female", "Male", "Male", "Female")
)

# (i) Extract and display only the Weight column
print("Weight column:")
print(Employees$Weight)

# (ii) Convert Gender into factors and then into numeric values
Employees$Gender <- as.factor(Employees$Gender)
print("Gender as factors:")
print(Employees$Gender)
print("Gender as numeric values:")
print(as.numeric(Employees$Gender))

# (iii) Obtain unique values of Age
print("Unique Age values:")
print(unique(Employees$Age))

# (iv) Obtain sorted unique values of Age
print("Sorted unique Age values:")
print(sort(unique(Employees$Age)))

# (v) Delete the Height column
Employees$Height <- NULL
print("Data frame after deleting Height column:")
print(Employees)
