# top-10-movies
- Project was made using Python,PHP, and MySql, this project webscrapes from IMBD and collects only the top 10 movies of all time which include the name,year it was made, and a picture of the movie itself. I then take the top 10 movies and store them in a database, so that if the top 10 were to change then the database can be updated and the changes can be made accordingly, I then use PHP to create the frontend part of the website by accessing the database that I made and putting them into the html elements
- Anyone may try to recreate this project just download the code and create a database so that you can store the info with the given info below, you may recreate using xammp with phpmyadmin
- CREATE DATABASE demo;
- CREATE TABLE movies(
	id INT NOT NULL,
	title VARCHAR(255),
	year int,
	img VARCHAR(255),
	PRIMARY KEY(id)
);
