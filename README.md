
# Tamil Font Generator

The Tamil Font Generator is a Python-based tool designed for creating custom fonts from handwritten letters.

## Overview

The TTF (TrueType Font) file serves as the foundational file for rendering fonts in design tools and document writing software. Our current plan involves creating a TTF specifically for Tamil fonts. To accomplish this, we will begin by generating SVG images. Within our tool, we can convert PNG images to SVG and subsequently use these converted SVG images to produce the TTF file.

Note: This tool acts as a font generator not only for Tamil but also for all languages by allowing users to upload JPG images of handwritten letters.

## Project Stages

### Initial Stage
Initially, our focus was on mapping Unicode characters to the fonts and creating proper SVG images.

### Current Progress
To achieve our project goals, we have completed the following steps:

1. **Handwritten Text to PNG**
   - Cropped each letter from uploaded JPG images.
   - Preprocessed images before converting them into PNGs for accuracy.
   - Removed backgrounds and converted them into PNG images.

2. **PNG to SVG Conversion**
   - Generated PBM (Portable Bitmap Format) files before converting them into SVG images.
   - Produced SVG images from PNG files.

3. **SVG to TTF**
   - Collected SVG images and mapped them to appropriate Unicode characters.
   - Generated the TTF file.

### Pending Tasks

- **Font Metadata**
  - Add font metadata such as font name and language.

- **Unicode Mapping**
  - Complete recognition of letters for the Unicode map.
  - Executed a Python script using Tesseract to analyze SVG image geometry, which is functioning correctly. Finalizing Unicode mapping is planned within a week.

## Usage
- Clone this repo
- activate the virtual env
- Run the app
```bash
streamlit run app.py
