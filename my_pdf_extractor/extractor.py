import re
import fitz  # PyMuPDF
import os
import csv


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with fitz.open(pdf_path) as pdf_file:
            for page in pdf_file:
                text += page.get_text()
    except Exception as e:
        print(f"Error occurred while extracting text from PDF: {e}")
        # Optionally, you can raise the exception to propagate it to the caller
        raise
    return text


def extract_info(text):
    """Extract information (name, phone number, email) from text."""
    # Regular expressions for extracting email and phone number
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_regex = r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})\b'

    # Initialize variables
    emails = []
    phones = []
    first_name = ""
    last_name = ""

    try:
        # Find all email addresses
        emails = re.findall(email_regex, text)
        # Find all phone numbers
        phones = re.findall(phone_regex, text)

        # Assume first and last name appear before email or phone
        name_pattern = re.compile(r'([A-Z][a-z]+)\s+([A-Z][a-z]+)')
        name_match = name_pattern.search(text)
        if name_match:
            first_name = name_match.group(1)
            last_name = name_match.group(2)
    except Exception as e:
        print(f"Error occurred while extracting information: {e}")
        # Optionally, you can raise the exception to propagate it to the caller
        raise

    # Format phone number
    phone_number = "-".join([part for part in phones[0] if part]) if phones else None

    return {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": emails[0] if emails else None
    }


def extract_info_from_file(file_path):
    """Extract information from a file."""
    try:
        if file_path.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        print(f"Error occurred while processing file {file_path}: {e}")
        # Optionally, you can raise the exception to propagate it to the caller
        raise

    return extract_info(text)


def extract_info_from_folder(folder_path):
    """Extract information from all files in a folder."""
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        results = []
        for file in files:
            file_path = os.path.join(folder_path, file)
            results.append(extract_info_from_file(file_path))
    except Exception as e:
        print(f"Error occurred while processing folder {folder_path}: {e}")
        # Optionally, you can raise the exception to propagate it to the caller
        raise

    return results


def write_dict_to_csv(list_of_dicts, csv_file_path):
    """Write a list of dictionaries to a CSV file."""
    try:
        with open(csv_file_path, 'w', newline='') as file:
            fieldnames = set().union(*(d.keys() for d in list_of_dicts))
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for data in list_of_dicts:
                writer.writerow(data)
    except Exception as e:
        print(f"Error occurred while writing to CSV file {csv_file_path}: {e}")
        # Optionally, you can raise the exception to propagate it to the caller
        raise

