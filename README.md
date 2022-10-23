# World-of-Tanks-drive-assistant<br>

![maxresdefault](https://user-images.githubusercontent.com/49094051/197392749-d70dd82f-91de-4287-b62e-865d267b009a.jpg)
world of tanks UI

World of Tanks is a free MMo where you are driving the most iconic tanks in the history. Here I propose a project providing an automatic driving assistant powered by a deep CNN which take a look at the minimap and drives the tank towards the placeholder.<br>

![387de88a-520f-11ed-88e2-64bc580216eb](https://user-images.githubusercontent.com/49094051/197392459-072d7c3e-e87d-4e78-a034-ae9df47477d4.jpg)

The idea is pretty simple:<br>
 1) Capture gameplay (frames and keys) (capture_frames.py) <br>
 2) Train an end-to-end CNN to take frames as inputs and returns commands as outputs (TF_pipeline_wot)<br>
 3) Use the Model to command a tank in real time (Play.py)<br>
 
 While the idea was simple I soon encountered many challenges:<br>
 - capture multiple keys at the same time<br>
 - converting .txt files in hot-one encoded labels and making the y dataset <br>
 - class imbalances (fixed with data augmentation and balancing scripts). These solutions are the best I could came up with but 'unfortunately' they require much gameplay to be collected
 
problems and how to solve them:
 - capture the EXACT minimap square. with some tries can be done but remember to adjust the pipeline process
 - the model requires a lot of positive examples (5 - 6 000 pairs) to perform nicely;
 - many hyper parameters to be chosen that affect training process and control experience. The learning rate was set at 1e-5 but some in some iterations the model could not learn; while controlling the tank the output 
 - the actual model deployment it's not smooth since you'll need to play WoT in a windowed mode. This is due some incompatibility with Thread processes. In theory the problem could be solved by NOT using thread at all baut this would require re-writing most of the code with different modules and functions
 - it's not a Reinforcement Learning approach which is the best approach for agent-control problems (but the game is complex and it would require much more training) but it's on the to-do list ;)
