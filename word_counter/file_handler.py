def file_select():
    file_path = input("Please copy and paste the path of your file: ") # Variable storing the file path
    
    def write_to_file(file_path):
        with open(file_path, "w+") as file:
            file.write("This is a test.")  # Example content written to the file
    
    write_to_file(file_path)  # Call the function with the variable as the parameter
