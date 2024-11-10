from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
chrome.get("file:///home/thalison/Documentos/beemon/antiscraping-toolkit/examples/fingerprint_catcher.html")
sleep(5)

before_fingerprint = chrome.find_element(By.ID, "fingerprint").text
print(f"Fingerprint antes: {before_fingerprint}")

chrome.execute_cdp_cmd("Emulation.setHardwareConcurrencyOverride", {"hardwareConcurrency": 2})
chrome.refresh()
sleep(5)

after_fingerprint = chrome.find_element(By.ID, "fingerprint").text
print(f"Fingerprint depois: {after_fingerprint}")