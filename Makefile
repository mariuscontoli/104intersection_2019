##
## EPITECH PROJECT, 2019
## makefile
## File description:
## makefile for 104intersection
##

NAME	=	104intersection

SRC	=	104intersection.py

all:	$(NAME)

$(NAME): $(SRC)
	mv 104intersection.py 104intersection
	chmod +x 104intersection

clean:
	chmod -x 104intersection
	mv 104intersection 104intersection.py

fclean: clean

re: fclean all

.PHONY: all test clean