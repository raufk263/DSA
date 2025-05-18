# A simple dictionary with integer keys
demo = {1: "one", 2: "two", 3: "three", 4: "four"}

print(demo[1])          # Access value for key 1 → Output: 'one'
print(len(demo))        # Number of key-value pairs → Output: 4

# Another dictionary with continent-country mapping
demo_countries = {
    "Asia": "India",
    "North America": "USA",
    "South America": "Peru",
    "Europe": "Finland"
}

print(demo_countries)               # Prints the full dictionary
print(demo_countries["Asia"])      # Access value for key 'Asia' → Output: 'India'
print(len(demo_countries))         # Number of key-value pairs → Output: 4
print(type(demo_countries))        # Output: <class 'dict'>


demo_countries["Africa"] = "Nigeria" # Add a New Key-Value Pair
print(demo_countries)

demo_countries["Asia"] = "Nepal"  # Update an Existing Value
print(demo_countries["Asia"])

del demo_countries["Europe"]   # Delete existing value
print(demo_countries)
print("\n")
print(demo_countries.keys()) # Returns all keys in dictionary.

print(demo_countries.values()) # Returns all valuess in dictionary.

# To check if key exists or not
if "Australia" in demo_countries:
    print("Exist")
else:
    print("Does not exist")
