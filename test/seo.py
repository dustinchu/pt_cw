from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import zipfile
import os


def proxy_chrome(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS):
    manifest_json = """
            {
                "version": "1.0.0",
                "manifest_version": 2,
                "name": "Chrome Proxy",
                "permissions": [
                    "proxy",
                    "tabs",
                    "unlimitedStorage",
                    "storage",
                    "<all_urls>",
                    "webRequest",
                    "webRequestBlocking"
                ],
                "background": {
                    "scripts": ["background.js"]
                },
                "minimum_chrome_version":"22.0.0"
            }
            """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "http",
                host: "%(host)s",
                port: parseInt(%(port)d)
              },
              bypassList: ["foobar.com"]
            }
          };
    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%(user)s",
                password: "%(pass)s"
            }
        };
    }
    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
        """ % {
        "host": PROXY_HOST,
        "port": PROXY_PORT,
        "user": PROXY_USER,
        "pass": PROXY_PASS,
    }

    pluginfile = 'proxy_auth_plugin.zip'

    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    co = Options()
    # extension support is not possible in incognito mode for now
    # co.add_argument('--incognito')
    co.add_argument('--disable-gpu')
    # disable infobars
    co.add_argument('--disable-infobars')
    co.add_experimental_option(
        "excludeSwitches", ["ignore-certificate-errors"])
    # location of chromedriver, please change it according to your project.
    co.add_extension(pluginfile)
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=co)
    # return the driver with added proxy configuration.
    return driver


altarr = [
    '[alt="3M"]',
    '[alt="AVX"]',
    '[alt="Amphenol"]',
    '[alt="APTIV"]',
    '[alt="Coto"]',
    '[alt="DIODES"]',
    '[alt="FUJIKURA"]',
    '[alt="FURUKAWA"]',
    '[alt="FCI"]',
    '[alt="HIRSCHMANN"]',
    '[alt="HIROSE"]',
    '[alt="ITT"]',
    '[alt="IXYS"]',
    '[alt="JAE"]',
    '[alt="JST"]',
    '[alt="KET"]',
    '[alt="KEMET"]',
    '[alt="Keystone Electronics"]',
    '[alt="KUM"]',
    '[alt="Kyocera"]',
    '[alt="Littelfuse"]',
    '[alt="MOLEX"]',
    '[alt="MURATA"]',
    '[alt="NXP"]',
    '[alt="OMRON"]',
    '[alt="Samsung"]',
    '[alt="PHOENIX"]',
    '[alt="SAMTEC"]',
    '[alt="SEI Stackpole Electr"]',
    '[alt="STMicroelectronics"]',
    '[alt="SUMITOMO"]',
    '[alt="Taiyo Yuden"]',
    '[alt="TDK"]',
    '[alt="TE"]',
    '[alt="Texas Instruments"]',
    '[alt="TOKAI RIKA"]',
    '[alt="Toshiba"]',
    '[alt="VISHAY"]',
    '[alt="WAGO"]',
    '[alt="Walsin"]',
    '[alt="YAGEO"]',
    '[alt="YAZAKI"]',
    '[alt="MOREPRODUCTS"]',
]
# driver = webdriver.Chrome(ChromeDriverManager().install())
username = "pteamtech"
password = "76bb3b-357e9e-4492c2-d52f43-35690e"
PROXY_RACK_DNS = "megaproxy.rotating.proxyrack.net:{}".format(
    random.randint(10000, 13999))
while True:
    try:
        driver = proxy_chrome('megaproxy.rotating.proxyrack.net',
                              random.randint(10000, 13999), username, password)
        driver.get("https://www.pingkai.com.tw/en/product.php?cid=14")

        for alt in altarr:
            sleep(1)
            btnImg = driver.find_element_by_css_selector(alt)
            btnImg.click()
            sleep(1)
            driver.back()
        sleep(10)
        driver.close()
        driver.quit()
    except:
        driver.close()
        driver.quit()


# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="AVX"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Amphenol"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="APTIV"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Coto"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="DIODES"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="FUJIKURA"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="FURUKAWA"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="FCI"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="HIRSCHMANN"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="HIROSE"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="ITT"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="IXYS"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="JAE"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="JST"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="KET"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="KEMET"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Keystone Electronics"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="KUM"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Kyocera"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Littelfuse"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="MOLEX"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="MURATA"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="NXP"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="OMRON"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Samsung"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="PHOENIX"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="SAMTEC"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="SEI Stackpole Electr"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="STMicroelectronics"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="SUMITOMO"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Taiyo Yuden"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="TDK"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="TE"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Texas Instruments"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="TOKAI RIKA"]')
# btnImg.click()
# sleep(1)
# driver.back()
# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Toshiba"]')
# btnImg.click()
# sleep(1)
# driver.back()
# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="VISHAY"]')
# btnImg.click()
# sleep(1)
# driver.back()
# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="WAGO"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="Walsin"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="YAGEO"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="YAZAKI"]')
# btnImg.click()
# sleep(1)
# driver.back()

# sleep(1)
# btnImg = driver.find_element_by_css_selector('[alt="MOREPRODUCTS"]')
# btnImg.click()
# sleep(1)
# driver.back()
# driver.back()
# driver.close()
# driver.quit()
