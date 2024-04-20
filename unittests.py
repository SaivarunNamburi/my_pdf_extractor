import unittest
from my_pdf_extractor.extractor import *


class MyTestCase(unittest.TestCase):
    def test_extract_info_from_file_pdf(self):
        file_path = 'Resumes\SaiVaruKumar_A.pdf'
        result = extract_info_from_file(file_path)
        self.assertEqual(result['first_name'], 'Sai')
        self.assertEqual(result['last_name'], 'Varun')
        self.assertEqual(result['phone_number'], '857-265-1349')
        self.assertEqual(result['email'], 'saivarun.namburi@gmail.com')

    # Add more test cases for other file formats if needed

    def test_extract_info_from_folder(self):
        folder_path = 'Resumes'
        result = extract_info_from_folder(folder_path)
        self.assertEqual(len(result), 5)  # Assuming there are 5 resumes in the folder
        # Add assertions for the extracted information from each résumé

    def test_write_dict_to_csv(self):
        data = [
            {'first_name': 'Andres', 'last_name': 'Colon', 'phone_number': '407-750-2656', 'email': 'acolon01@outlook.com'},
            {'first_name': 'Pooja', 'last_name': 'Ramesh', 'phone_number': '857-757-0070', 'email': 'ramesh.po@northeastern.edu'},
            {'first_name': 'Sai', 'last_name': 'Varun', 'phone_number': '857-265-1349', 'email': 'saivarun.namburi@gmail.com'},
            {'first_name': 'Ujjanth', 'last_name': 'Arhan', 'phone_number': '857-313-2887', 'email': 'arhan.u@northeastern.edu'},
            {'first_name': 'Venkat', 'last_name': 'Pavan', 'phone_number': '857-268-9748', 'email': 'munaganti.v@northeastern.edu'}
        ]
        csv_file_path = 'test_output.csv'
        write_dict_to_csv(data, csv_file_path)
        self.assertTrue(os.path.isfile(csv_file_path))


if __name__ == '__main__':
    unittest.main()
