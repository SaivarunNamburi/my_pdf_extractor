import my_pdf_extractor

try:
    # info = my_pdf_extractor.extract_info_from_file("Resumes\Colon_2024 Resume.pdf")
    info = my_pdf_extractor.extract_info_from_folder("Resumes")
    csv_file_path = 'resume_info.csv'
    my_pdf_extractor.write_dict_to_csv(info, csv_file_path)
    print(f"CSV file '{csv_file_path}' has been created.")

except Exception as e:
    print(f"Error occurred: {e}")