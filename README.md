# PDF Resume Extractor

## Summary:

The PDF Resume Extractor is a tool designed to simplify the process of extracting names, phone numbers, and email addresses from PDF files. It addresses the common inefficiencies of manual data extraction, which is prone to errors and time-consuming. By focusing on PDFs, which are commonly used across various industries, this tool provides a specialized solution capable of accurately identifying and retrieving diverse types of contact information embedded in PDFs. This capability is crucial for professionals in fields such as human resources, marketing, and research, as they often need to process substantial amounts of data embedded in documents like resumes effectively.

## How to Use:

### Steps to run this module:

1. **Make sure Python is installed on your system.**

2. **Clone the repository:**
   ```
   git clone https://github.com/SaivarunNamburi/my_pdf_extractor.git
   ```

3. **Navigate to the module directory:**
   ```
   cd my_pdf_extractor
   ```

4. **Install required packages:**
   ```
   pip install .
   ```

5. **Run unit tests:**
   ```
   python test_pdf_extractor.py
   ```

6. **Run the main function:**
   ```
   python importmodule.py
   ```
   Provide the file or folder path for resumes when prompted.

7. **Store output in a CSV file:**
   After obtaining the extracted information, you can utilize the `write_dict_to_csv` function to store the data in a CSV file. Pass the dictionary containing the extracted information and the desired CSV file path as arguments to the function.

8. **Check the output:**
   Once the execution is complete, check if the CSV file has been created and if the extracted data is present.

9. **Integrate with other projects:**
   You can incorporate this module into your other projects by keeping the `my_pdf_extractor` folder in your project directory.

### Steps to run from scratch:

1. **Navigate to the `pdf_resume_parser` directory.**

2. **Create a new Python file in the `pdf_resume_parser` directory.**

3. **Import the `my_pdf_extractor` module at the top of your Python file.**
   ```python
   import my_pdf_extractor
   ```

4. **Utilize the functions provided by the module:**
   You can use functions such as `my_pdf_extractor.extract_info_from_folder`, `my_pdf_extractor.extract_info_from_file`, and `my_pdf_extractor.write_dict_to_csv`. These functions return a dictionary containing the extracted information.

5. **Write the extracted information to a CSV file:**
   Pass the dictionary containing the extracted information and the desired CSV file path to the `write_dict_to_csv` function to create a CSV file with the extracted details.

6. **Congratulations!**
   You have successfully utilized the PDF Resume Extractor for resume parsing.


