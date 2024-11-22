from dataclasses import dataclass, field
from selenium.webdriver import Edge
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@dataclass
class Instance:
    accounts: list = field(init=False)

    # input_elements_names: list = field(default_factory=list)
    # inputs_values: list = field(default_factory=list)
    # last_inputs_values: deque = field(default_factory=deque)
    browser: Edge = field(init=False)
    # caption: WebElement = field(default=None)

    def __post_init__(self):
        self.accounts = [
            ["aldairperezjuarez3@gmail.com",	"4toCreativo_123"],
            ["elenatorresmaya5@gmail.com",	"4toCreativo_123"]
        ]

        options = Options()
        options.add_argument("-inprivate")
        service = Service(
            executable_path="./drivers/msedgedriver.exe")
        self.browser = Edge(service=service, options=options)
        self.browser.get('https://www.facebook.com/promesas.ac/posts/pfbid0ySpVkv5EHcsemG2fsTA4dfBHLcdm75and5Eo77xhudRTajtGitsvQ1DBpzRPJN2ml?rdid=8eZkJ2UJ9sAIuqeq')

    def sign_in(self):
        try:
            email = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                 'label[aria-label="Email or phone number"]'))
            )
            email.click()
            email.send_keys('aldairperezjuarez3@gmail.com')

            password = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                 'label[aria-label="Password"]'))
            )
            password.click()
            password.send_keys('4toCreativo_123\n')            
        except TimeoutException:
            print("El elemento no se encontró dentro del tiempo de espera.")
        except NoSuchElementException:
            print("El elemento no existe en la página.")
        except Exception as e:
            print(f"Ocurrió un error: {e}") 

    def find_interactions_bar(self):
        try:
            elemento = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.xq8finb.x16n37ib"))
            )
            # print(elemento.text)
        except TimeoutException:
            print("El elemento no se encontró dentro del tiempo de espera.")
        except NoSuchElementException:
            print("El elemento no existe en la página.")
        except Exception as e:
            print(f"Ocurrió un error: {e}") 

if __name__ == "__main__":
    instance = Instance()
    input("Presiona Enter para continuar...")
    instance.sign_in()
    input("Presiona Enter para continuar...")
