import pyautogui
import time

# Give time to switch to the Google Doc
time.sleep(5)

# Data to type into the table
table_data = [
    ["Specification", "Design 1 Score", "Design 2 Score"],
    ["A", "4 - The product is minimalist and helps the space feel bigger, but it could have more interesting patterns.", 
         "3 - The design is simple but might be too plain. It could use a little more style to make it fit well in a modern dorm room."],
    ["C", "4 - The cost is kept low, but using eco-friendly materials might increase it slightly.", 
         "3 - The table’s detachable legs might increase costs due to extra material and production steps."],
    ["C", "5 - Perfect for college students since it saves space and is easy to use.", 
         "3 - The detachable legs are useful, but it’s not as multifunctional as Design 1."],
    ["E", "5 - Made from eco-friendly wood and recyclable materials.", 
         "5 - Uses sustainable materials and can be recycled easily."],
    ["S", "5 - Compact and fits well in a small dorm room.", 
         "4 - The table is small, but the detachable legs could make storage a bit tricky."],
    ["S", "3 - It’s sturdy, but the lifting mechanism needs to be durable to avoid breaking.", 
         "4 - The detachable legs are well designed, but they need to be properly secured to ensure safety."],
    ["F", "4 - The product is multi-functional and works well for studying, relaxing, and storing small items.", 
         "3 - The design is simple but not as versatile as Design 1."],
    ["M", "4 - Made from durable wood, but the lifting mechanism needs to be tested for long-term use.", 
         "5 - Strong and lightweight, making it easy to move around."]
]

# Type table data
for row in table_data:
    for cell in row:
        pyautogui.write(cell, interval=0.05)  # Type the cell content
        pyautogui.press('tab')  # Move to next cell
    pyautogui.press('enter')  # Move to next row

# Exit the table and type the final decision
time.sleep(1)  # Pause before typing decision
pyautogui.press('enter')
pyautogui.write("Final Scores:", interval=0.05)
pyautogui.press('enter')
pyautogui.write("Design 1: 38/40", interval=0.05)
pyautogui.press('enter')
pyautogui.write("Design 2: 30/40", interval=0.05)
pyautogui.press('enter')
pyautogui.write("After comparing both designs, I have decided to go with Design 1 because it meets the design specifications better. The main goal was to create furniture that maximizes space, is functional, and works well for students in small rooms. Design 1 is the better option because it’s multi-functional, space-efficient, eco-friendly, and practical for students who need a flexible workspace.", interval=0.05)
