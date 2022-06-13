# Elastic Pendulum Simulation
By: Andy Kraja and Kevin Li

### Description:
Our goal was to create an accurate simulation of an elastic pendulum, or a pendulum with a spring instead of a string, using python and its libraries.

### Prerequisites:
Vpython is required.  
Install using $pip install vpython in terminal/command prompt.

### Instructions:
Clone the github repository.  
Run the program using $python epen.py or running the file in IDLE.  
Once the browser tab opens, you can adjust the starting conditions using the sliders before pressing the start button. You can pause and resume at any time, as well as adjust the variables.

### Features:
Sliders to adjust  
  - Gravity  
  - Mass of Ball
  - Starting Angle of Pendulum
  - Initial Stretch of String
  - Spring Constant K
Pause and Resume Button
Reset Button (Sets velocity, acceleration all back to 0, puts elastic pendulum back in its initial conditions based on the sliders)
### Bugs:
Adjusting the variables as the elastic pendulum moves is physically accurate, but it may lead to certain bugs if there is a rapid change (i.e. rapidly decreasing the mass)
