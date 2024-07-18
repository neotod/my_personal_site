import yaml
import json

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


SKILLS_URL = "https://neotod.herokuapp.com/admin/home/skill/"
CHROME_DRIVER_PATH = "./chromedriver"

USERNAME = "neotod"
PASSWORD = "Farcry5Mr.R0B0T"

PROXY_URL = "socks5://127.0.0.1:7890"

# make a new Chrome driver w/ executable path to '/home/neotod/joint/compsci/tmp/chromedriver' and open the skills page
opts = Options()
opts.add_argument(f"--proxy-server={PROXY_URL}")

driver = Chrome(executable_path=CHROME_DRIVER_PATH, options=opts)
driver.get(SKILLS_URL)

# find the username and password fields and fill them in
username_field = driver.find_element(By.CSS_SELECTOR, "#id_username")
username_field.send_keys(USERNAME)
password_field = driver.find_element(By.CSS_SELECTOR, "#id_password")
password_field.send_keys(PASSWORD)

# find the login button and click it
login_button = driver.find_element(
    By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]"
)
login_button.click()

## stage 2
SKILLS_LINKS_XPATH = (
    "/html/body/div/div[3]/div/div[1]/div/div/div/form/div[2]/table/tbody/tr/th/a"
)


def get_skill_data_from_site(skill_name):
    skills_links = driver.find_elements(By.XPATH, SKILLS_LINKS_XPATH)
    corresponding_skill_link = None
    for skill_link in skills_links:
        if skill_name.lower() in skill_link.text.lower():
            corresponding_skill_link = skill_link

    if corresponding_skill_link:
        corresponding_skill_link.click()
        # get the skill data and make it in a form of json

        SKILL_NAME_SELECTOR = "#id_name"

        # wait explicity until an element is loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, SKILL_NAME_SELECTOR))
        )

        skill_name = driver.find_element(
            By.CSS_SELECTOR, SKILL_NAME_SELECTOR
        ).get_attribute("value")

        # find the svg icon field and fill it in
        svg_icon_field = driver.find_element(
            By.CSS_SELECTOR, "#id_svg_icon"
        ).get_attribute("value")

        skill_level = driver.find_element(By.CSS_SELECTOR, "#id_rate").get_attribute(
            "value"
        )

        skill_data = {
            "name": skill_name,
            "svg_icon_html": svg_icon_field,
            "level": int(skill_level),
        }

        # go back into skills page
        driver.get(SKILLS_URL)

        # return the data
        return skill_data
    else:
        # couldn't find the link with the skill name
        return {
            "name": skill_name,
            "svg_icon_html": None,
            "level": None,
        }


with open("./site_parts.json") as f:
    site_parts = json.load(f)

new_skills = {}
for skill_section in site_parts["skills"]:

    new_skills[skill_section] = []
    for skill in site_parts["skills"][skill_section]:
        skill_data_from_site = get_skill_data_from_site(skill["name"])

        new_skills[skill_section].append(
            {
                "name": skill["name"],
                "svg_icon_html": skill_data_from_site["svg_icon_html"],
                "level": skill_data_from_site["level"],
            }
        )

site_parts["skills"] = new_skills

with open("./site_parts_new.json", "w") as f:
    json.dump(site_parts, f, indent=3)
