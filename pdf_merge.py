import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_directory, output_filename):
    """
    Merge all PDF files in the specified directory into a single PDF.

    Args:
    input_directory (str): Path to the directory containing PDF files to merge
    output_filename (str): Name of the output merged PDF file

    Returns:
    bool: True if merge successful, False otherwise
    """
    try:
        # Create a PDF merger object
        merger = PdfMerger()
        print('created merger object')

        # Get a list of PDF files in the directory
        pdf_files = [f for f in os.listdir(input_directory) if f.lower().endswith('.pdf')]
        print(f'got list of pdf files: {pdf_files}')
        # Sort the files to ensure consistent order
        pdf_files.sort()
        print('sorted pdf files')

        # Check if any PDF files were found
        if not pdf_files:
            print("No PDF files found in the specified directory.")
            return False

        # Append each PDF file to the merger
        print('found pdf files in directory')
        for pdf_file in pdf_files:
            file_path = os.path.join(input_directory, pdf_file)
            merger.append(file_path)

        # Write the merged PDF to the output file
        with open(output_filename, 'wb') as output_file:
            print('writing merged pdf')
            merger.write(output_file)

        print(f"Successfully merged {len(pdf_files)} PDF files into {output_filename}")
        return True

    except Exception as e:
        print(f"An error occurred while merging PDFs: {e}")
        return False

def main():
    # Example usage
    input_dir = os.path.expanduser("~/Desktop/files")
    output_file = os.path.expanduser("~/Desktop/merged_MSDSprepform_CCT.pdf")

    # Ensure the output filename ends with .pdf
    if not output_file.lower().endswith('.pdf'):
        output_file += '.pdf'

    # Merge the PDFs
    merge_pdfs(input_dir, output_file)

if __name__ == "__main__":
    main()