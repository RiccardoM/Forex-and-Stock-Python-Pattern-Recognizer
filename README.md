# Forex and Stock Python Pattern Recognizer

## Introduction
This project represents a machine learning program that is able to recognize patterns inside Forex or stock data. 

## Data used
Currently all the data loaded are the ones represented inside the [GBPUSD1d.txt](https://github.com/RiccardoM/Forex-and-Stock-Python-Pattern-Recognizer/blob/master/data/GBPUSD1d.txt) file, which contains bids and asks for 1-day tick data.  
You can also try out the system loading the 1-month tick data (1.63 milions entries) simply by changing the followin code

```python
# settings.py

# Use GBPUSD1d for 1-day tick data (~62k lines) or GBPUSD1m for 1-month tick data (~1.63 mln lines)
file_name = "data/GBPUSD1d.txt"

```

This data was downloaded from the [Sentdex.com](http://sentdex.com/) website, following the url http://sentdex.com/GBPUSD.zip (direct download).


## Motivations
This code was written following the YouTube playlist [Machine Learning for Forex and Stock analysis and algorithmic trading](https://www.youtube.com/playlist?list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO) uploaded by the YouTube channel [sentdex](https://www.youtube.com/user/sentdex), adapting it to Python 3 and performing some minor performance improvements. 
This was done as a way to get into practical machine learning after having followed the Machine Learning of the Master Degree in Computer Science at the University of Padua. 

## Requirements 
In order to run the code you need to have the following libraries and programs installed on your computer
* Python 3.6
* `numpy`
* `matplotlib`

You can install `matplotlib` by following the [matplotlib official guide](https://matplotlib.org/users/installing.html), and `numpy` following [numpy's official guide](https://docs.scipy.org/doc/numpy-1.13.0/user/install.html).

## How it works 
The program will run the following tasks
1. Take the first `end_point` (inside `settings.py`) lines of data.
2. Recognize all the different patterns of data made by `dots_for_pattern` entries each one and store them. 
3. Take `dots_for_pattern` entries that have never seen before (30 steps into the future). 
4. Recognize the patterns that are most similar to the new data. This means that
   * Each pattern must be made of points that are at least 50% similar to the corresponding point inside the new data
   * Each pattern must be overall at least `pattern_similarity_value`% similar to the new pattern
5. Save into the `patterns` folder a graph with the following data plotted inside
   * All the patterns that have been recognized, each one with a different color
   * The pattern that was been searched for, in a turquoise and thicker line
   * The predictions of the outcome of all the recognized patterns
      * A green dot for each outcome that represents a prediction of a rise
      * A red dot for each outcome that predicts a fall 
   * The average predicted outcome value as a blue dot
   * The real outcome value as a turquoise dot
 6. Increment by one the considered set of data and repat from point (1).
 
 ## Collaborating 
 I'm open to all kinds of improvements that can be possibily made, as long as they are submitted using well-documented pull requests.
 
 ## License
 ```
Copyright 2018 Riccardo Montagnin.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
