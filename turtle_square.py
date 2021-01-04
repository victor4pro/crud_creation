import turtle


def square():
	window = turtle.Screen()
	tortuga = turtle.Turtle()

	tortuga.forward(100)
	tortuga.left(90)
	tortuga.forward(100)
	tortuga.left(90)
	tortuga.forward(100)
	tortuga.left(90)
	tortuga.forward(100)
	window.mainloop()

if __name__ == '__main__':
	square()
