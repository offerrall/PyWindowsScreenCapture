import numpy as np
from PIL import Image
from PyWindowsScreenCapture import PyWindowsScreenCapture

dll_path = "./WindowsScreenCapture.dll"
screen_capture = PyWindowsScreenCapture(dll_path)
monitors_info = screen_capture.get_monitors_info()

data, width, height = screen_capture.capture_monitor(0)

# Convert the data to a NumPy array
if data:
    # Convert the raw data to a NumPy array
    image_shape = (height, width, 3)
    image_array = np.ctypeslib.as_array(data, shape=image_shape)
    image_array = image_array[:, :, ::-1]
    # Save the image using PIL
    image = Image.fromarray(image_array, 'RGB')
    image.save("test.png")

# Free the memory allocated by the DLL
screen_capture.free_all_captures()