import fontforge
import os

# Define supported output formats and their corresponding FontForge extensions
output_formats = {
    "ttf": ".ttf",
    "otf": ".otf",
    "woff": ".woff",
    "woff2": ".woff2",
    "svg": ".svg",
    "eot": ".eot",
    "bdf": ".bdf",
    "pfa": ".pfa",
    "pfb": ".pfb",
    "ufo": ".ufo",
    "pcf": ".pcf",
    "afm": ".afm",
    "mm": ".mm",  # Multiple Master fonts (may not be fully supported)
}

def convert_font(input_file, output_dir, selected_formats):
    # Load the font file
    font = fontforge.open(input_file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through each selected format and generate the output
    for format_name in selected_formats:
        if format_name not in output_formats:
            print(f"Unsupported format: {format_name}. Skipping...")
            continue

        extension = output_formats[format_name]
        output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_file))[0]}{extension}")
        print(f"Converting to {format_name.upper()} format...")
        try:
            if format_name in ["woff", "woff2", "svg", "eot"]:
                font.generate(output_path, flags=("opentype"))
            else:
                font.generate(output_path)
            print(f"Successfully generated: {output_path}")
        except Exception as e:
            print(f"Error converting to {format_name.upper()}: {e}")

    # Close the font
    font.close()

if __name__ == "__main__":
    # Input file and output directory
    input_font = "/home/vasanth/font-maker/Generated ttf/tamilfonts.ttf"
    output_directory = "/home/vasanth/font-maker/vasanthoutput"

    if not os.path.isfile(input_font):
        print("The specified input font file does not exist. Please check the path and try again.")
    else:
        # Get user input for formats
        print("Supported formats: " + ", ".join(output_formats.keys()))
        selected_formats = input("Enter the desired formats (comma-separated, e.g., ttf, otf, woff): ").strip().split(",")

        # Clean up input
        selected_formats = [format_name.strip().lower() for format_name in selected_formats]


        convert_font(input_font, output_directory, selected_formats)
