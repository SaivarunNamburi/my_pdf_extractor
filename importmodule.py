from my_pdf_extractor.extractor import *

try:
    # info = extract_info_from_file("C:\Disk_D\CourseWork\Intro to Programming for DS\Project\Resumes\Colon_2024 Resume.pdf")
    # print(type(info))
    info = extract_info_from_folder("C:\Disk_D\CourseWork\Intro to Programming for DS\Project\Resumes")
    print(info)
    csv_file_path = 'resume_info.csv'
    write_dict_to_csv(info, csv_file_path)
    print(f"CSV file '{csv_file_path}' has been created.")

except Exception as e:
    print(f"Error occurred: {e}")