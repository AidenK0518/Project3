# Project 3

The third and final project for SIUE cs325 Software Development class. This project consists of 4 python files and a .yaml file.

# How to run

Install all the files into a folder, make sure you have everything in the .yaml (PyTorch, HuggingFace, BeautifulSoup, and Transformers). When all of these are installed, run test_sentiment_analyzer.py to make sure the instalation is correct. If any of the 3 test cases do not work, attempt to reinstall or change the prompts inside to make sure the AI can distinguish between the three. When these test cases are valid and running fine, run main.py.

# What the program does.

The program uses a local LLM in parallel with a web scraping program. The local LLM is stored inside of sentiment_analyzer.py, where the class of the same name will run through a selection of the headlines and judge if they are Positive, Negative, or Neutral. The scraper is stored in scraper.py, which this will read a selection of URLs provided in urls.txt and grab the HTML code from them, using BeautifulSoup to clean it up and extract just the headlines. Both of these files are combined inside of main.py, which sets the name of the model we will be using (by default, phi-2) and where our input and output files are (by default, urls.txt and results.txt).

# Possible Errors

1. The results only will say unknown.
   Cause: The AI is producing a response that is not one of the three that we should be getting.
   Solution: Attempt to rerun first, if that does not work, go into sentiment_analyzer.py and in prompt, strengthen it (add words like "only respond in one word")
2. The results are not going into results.txt
   Cause: It is unable to find the file to write to.
   Solution: Check the spelling of results.txt to verify the file name is correct
3. No headlines are being scraped.
   Cause: It is unable to read urls.txt
   Solution: Check the spelling of urls.txt to verify the file name is correct. If it is, check to see if there are any urls inside of the text file and save the text document.
