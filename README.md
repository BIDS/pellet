# pellet
Investigating Pill Recognition Methods for a new National Library of Medicine Image Dataset

###How did it started?
With a NIH RFI for the PIR Pilot - more at http://pir.nlm.nih.gov/pilot/instructions.html

###Where are we now?
We are able to create masks using the reference (DR) dataset, on the way to extract features and identify how well we are clustering the datasets based on classes.txt, which contains the labels of the image and the class it belong to.

###Where are we going?
After identifying classes, we can tailor recognition based on the type of pellet we are dealing with. Why is it important?
- tablets may or may not have inscriptions, most of the time they are very simple (1-3 chars) but will never be black, and they will always present just one color;
- capsules may or may not have inscriptions, when it happens it is black, and they may have more than one color;
- more prior coming up.

###Why should you join us?
We are generating image processing workflows for pills that could be easily extended to other images such as particles, cells, physical phenomenon as aurora, etc. Come aboard!

###Current team:
- Dani Ushizima 
- Stefan van der Valt
