import time
import random
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def human_pause(min_sec=0.5, max_sec=1.5):
    """
    Pause the script for a random duration between min_sec and max_sec.
    This helps mimic human interaction.
    """
    time.sleep(random.uniform(min_sec, max_sec))


def fill_radio_questions(driver):
    """
    Locates all groups of radio buttons (i.e., [role='radiogroup'])
    and selects a random option in each.
    """
    radio_groups = driver.find_elements(By.CSS_SELECTOR, "[role='radiogroup']")
    for group in radio_groups:
        options = group.find_elements(By.CSS_SELECTOR, "[role='radio']")
        if options:
            random.choice(options).click()
            human_pause()  # Pause slightly after each click


def fill_form(thread_id, submissions_per_thread):
    """
    Each thread runs this function to submit the form the specified number of times.
    """
    submissions_done = 0
    
    while submissions_done < submissions_per_thread:
        # Initialize WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        try:
            # Go to the Google Form link
            driver.get("https://docs.google.com/forms/d/e/1FAIpQLSebuO_V3MIkXQQdcq-H39j2Kzsjp7DxxXGLF2wOXjKfpZH6BA/viewform")
            human_pause(2, 3)  # Let the form load

            # Fill the first page (randomly selecting radio options)
            fill_radio_questions(driver)

            # Click the Next button
            next_button = driver.find_element(By.CSS_SELECTOR, "[jsname='OCpkoe']")
            driver.execute_script("arguments[0].click();", next_button)
            human_pause(2, 4)  # Wait for the next page

            # Fill the second page
            fill_radio_questions(driver)

            # Submit the form
            submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button'][jsname='M2UYVd']")
            driver.execute_script("arguments[0].click();", submit_button)

            # Update the submission count for this thread
            submissions_done += 1
            print(f"Thread {thread_id}: Submitted {submissions_done}/{submissions_per_thread}")
            
            # Slight pause before the next submission (so as not to hammer the server)
            human_pause(1, 2)
            
        except Exception as e:
            print(f"Thread {thread_id} encountered an error: {str(e)}")
            human_pause(2, 3)
            
        finally:
            driver.quit()


def main():
    """
    Main entry point to run multiple threads simultaneously and gather user input.
    """
    print("\n===== Made By Riyad M. =====\n")
    print("This script will automate submissions to the specified Google Form.\n")
    
    # Get user input for number of parallel threads/windows
    num_threads = int(input("How many parallel windows? "))
    
    # Get user input for submissions per thread/window
    submissions_per_thread = int(input("How many submissions per window? "))
    
    # Create and start the threads
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=fill_form, args=(i+1, submissions_per_thread))
        threads.append(t)
        t.start()
        human_pause(1, 2)  # Stagger the thread starts so they don't all open at once
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print("\nAll threads have finished their submissions. Thanks for using this script!")
    print("===== Made By Riyad M. =====\n")


if __name__ == "__main__":
    main()
