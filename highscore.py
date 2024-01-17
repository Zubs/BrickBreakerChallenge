class HighScore:
    def __init__(self):
        self.file_path = "highscore.txt"

    def get_high_scores(self):
        try:
            with open(self.file_path, 'r') as file:
                scores = file.readlines()
            return [int(score.strip()) for score in scores]
        except FileNotFoundError:
            return []

    def add_score(self, score):
        scores = self.get_high_scores()
        scores.append(score)
        scores.sort(reverse=True)
        with open(self.file_path, 'w') as file:
            for score in scores[:10]:  # Keep only top 10 scores
                file.write(str(score) + '\n')

        if score in self.get_high_scores():
            return True
        return False
