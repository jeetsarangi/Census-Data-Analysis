## CS685A   Assignment 2
To run the code:<br>
Libraries required are:-<br>
· Python pandas<br>
· Python numpy<br>
· Python openpyxl<br>
· Python os<br>
· Python scipy<br>
---------------------------------------------------------------------------
Files for each question:<br>
Question1:<br>
Code/scripts : Question1.py,percent-india.sh<br>
Libraries:pandas,openpyxl,numpy<br>
Data files:<br>
 DDW-C18-0000.xlsx,DDW_PCA0000_2011_Indiastatedist.xlsx<br>
Output:percent-india.csv<br>

Question2:<br>
Code/scripts : Question2.py,gender-india.sh<br>
Libraries:pandas, openpyxl,scipy<br>
Data files:<br>
DDW-C18-0000.xlsx,DDW_PCA0000_2011_Indiastatedist.xlsx<br>
Output:gender-india-a.csv, gender-india-b.csv, gender-india-c.csv<br>
(a-monolingual,b-bilingual,c-trilingual)<br>

Question3:<br>
Code/scripts : Question3.py,geography-india.sh<br>
Libraries:pandas,openpyxl,scipy<br>
Data files:<br>
DDW-C18-0000.xlsx,DDW_PCA0000_2011_Indiastatedist.xlsx<br>
Output:<br>
geography-india-a.csv, geography-india-b.csv<br>
, geography-india-c.csv<br>
(a-monolingual,b-bilingual,c-trilingual)<br>

Question4a:<br>
Code/scripts : Question4a.py,3-to-2-ratio.sh<br>
Libraries:pandas,openpyxl,numpy<br>
Data files:<br>
DDW-C18-0000.xlsx,DDW_PCA0000_2011_Indiastatedist.xlsx<br>
Output:<br>
3-to-2-ratio.csv<br>

Question4b:<br>
Code/scripts : Question4b.py,2-to-1-ratio.sh<br>
Libraries:pandas,openpyxl,numpy<br>
Data files:<br>
DDW-C18-0000.xlsx,DDW_PCA0000_2011_Indiastatedist.xlsx<br>
Output:<br>
2-to-1-ratio.csv<br>

Question5:<br>
Code/scripts : Question5.py,age-india.sh<br>
Libraries:pandas,openpyxl,numpy<br>
Data files:<br>
DDW-C18-0000.xlsx, DDW-0000C-14.xls<br>
Output:age-india.csv<br>

Question6:
Code/scripts : Question6.py,literacy-india.sh
Libraries:pandas,openpyxl,numpy
Data files:
DDW-0000C-08.xlsx, DDW-C19-0000.xlsx
Output:literacy-india.csv

Question7:
Code/scripts : Question7.py,region-india.sh
Libraries:pandas,openpyxl,numpy,os
Data files:Question7data(folder includes all so just copy the whole folder)
Output:region-india-a.csv,region-india-b.csv
(a-only mother tongue,b-mother tongue+2nd language+3rd language)

Question8:
Code/scripts : Question8.py,age-gender.sh
Libraries:pandas,openpyxl
Data files: DDW-0000C-14.xls, DDW-C18-0000.xlsx
Output:age-gender-a.csv,age-gender- b.csv,age-gender-c.csv
(a-trilingual,b-bilingual,c-monolingual)

Question9:
Code/scripts : Question9.py,literacy-gender.sh
Libraries:pandas,openpyxl
Data files: DDW-0000C-08.xlsx, DDW-C19-0000.xlsx
Output:literacy-gender-a.csv,literacy-gender-b.csv,literacy-gender-c.csv
(a-trilingual,b-bilingual,c-monolingual)

How to run:
· Load the script and code files for respective question on same folder.
· Load the respective data files as mentioned above for that question.
· Make sure you have the respective libraries to give the environment.
· Run using the .sh file for respective question.
e.g : ./assign2.sh
· assign2.sh is the main shell to run all the .sh files in one go.

-------------------------------------------------------------------------
Question2:
Uttar Pradesh(09) has p-value of 0.23 which is the lowest amongest all states
then comes Rajasthan(08) having p-value of 0.26 making it second lowest and 
lastly Uttarakhand(05) has the third lowest.Hence these three are having the most
different ratios than the original males:female ratio.
