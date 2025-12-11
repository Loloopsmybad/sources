import PyPDF2
import pyttsx3
import argparse
import os

def extract_text_from_pdf(pdf_path, start_page=None, end_page=None):
    """
    Extract text from a PDF file with optional page range.
    
    Args:
        pdf_path (str): Path to the PDF file
        start_page (int, optional): First page to read (1-indexed)
        end_page (int, optional): Last page to read (1-indexed)
        
    Returns:
        str: Extracted text from the PDF
    """
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get number of pages
            num_pages = len(pdf_reader.pages)
            print(f"PDF has {num_pages} pages")
            
            # Adjust page range
            if start_page is None:
                start_page = 1
            if end_page is None:
                end_page = num_pages
            
            # Convert to 0-indexed
            start_idx = max(0, start_page - 1)
            end_idx = min(num_pages, end_page)
            
            if start_idx >= num_pages or end_idx <= 0 or start_idx > end_idx:
                print("Invalid page range")
                return None
            
            print(f"Reading pages {start_page} to {end_page}")
            
            # Extract text from specified pages
            text = ""
            for page_num in range(start_idx, end_idx):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                if page_text:
                    text += f"\n--- Page {page_num + 1} ---\n" + page_text
                
            return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

def text_to_speech(text, output_file=None, rate=150, voice=None):
    """
    Convert text to speech.
    
    Args:
        text (str): Text to convert to speech
        output_file (str, optional): Path to save audio file (if None, plays audio directly)
        rate (int): Speech rate (words per minute)
        voice (str, optional): Voice ID to use
    """
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()
        
        # Set properties
        engine.setProperty('rate', rate)  # Speed of speech
        
        # Set voice if specified
        if voice:
            voices = engine.getProperty('voices')
            for v in voices:
                if voice in v.id:
                    engine.setProperty('voice', v.id)
                    break
        
        if output_file:
            # Save to file
            engine.save_to_file(text, output_file)
            engine.runAndWait()
            print(f"Audio saved to {output_file}")
        else:
            # Speak the text
            engine.say(text)
            engine.runAndWait()
    except Exception as e:
        print(f"Error converting text to speech: {e}")

def list_available_voices():
    """List all available voices on the system"""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    print("Available voices:")
    for i, voice in enumerate(voices):
        print(f"{i+1}. ID: {voice.id}")
        print(f"   Name: {voice.name}")
        print(f"   Languages: {voice.languages}")
        print(f"   Gender: {voice.gender}")
        print(f"   Age: {voice.age}")
        print("-" * 40)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Read PDF files aloud using text-to-speech")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("-s", "--start-page", type=int, help="First page to read (starts at 1)")
    parser.add_argument("-e", "--end-page", type=int, help="Last page to read")
    parser.add_argument("-p", "--page", type=int, help="Read a single specific page")
    parser.add_argument("-o", "--output", help="Save audio to file instead of playing it")
    parser.add_argument("-r", "--rate", type=int, default=150, help="Speech rate (words per minute)")
    parser.add_argument("-v", "--voice", help="Voice ID to use")
    parser.add_argument("-l", "--list-voices", action="store_true", help="List available voices and exit")
    
    # Parse arguments
    args = parser.parse_args()
    
    # List voices if requested
    if args.list_voices:
        list_available_voices()
        return
    
    # Check if file exists
    if not os.path.isfile(args.pdf_path):
        print(f"Error: The file '{args.pdf_path}' does not exist.")
        return
    
    # Determine page range
    start_page = args.start_page
    end_page = args.end_page
    
    # If single page is specified, use it for both start and end
    if args.page:
        start_page = args.page
        end_page = args.page
    
    # Extract text from PDF
    print(f"Extracting text from {args.pdf_path}...")
    text = extract_text_from_pdf(args.pdf_path, start_page, end_page)
    
    if text:
        print("Converting text to speech...")
        text_to_speech(text, args.output, args.rate, args.voice)
    else:
        print("Failed to extract text from the PDF.")

if __name__ == "__main__":
    main()