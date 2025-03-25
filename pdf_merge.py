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

        # Get a list of PDF files in the directory
        pdf_files = [f for f in os.listdir(input_directory) if f.lower().endswith('.pdf')]

        # Sort the files to ensure consistent order
        pdf_files.sort()

        # Check if any PDF files were found
        if not pdf_files:
            print("No PDF files found in the specified directory.")
            return False

        # Append each PDF file to the merger
        for pdf_file in pdf_files:
            file_path = os.path.join(input_directory, pdf_file)
            merger.append(file_path)

        # Write the merged PDF to the output file
        with open(output_filename, 'wb') as output_file:
            merger.write(output_file)

        print(f"Successfully merged {len(pdf_files)} PDF files into {output_filename}")
        return True

    except Exception as e:
        print(f"An error occurred while merging PDFs: {e}")
        return False

def main():
    # Example usage
    input_dir = input("Enter the directory path containing PDF files to merge: ").strip()
    output_file = input("Enter the name of the output merged PDF file: ").strip()

    # Ensure the output filename ends with .pdf
    if not output_file.lower().endswith('.pdf'):
        output_file += '.pdf'

    # Merge the PDFs
    merge_pdfs(input_dir, output_file)

if __name__ == "__main__":
    main()