title=({"WAR"})
topic=("International News")
def show_page(title, description, button):
#this is the only function
    print(title)
    print(description)
    while input("Type " + button + ": ") != button:
        pass


while True:
    print(topic)
    input("Press Enter to start")

    show_page("WAR", "Description: The war in Ukraine continues, with Russia carrying out missile and drone strikes on Kyiv and heavy drone warfare along the front lines.", "next")

    show_page("AI", "Government Actions & Security: The U.S. government has officially banned China’s DeepSeek AI from federal agencies, and OpenAI accused a former employee of planting a secret recording device and leaking intelligence.", "next")

    show_page("GLOBAL WARMING", "Global warming is accelerating rapidly as rising greenhouse gas emissions push key Earth systems toward critical limits ahead of the upcoming United Nations COP31 climate talks.", "next")

    show_page("POLITICS", "With just two weeks until the November 3, 2026, midterm elections, Al Jazeera reports that the political landscape is dominated by heavy campaigning as Democrats hold a significant polling lead over Republicans amid widespread voter frustration regarding the economy, inflation, and the ongoing war in Iran.", "next")

    show_page("SPORTS", "Major League Baseball has set up a historic, all-indoor World Series matchup between the Tampa Bay Rays and the Milwaukee Brewers, guaranteeing a first-time champion for either franchise. Meanwhile, the NBA season has officially tipped off today with a reloaded landscape, while European Champions League soccer is in full swing with major mid-week group stage fixtures.", "return")