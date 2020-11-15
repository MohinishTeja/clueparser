# clueparser
## Inspiration
Forensic experts often find it difficult to extract information from different kinds of raw data. This raw data is often old and so big in amounts that we can't understand. It is so important to filter out the waste information from this data and get the useful information out.  
## What it does
We have built mainly 4 tools. They mainly help us in image reconstruction and filteration. Another main tool helps us to filter the useful data from Blockchain client nodes(Ganache). 

1) Image reconstructer takes in old and blurry images and gives out clear pictures.
2) Image filter takes in pictures and gives out images with special blurry filters or any other filters we want.
3) Block logger takes in huge log files of Ganache app and gives out the main events details.
4) Steganagrpaher takes in images and stores information inside them or reveal any information hidden inside them.
## How I built it
We built these tools using mainly Python. We have even used some ML models to train usnig log files and find a suitable approach. IPFS is used for comparing Hashes of images.

## Challenges I ran into
Parsing log files is very big task for us as we didn't have any experience in it. We have run into many troubles to get out the useful information out of log files. 
## Accomplishments that I'm proud of
We are very proud of building these tools. These can be used in real-life scenarios readily. Image reconstructer turned out to be very useful as it transformed entire blurry,useless image into clear,useful image.
## What I learned
We have learned a lot about python and image classification and filteration techniques. Parsing is a hectic task and we have completed it successfully which is a big learning experience for us.

## What's next for Clue Parser
We would like to continue this project with object detection in images as well. This adds to overall usefullness of our tools for people to use.
