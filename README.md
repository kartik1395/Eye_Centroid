# Eye_Centroid
 
## SETUP
1. Open cmd on windows and create a virtual env using ```python -m venv \path\to\env```
2. Activate your env using ```.\path\to\env\Scripts\activate```
3. Install the necessary libraries using 
```
pip install opencv-python
pip install numpy
```
4. Clone this repo using ```git clone https://github.com/kartik1395/Eye_Centroid.git```

## Running the code
1. Open cmd and go to the location of the repo.
2. Run the code using ``` python eye_centroid.py --video \path\to\video```
3. The video should be displayed with the Eye Tracking in place.
4. Press "p" to pause/play the video.
5. Press "q" to exit the video.


## Explanation 
Assumptions are made based on the videos in the folder 'daniel-ir'.
1. The first thing we do is convert the frame to grayscale for better results.
2. Then we use haarcascade for eyes provided by opencv to extract the ROI.
3. We expand the ROI by a few pixels to get a better result.
3. Once we have the ROI i.e the eyes, we use HoughCircles method to extract the pupil and the centroid.
5. The parameters of the HoughCircles method were tuned to detect the pupils and centroid thoroughly. The min and max radius has been set according to the sample videos provided.

## Additional Points
1. There is a frame counter on the original video.
2. Once an eye is detected, it is displayed in a separate window for visualisation. 
3. There is play/pause control using "p".
