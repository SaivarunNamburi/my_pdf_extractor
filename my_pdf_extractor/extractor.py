import re
import fitz  # PyMuPDF
import os
import csv


def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf_file:
        for page in pdf_file:
            text += page.get_text()
    return text


def extract_info(text):
    # Regular expressions for extracting email and phone number
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_regex = r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})\b'

    # Find all matches
    emails = re.findall(email_regex, text)
    phones = re.findall(phone_regex, text)

    # Assume first and last name appear before email or phone
    name_pattern = re.compile(r'([A-Z][a-z]+)\s+([A-Z][a-z]+)')
    name_match = name_pattern.search(text)
    first_name = ""
    last_name = ""
    if name_match:
        first_name = name_match.group(1)
        last_name = name_match.group(2)

    phone_number = "-".join([part for part in phones[0] if part]) if phones else None
    return {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": emails[0] if emails else None
    }


def extract_info_from_file(file_path):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format")

    return extract_info(text)


def extract_info_from_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    results = []
    for file in files:
        file_path = os.path.join(folder_path, file)
        results.append(extract_info_from_file(file_path))
    return results


def write_dict_to_csv(list_of_dicts, csv_file_path):
    with open(csv_file_path, 'w', newline='') as file:
        fieldnames = set().union(*(d.keys() for d in list_of_dicts))
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in list_of_dicts:
            writer.writerow(data)
