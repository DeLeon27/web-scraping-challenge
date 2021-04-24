from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return_data = {}
    driver.close()
    return return_data

# Create Mission to Mars global dictionary that can be imported into Mongo
mission_to_mars = {}    

# NASA MARS NEWS
def scrape_mars_news():

        # Initialize browser 
        browser = init_browser()

        #browser.is_element_present_by_css("div.content_title", wait_time=1)

        # Visit Nasa news url through splinter module
        Marsnews_url = 'https://mars.nasa.gov/news/'
        browser.visit(Marsnews_url)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        MarsNews_soup = soup(html, 'html.parser')

        # Retrieve the latest element that contains news title and news_paragraph
        News_title = soup.find('div', class_='content_title').find('a').text
        News_paragraph = soup.find('div', class_='article_teaser_body').text

        # Dictionary entry from MARS NEWS
       mission_to_mars['News_title'] = News_title
        mission_to_mars['News_paragraph'] = News_paragraph


        return mission_to_mars

        browser.quit()


# FEATURED IMAGE
def scrape_mars_image():

        # Initialize browser 
        browser = init_browser()

        # Visit Mars Space Images through splinter module
        mars_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(mars_image_url)
        base_url = 'https://www.jpl.nasa.gov'

        # HTML Object 
        html = browser.html

        # Parse HTML with Beautiful Soup
        MarsNews_soup = soup(html, 'html.parser')

        # Retrieve background-image url from style tag 
        image_url=soup.find("a", class_ = "button fancybox")["data-fancybox-href"]
        featured_image_url = base_url + image_url
        print(featured_image_url)

        
        browser.quit()

        return mission_to_mars

        
# Mars Facts
def scrape_mars_facts():

        # Initialize browser 
        browser = init_browser()

         # Visit Mars facts url 
        url = 'http://space-facts.com/mars/'
        browser.visit(url)

        # Use Pandas to "read_html" to parse the URL
        tables = pd.read_html(url)
        # Mars Facts DataFrame 
        facts_df = tables[0]
        facts_df.columns = ['Fact', 'Value']
        facts_df['Fact'] = facts_df['Fact'].str.replace(':', '')
        facts_df

        # Show as html table string
        facts_df = tables[0]
        facts_df.columns = ['Fact', 'Value']
        facts_df['Fact'] = facts_df['Fact'].str.replace(':', '')
        facts_df
        facts_html = facts_df.to_html()

print(facts_html)

        # Dictionary entry from Mars Facts

        mission_to_mars['tables'] = html_table

        return mission_to_mars

# Mars Hemisphere

def scrape_mars_hemispheres():

        # Initialize browser 
        browser = init_browser()

        # Visit hemispheres website through splinter module 
        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)

        # HTML Object
        html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
        MarsNews_soup = soup(html_hemispheres, 'html.parser')

        # Retreive all items that contain mars hemispheres information
        items = soup.find_all('div', class_='item')

        # Create empty list for hemisphere urls 
       hemisphere_image_urls = []

        # Store the main_ul 
        hemispheres_main_url = 'https://astrogeology.usgs.gov' 

        # Loop through the items previously stored
        for i in items: 
            # Store title
            title = i.find('h3').text
            
            # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            # Visit the link that contains the full image website 
            browser.visit(hemispheres_main_url + partial_img_url)
            
            # HTML Object of individual hemisphere information website 
            partial_img_html = browser.html
            
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            MarsNews_soup = soup( partial_img_html, 'html.parser')
            
            # Retrieve full image source 
            image_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            
            # Append the retreived information into a list of dictionaries 
            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

        mission_to_mars['hemisphere_image_urls'] = hemisphere_image_urls
        
       
        browser.quit()


if __name__ == "__main__":
    print(scrape_info() )