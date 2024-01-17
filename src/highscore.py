"""
This module contains a HighScore class used for managing high scores in a game.
"""

class HighScore:
    """
    This class is used for managing high scores in a game.
    It reads and writes high scores to a file.
    """
    def __init__(self):
        self.file_path = "highscore.txt"

    def get_high_scores(self):
        """
        This method reads the high scores from a file and returns them as a list of integers.
        If the file does not exist, it returns an empty list.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                scores = file.readlines()
            return [int(score.strip()) for score in scores]
        except FileNotFoundError:
            return []

    def add_score(self, user_score):
        """
        This method adds a user's score to the high scores list, sorts the list in descending order,
        and writes the top 5 scores to the file. 
        It returns True if the user's score is in the top 5.
        """
        scores = self.get_high_scores()
        scores.append(user_score)
        scores.sort(reverse=True)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            for score in scores[:5]:  # Keep only top 5 scores
                file.write(str(score) + '\n')

        if user_score in self.get_high_scores():
            return True
        return False
