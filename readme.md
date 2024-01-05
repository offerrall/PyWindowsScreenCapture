
# PyWindowsScreenCapture

This Python wrapper, `PyWindowsScreenCapture`, is designed to simplify the use of the Windows Screen Capture DLL in Python applications. It provides an easy-to-use interface for capturing screens on Windows platforms.

The DLL is here: [WindowsScreenCapture](https://github.com/offerrall/WindowsScreenCapture)

## Fast
The DLL is written in C and uses the Windows API to capture screens. It is designed to be fast and efficient, and it can capture screens at a rate of 60 FPS.

In my pc is 10-20% more faster than [mss](https://github.com/BoboTiG/python-mss)
but it is not cross-platform and this library is in beta.

For professional use, I recommend mss, but if you want more speed, you can use this library.

## Features
- **Simple Interface**: Offers a straightforward Pythonic interface to the low-level DLL functions.
- **Multiple Monitor Support**: Can capture screens from multiple monitors connected to the system.
- **Dynamic Resource Management**: Automatically handles the allocation and release of resources.

## Requirements
- The Windows Screen Capture DLL compiled and available on the system.
- Python 3.x environment.
- For the example, the numpy and PIL libraries are required.

## Installation
1. Ensure the Windows Screen Capture DLL is compiled and located in a known directory.
2. Place the `PyWindowsScreenCapture.py` file in your project directory.

## Usage
```python
from PyWindowsScreenCapture import PyWindowsScreenCapture, MonitorInfo

# Initialize the wrapper with the path to your DLL
screen_capture = PyWindowsScreenCapture('path_to_dll')

# Get information about connected monitors
monitors = screen_capture.get_monitors_info()

# Capture a specific monitor (e.g., primary monitor)
data, width, height = screen_capture.capture_monitor(0)

# Process the captured data...
# ...

# Free resources when done
screen_capture.free_all_captures()
```

For proccessing the captured data, you can use the numpy library to convert the data to a numpy array:
```python
import numpy as np
from PIL import Image

dll_path = "./WindowsScreenCapture.dll"
screen_capture = PyWindowsScreenCapture(dll_path)
monitors_info = screen_capture.get_monitors_info()

data, width, height = screen_capture.capture_monitor(0)

# Convert the data to a NumPy array
if data:
    print("width: ", width)
    # Convert the raw data to a NumPy array
    image_shape = (height, width, 3)
    image_array = np.ctypeslib.as_array(data, shape=image_shape)
    image_array = image_array[:, :, ::-1]
    # Save the image using PIL
    image = Image.fromarray(image_array, 'RGB')
    image.save("test.png")

# Free the memory allocated by the DLL
screen_capture.free_all_captures()
```

## API Overview
- `get_monitors_info`: Retrieve information about all connected monitors.
- `capture_monitor`: Capture the screen of a specified monitor.
- `free_all_captures`: Release resources allocated for screen captures.

## Contributions
Contributions to both the DLL and the Python wrapper are welcome. Feel free to submit pull requests or open issues for any bugs or feature requests.

## License
The PyWindowsScreenCapture wrapper is released under the MIT License.
