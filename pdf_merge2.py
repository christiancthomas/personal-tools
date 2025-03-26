# this version uses pikepdf to merge pdfs. pikepdf will preserve some of the original document properties better than PyPDF2.
import pikepdf
import os

def merge_pdfs(input_directory, output_filename):
    """Merge PDFs while better preserving original document properties"""
    try:
        pdf_files = [f for f in os.listdir(input_directory) if f.lower().endswith('.pdf')]
        pdf_files.sort()

        if not pdf_files:
            print("No PDF files found in the specified directory.")
            return False

        # Create a new PDF
        merged_pdf = pikepdf.Pdf.new()

        # Add each PDF's pages to the merged PDF
        for pdf_file in pdf_files:
            file_path = os.path.join(input_directory, pdf_file)
            print(f"Processing {pdf_file}")

            with pikepdf.open(file_path) as pdf:
                merged_pdf.pages.extend(pdf.pages)

        # Save the merged PDF
        merged_pdf.save(output_filename)
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