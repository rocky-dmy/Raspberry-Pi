##############################################################################
#   
#   LCD display
#
##############################################################################

import framebuf
 
# Define the screen size and color mode
width = 128
height = 64
buf = bytearray(width * height // 8)

# FrameBuffer() Creates a frame buffer object that is used to draw graphics on the LCD display
fb = framebuf.FrameBuffer(buf, width, height, framebuf.MONO_VLSB)
 
# Draw graphics on the screen
fb.fill(0)  # Clear the screen
fb.rect(10, 10, 50, 30, 1)  # Draw rectangle
fb.line(0, 0, width - 1, height - 1, 1)  # Draw line
fb.text("Hello", 20, 40, 1)  # Draw text
 
# Displays the graphics on the LCD screen
lcd = LCD()  # Assume that the LCD object has been initialized
lcd.show_framebuffer(fb)
 
print("Graphic display success！")
