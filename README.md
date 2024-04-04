
# PlantGrowingContainers

![Project Render 1](imagesAndVideos/render1.png)
# Introduction to the Project

This project was initiated with the aim of securing funding at the technical university, within the framework of the "Spectrum" scientific club. The primary focus is to investigate the impact of electromagnetic fields on plant growth. To this end, the project proposes the construction of two boxes, both of which are remotely and automatically controlled. These boxes are equipped to monitor various environmental conditions such as temperature, humidity, and sunlight exposure, among others. Additionally, the project includes provisions for photographing the plants to compare the growth of control and experimental samples. This research could provide invaluable insights into how electromagnetic fields influence plant development, which has implications for both scientific understanding and practical applications in agriculture and environmental management.


# Mechanics

![Project Render 2](imagesAndVideos/render2.png)
![Project Render 3](imagesAndVideos/render3.png)
![Project Render 4](imagesAndVideos/render4.png)
![Project Render 5](imagesAndVideos/render5.png)


The project utilizes Fusion 360 for the design and assembly planning, ensuring precise construction. The structural framework is made from V-slot 2020 aluminum profiles, creating a sturdy and adaptable base. Enclosures are constructed from 50x50 cm plywood sheets, chosen for their flexibility and ease of handling. Key components that required customization were produced using 3D printing, allowing for precise fitting and functionality tailored to the project's needs. This approach provides a solid yet flexible setup for conducting research on the impact of electromagnetic fields on plant growth.

![Assembly Step 0](imagesAndVideos/assembly0.jpeg)
![Assembly Step 1](imagesAndVideos/assembly1.jpeg)
![Assembly Step 2](imagesAndVideos/assembly2.jpeg)
![Assembly Step 3](imagesAndVideos/assembly3.jpeg)
![Assembly Step 4](imagesAndVideos/assembly4.jpeg)
![Assembly Step 5](imagesAndVideos/assembly5.jpeg)


# Electronics

The system converts 230VAC to 12VDC using a power supply, then steps down to 5VDC for electronics, including the ESP32 microcontroller, sensors, and LCD. One box houses the 12VDC to 5VDC converter, ESP32, sensors, and an LCD connected to an encoder for navigation. The other contains an 8-relay module controlling fans, LED strips, and a peristaltic pump for irrigation. The ESP32 connects to a magnetometer and barometric sensor via I2C, measuring magnetic forces and atmospheric pressure. Current software favors a web interface over the LCD and encoder for ease of use and settings adjustments. Lighting intensity and air temperature/humidity are monitored to ensure optimal growing conditions.


# Software Components

## ESP32 for Measurements
The core of the project is the ESP32 microcontroller, which uses various communication protocols like I2C, SPI, and GPIO to connect to devices. It runs on GUI-Generic software developed by krycha88, available on GitHub, and integrates with the supla.org IoT platform. This setup allows for the remote management of connected devices over the local network, enabling efficient configuration and real-time data acquisition from sensors.

![Supla Example 1](imagesAndVideos/supla1.png)
![Supla Example 2](imagesAndVideos/supla2.png)
![Supla Example 3](imagesAndVideos/supla3.png)
![Supla Example 4](imagesAndVideos/supla4.png)




https://github.com/lukasznowarkiewicz/PlantGrowingContainers/assets/82212257/1b0bc497-01b2-416b-923e-d7e70e49807f


## ESP32 for Image Capture
An additional ESP32 module, equipped with a camera, is dedicated to capturing images within the system. This module, through its built-in web server, offers live streaming capabilities over the local network. A specialized Python script is employed to automate the process of image capture, saving the photos for further analysis. This feature facilitates continuous monitoring of the project's environment, allowing for detailed observation of plant growth and development under varying conditions.

![ESP32 Camera Streaming](imagesAndVideos/esp32_camera.png)


## Local Server for Image Acquisition
To handle the images captured by the ESP32 camera module, a local server runs a Python script that periodically queries the camera for new images. This script processes and stores these images in a designated folder, making them readily available for review and analysis. This setup ensures that all captured data, including photographic evidence of the experiment's progress, is systematically organized and easily accessible for further study.

![Photo Server Demo](imagesAndVideos/demo_photo_server.jpeg)


## Filka.io for Data Visualization
The project also utilizes Filka.io, an online platform designed for collecting and analyzing sensor data, as well as managing IoT devices. By connecting the system to Filka.io, users can visualize measurement data in real-time, creating reports and notifications that facilitate immediate response to environmental changes or device status updates. This integration enhances the project's ability to monitor, analyze, and respond to the collected data, making it an essential tool for comprehensive research analysis and presentation.

![Filka.io Dashboard](imagesAndVideos/filka_io_dashboard.png)
![Filka.io Visualization](imagesAndVideos/filka_io_visualization.png)


# Documentation

Within the project's repository, there is a dedicated folder containing comprehensive documentation written in Polish. This documentation has been meticulously crafted to meet the internal needs of researchers and individuals directly involved in conducting the experiments. It provides a detailed description of all aspects of the project, including but not limited to, the mechanical design, electronic setup, software configuration, and operational procedures. The aim of this documentation is to ensure that team members have a thorough understanding of the project's components and methodologies, facilitating efficient management and execution of the research activities.



