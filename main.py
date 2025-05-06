# Aiden Kohr
# 800719274

# Begin by importing both the HeadlineScraper and SentimentAnalyzer from their respective python files. We also import random to get a mix of the headlines (as we do not want to run through all 100 some headlines!)
import random
from scraper import HeadlineScraper
from sentiment_analyzer import SentimentAnalyzer

def main():
    # Classify some names here and the model we are using, I chose phi-2 (not using tinylama from project 1 as it did not work well with this project.)
    urls_file = "urls.txt"
    output_file = "results.txt"
    model_name = "microsoft/phi-2"

    # Start by scraping the headlines. Then collect a random sample of 10 of those headlines.
    scraper = HeadlineScraper(urls_file)
    all_headlines = scraper.scrape_all()
    headlines = random.sample(all_headlines, min(10, len(all_headlines)))

    # Start up the analyzer.
    analyzer = SentimentAnalyzer(model_name)

    # Once we have our headlines and the analyzer is up and running, we can start feeding it the headlines one by one and writing them to the results.txt file.
    with open(output_file, "w", encoding="utf-8") as outfile:
        for i, headline in enumerate(headlines, start=1):
            sentiment = analyzer.analyze_sentiment(headline)
            result = f"{i}. {headline}\nResult: {sentiment}\n\n"
            print(result.strip())
            outfile.write(result)

    # Let the user know when the results are in.
    print(f"Done. Results written to {output_file}")

if __name__ == "__main__":
    main()