import zipfile
import py7zr
import os

print("Safe Archive Extractor")

x = input("Path to File: ").strip()
y = input("Extract Location Path: ").strip()

# Validate paths
if not os.path.exists(x):
    print("Error: The specified file path does not exist.")
else:
    blocked_extensions = {".exe", ".bat", ".scr"}

    try:
        if zipfile.is_zipfile(x):  # Handle ZIP files
            with zipfile.ZipFile(x, "r") as zip_ref:
                for file_info in zip_ref.infolist():
                    if any(file_info.filename.endswith(ext) for ext in blocked_extensions):
                        print(f"Warning: Skipping potentially dangerous file {file_info.filename}")
                    else:
                        print(f"Extracting: {file_info.filename}")
                        zip_ref.extract(file_info.filename, y)
            print("ZIP Extraction completed successfully.")

        elif x.endswith(".7z"):  # Handle 7z files
            with py7zr.SevenZipFile(x, mode='r') as archive:
                all_files = archive.getnames()
                safe_files = [f for f in all_files if not any(f.endswith(ext) for ext in blocked_extensions)]
                
                for file in safe_files:
                    print(f"Extracting: {file}")
                archive.extract(targets=safe_files, path=y)
                
            print("7z Extraction completed successfully.")
        else:
            print("Error: Unsupported file format.")
    except Exception as e:
        print(f"Error during extraction: {e}")