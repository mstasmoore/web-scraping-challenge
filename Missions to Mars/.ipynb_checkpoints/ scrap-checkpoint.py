{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b44d9cae",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd\n",
    "import requests\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9358f73c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\mstas\\\\.wdm\\\\drivers\\\\chromedriver\\\\win32\\\\104.0.5112\\\\chromedriver.exe'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "manager = ChromeDriverManager() \n",
    "manager.install()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3cfb12c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': manager}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b061e3ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: webdriver-manager in c:\\users\\mstas\\anaconda3\\lib\\site-packages (3.8.3)\n",
      "Requirement already satisfied: requests in c:\\users\\mstas\\anaconda3\\lib\\site-packages (from webdriver-manager) (2.26.0)\n",
      "Requirement already satisfied: tqdm in c:\\users\\mstas\\anaconda3\\lib\\site-packages (from webdriver-manager) (4.62.3)\n",
      "Requirement already satisfied: python-dotenv in c:\\users\\mstas\\anaconda3\\lib\\site-packages (from webdriver-manager) (0.20.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\mstas\\anaconda3\\lib\\site-packages (from requests->webdriver-manager) (2021.10.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\mstas\\anaconda3\\lib\\site-packages (from requests->webdriver-manager) (1.26.7)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\mstas\\anaconda3\\lib\\site-packages (from requests->webdriver-manager) (3.2)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\mstas\\anaconda3\\lib\\site-packages (from requests->webdriver-manager) (2.0.4)\n",
      "Requirement already satisfied: colorama in c:\\users\\mstas\\anaconda3\\lib\\site-packages (from tqdm->webdriver-manager) (0.4.4)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install webdriver-manager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0fda004d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "\n",
    "driver = webdriver.Chrome(ChromeDriverManager().install())\n",
    "\n",
    "driver.get(\"http://www.python.org\")\n",
    "\n",
    "driver.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "670273b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e918431",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "52fed270",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pull from url\n",
    "\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n",
    "time.sleep(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "342220eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e01cbe5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Label-title\n",
    "\n",
    "title = soup.find('div', class_=\"content_title\").text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "ddaca3de",
   "metadata": {},
   "outputs": [],
   "source": [
    "paragraph = soup.find('div', class_ = \"article_teaser_body\").text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "510006ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's InSight 'Hears' Peculiar Sounds on Mars\n",
      "Listen to the marsquakes and other, less-expected sounds that the Mars lander has been detecting.\n"
     ]
    }
   ],
   "source": [
    "print(title)\n",
    "print(paragraph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "bd4c1915",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://spaceimages-mars.com/image/featured/mars2.jpg\n"
     ]
    }
   ],
   "source": [
    "images_url = 'https://spaceimages-mars.com'\n",
    "browser.visit(images_url)\n",
    "\n",
    "images_html = browser.html\n",
    "images_soup = bs(images_html, \"html.parser\")\n",
    "\n",
    "browser.links.find_by_partial_text('FULL IMAGE').click()\n",
    "time.sleep(3)\n",
    "images_html = browser.html\n",
    "images_soup = bs(images_html, 'html.parser')\n",
    "\n",
    "featured_image = images_soup.find('img', class_='fancybox-image')\n",
    "featured_image_url = 'https://spaceimages-mars.com/'+ featured_image['src']\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "140b2da1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#mars\n",
    "\n",
    "mars_facts_url = 'https://galaxyfacts-mars.com'\n",
    "browser.visit(mars_facts_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f90dc860",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Facts</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                               Mars\n",
       "Facts                              \n",
       "Diameter:                  6,779 km\n",
       "Mass:               6.39 × 10^23 kg\n",
       "Moons:                            2\n",
       "Distance from Sun:   227,943,824 km\n",
       "Length of Year:      687 Earth days\n",
       "Temperature:           -87 to -5 °C"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#data set up \n",
    "\n",
    "tables = pd.read_html(mars_facts_url)\n",
    "df = tables[0]\n",
    "df.rename(columns={0:'Facts',1:'Mars'}, inplace=True)\n",
    "df = df.iloc[1: , :]\n",
    "df = df.drop([2], axis=1)\n",
    "df = df.reset_index(drop=True)\n",
    "df.set_index('Facts', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7cea4d22",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n    </tr>\\n    <tr>\\n      <th>Facts</th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html_table = df.to_html()\n",
    "html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "fc0be0f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemispheres_url = 'https://marshemispheres.com/'\n",
    "browser.visit(hemispheres_url)\n",
    "titles = []\n",
    "urls = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8269bec1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's InSight 'Hears' Peculiar Sounds on Mars\n",
      "['https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg', 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg', 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg', 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg']\n"
     ]
    }
   ],
   "source": [
    "hemispheres_html = browser.html\n",
    "hemispheres_soup = bs(hemispheres_html, \"html.parser\")\n",
    "hemispheres = hemispheres_soup.find_all('div', class_=\"description\")\n",
    "for hemisphere in hemispheres:\n",
    "    titles.append(hemisphere.find('a').text.strip())\n",
    "    browser.links.find_by_partial_text(hemisphere.find('a').text.strip()).click()\n",
    "    time.sleep(1)\n",
    "    hemisphere_html = browser.html\n",
    "    hemisphere_soup = bs(hemisphere_html, 'html.parser')\n",
    "    hemisphere_image = hemisphere_soup.find('img', class_='wide-image')\n",
    "    hemisphere_image_url = hemispheres_url + hemisphere_image['src']\n",
    "    urls.append(hemisphere_image_url)\n",
    "    browser.links.find_by_partial_text('Back').click()\n",
    "    time.sleep(1)\n",
    "print(title)\n",
    "print(urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "98cbedcf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_list = []\n",
    "i = 0\n",
    "for title in titles:\n",
    "    img_url = urls[i]\n",
    "    hemisphere_dictionary = {'title': title, 'img_url': img_url}\n",
    "    hemisphere_list.append(hemisphere_dictionary)\n",
    "    i += 1\n",
    "hemisphere_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "18eeb428",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1b832f9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
