# Function to take user input and create a vector of given type and length
create_vector <- function(type, length) {
  vec <- vector(type, length)   # empty vector
  for (i in 1:length) {
    value <- readline(prompt = paste("Enter", type, "element", i, ": "))
    
    # Convert input based on type
    if (type == "numeric") {
      vec[i] <- as.numeric(value)
    } else if (type == "complex") {
      vec[i] <- as.complex(value)
    } else if (type == "logical") {
      vec[i] <- as.logical(value)
    } else if (type == "character") {
      vec[i] <- value
    }
  }
  return(vec)
}

# Take input for length (same for all types)
length_input <- as.integer(readline(prompt = "Enter length of vectors: "))

# Create all types of vectors
numeric_vector   <- create_vector("numeric", length_input)
complex_vector   <- create_vector("complex", length_input)
logical_vector   <- create_vector("logical", length_input)
character_vector <- create_vector("character", length_input)

# Print results
cat("\nNumeric vector:\n")
print(numeric_vector)

cat("\nComplex vector:\n")
print(complex_vector)

cat("\nLogical vector:\n")
print(logical_vector)

cat("\nCharacter vector:\n")
print(character_vector)
