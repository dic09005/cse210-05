###This is Sariah's part


 def __init__(self_two):

        super().__init__()

        self_two._points = 0

        self_two.add_points(0)



    def add_points(self, self_two, points):

        """Adds the given points to the score's total points.

       

        Args:

            points (int): The points to add.

        """

        self._points += points

        self_two._points += points

        self.set_text(f"Score: {self._points} + {self_two._points}")


        