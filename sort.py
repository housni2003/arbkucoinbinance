import json

def count_json_objects(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        count = len(data)
    print("Number of pairs:", count)
    return count

# def read_and_sort_json(filename):
#     # Read JSON data from file
#     with open(filename, 'r') as file:
#         # Read the entire file content
#         content = file.read()
        
#         # Remove the trailing comma if it exists
#         content = content.strip()
#         if content.endswith(','):
#             content = content[:-1]
        
#         # Load JSON data from corrected content
#         data = json.loads(content)
    
#     # Print the number of JSON objects
#     print(f"Number of JSON objects: {len(data)}")

#     # Sort data based on 'max_profit' in descending order
#     sorted_data = sorted(data, key=lambda x: x['max_profit'], reverse=True)

#     # Print sorted data
#     print("Sorted data:")
#     for entry in sorted_data:
#         print(entry)

#     return sorted_data

def remove_trailing_comma(input_filename, output_filename):
    # Read the entire content of the input file
    with open(input_filename, 'r') as file:
        content = file.read()
        
        # Remove the trailing comma if it exists
        content = content.strip()
        if content.endswith(','):
            content = content[:-1]
        
        # Write the corrected content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(content)

# Example usage
input_file = "arbitrage_results.json"
output_file = "arbitrage_results_sorted.json"

# Remove trailing comma from input file
remove_trailing_comma(input_file, input_file)

# # Read and sort JSON data
# sorted_data = read_and_sort_json(input_file)

# # Write sorted data to output file
# with open(output_file, 'w') as file:
#     json.dump(sorted_data, file, indent=4)
