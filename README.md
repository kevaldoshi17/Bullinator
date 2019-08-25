# Bullinator
Hack for Hack-a-bull 2019!

## Inspiration
One of the major problems that US school kids face nowadays is **Bullying!** The national data resulted from a survey conducted by stopbullying.gov shows that 28% of U.S. students in grades 6 –12 experienced bullying & 20% of U.S. students in grades 9 –12 experienced bullying. Approximately 30% of young people admit to bullying others in surveys and 70.6% of young people say they have seen bullying in their schools.

Hence, we tried to figure out that if people know about bullying incidence taking place then why there is no appropriate action being taken against it? Counselors in school try to figure out constantly how to stop bullying and help the victim. The major issue with bullying case is that victim is too scared to talk about it to either counselor or parents. There is lack of proof and evidence which prevents any actions against the bullies. 

Thus, we decided to make a hardware network system that detects such incidences and show who is bully and who is victim to the people who should know like counselors, headmasters, principals etc. It's a voice recognition system and tries to prevent bullying keeping in mind that we still need to follow privacy regulations which is the reason why video recording and camera surveillance need prior approval before installation. 

## What it does
It's a voice recognition system which detects the voice in a given environment. It determines if the conversation between two individuals is toxic. Once enough toxicity is discovered, it runs the data on backend and reveals the information such as the name of bully, the victim, the location where the incidence occurred etc. The data is visualized on a website and only counselors and authorities have access to see the information. The data visualization will help them see the severity and toxicity of the incidence and will compel them to take necessary actions before it escalates.  

## How we built it

We used Qualcomm's Dragonboard snapdragon 410C board as a hardware system. There is a mic installed which detects and record the voice. The recorded voice then is ran in the backend which is a python based program. Using the Google Voice recognition and the recorded data of subjects, it detects the important tags like who is bully, victim and place. The data in a JSON format is then provided to the display website where the visualization helps the spectator to analyze the situation and take appropriate action. 

## Challenges we ran into

The dragonboard didn't had any microphone port so it was quite difficult to install drivers. The dragonboard does not have enough graphical interface support and has network connectivity issues. Although we were able to create a working system but it was quite difficult to reach there. 

## Accomplishments that we're proud of

In 24 hours getting familiar with new hardware. Signal processing. Creating a website. Making a hack for social good. 

## What we learned

We learned about the grave situation students face in schools. How it impacts both their personal and professional development. We learned that first step to stop bullying is recognizing that it is happening! 

## What's next for The Bullinator

We will keep working on this project and try to make it effiecient and easy to install in schools so that the bullying and hazing cases are reduced and counselors have enough data set to come up with a permanent solution for this major problem in schools. 
