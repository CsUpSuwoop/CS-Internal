"# CS-Internal"  

**** Major change/code update log ****
**************************************
1. Worked on code from dates 10/06/22 to 14/06/22, committed code onto github for the 2nd time ever. From the 10th to the 12th I created all my labels, entry boxes and buttons. From the 12th to the 14th I worked on making my functions for my buttons.
2. 14/06/2022 7.30pm - Accidentally deleted committed code file
3. 14/06/2022 7.42pm - Re-commited code file onto github. Continued to build on my print_details function by adding a procedure where all the details that are entered in the entry boxes, print when the print button gets clicked, but if u fill the entry boxes out, then click the append button, then click the print button, nothing gets printed because of no information being in the entry boxes. Added a commented list of changes that need to be made in order to complete my code.
4. 14/06/2022 10.07pm - Deleted commited code file, RE-committed code file on to github. Editted check_inputs function to hide the error messages when the details have been entered into the entry box.
5. 17/06/2022 between 8.50 am and 10:20am - Editted code so that everytime the code ran, there would be no 'List Index out of range' error messages in the idle shell. I fixed this by changing the value of 'total_entries' from 10 (total_entries = 10) to (total_entries = 0), and by also changing the append_details function for the total_entries variable from (total_entries -= 1) to (total_entries += 1). 
6. 20/06/2022 6.45pm to 7.20pm - Worked on setting up delete row function, first changed all the 'main_window's to 'root', then globalled my 'total_entries' variable and 'name_count' variable and then changed the last command in line 84 'print_customer_details' to my actual function that prints all the details called 'print_details'. 
7. 22/06/2022 3.46pm - Completed coding for delete row function, and the delete row function is now fully functional.
8. 24/06/2022 4.30pm - Found out that my check inputs function did not completly work. Even if the requiremnts were not being met, the details would still get appended and printed, so I added on to the function where, the details would only append and print, if the detail requirements were met. Also added a feature where the user cannot enter a letter into the reciept number, if there is a letter in the reciept number, an error message pops up, and all none of the details will be able to be appended or printed.
9. 25/06/22 2.50pm - Added details, like file creation date and the author's name in comments, and also a to-do list of all the things i need to add in order for my code to be completed.
10. 27/06/22 3.54pm - Fixed input checker problem, before the changes i made, if the customer entered a number that was less than zero eg. -55, or a number that was greater than 500, eg. 505 or 60000, and then if the append button was clicked, no error message would pop up, but the values would not append either which was good. In the changes i have made, i have made it so that if a number greater than 500 or a number less than 0 is entered and the append button is clicked, a error message does pop up now.
11. 28/06/22 3.06pm - Added extra feature to the input checker, the user must enter their full name, if only one name is entered, an error message pops up, if the full name is entered then the programme will be able to continue. However the extra name is represented by just a space, if the user only enters one name, and presses the space bar, it will count as the full name.
12. 3/07/22 5.15pm - Added another extra feature to the input checker, the user cannot enter any integers into the 'item hired' entry box, doing so will pop up an error message instructing them to only enter strings, in order for the code to continue.


