import pygame
import random
import time

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 60
AVATAR_WIDTH, AVATAR_HEIGHT = 50, 50
TILE_WIDTH, TILE_HEIGHT = 200, 50
ANSWER_BOX_HEIGHT = 60
FONT = pygame.font.SysFont("Arial", 30)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (211, 211, 211)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Quiz Game")

# Initialize the leaderboard
leaderboard = []

# Define Avatar class
class Avatar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((AVATAR_WIDTH, AVATAR_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - AVATAR_HEIGHT - 10)
        self.velocity = 0
        self.on_ground = False

    def update(self):
        # Avatar movement (left, right)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Gravity effect
        if not self.on_ground:
            self.velocity += 1  # Gravity
        else:
            self.velocity = 0
        
        self.rect.y += self.velocity

        # Prevent avatar from going below the ground level
        if self.rect.y > HEIGHT - AVATAR_HEIGHT - 10:
            self.rect.y = HEIGHT - AVATAR_HEIGHT - 10
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.velocity = -15
            self.on_ground = False


# Define Answer class
class Answer:
    def __init__(self, text, x, y, is_correct=False):
        self.text = text
        self.rect = pygame.Rect(x, y, TILE_WIDTH, TILE_HEIGHT)
        self.is_correct = is_correct

    def draw(self, screen):
        color = GREEN if self.is_correct else LIGHT_GRAY
        pygame.draw.rect(screen, color, self.rect)
        text_surface = FONT.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))


# Function to generate a new question
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2
    wrong_answers = [correct_answer + random.randint(-5, 5) for _ in range(2)]
    answers = [correct_answer] + wrong_answers
    random.shuffle(answers)
    return num1, num2, answers


# Function to initialize the leaderboard
def initialize_leaderboard():
    # This could load from a file or initialize an empty list
    global leaderboard
    leaderboard = []  # Example: Load an existing leaderboard or create an empty list
    pass

# Function to add a score to the leaderboard
def add_to_leaderboard(player_name, score):
    global leaderboard
    leaderboard.append((player_name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)  # Sort leaderboard by score (high to low)
    if len(leaderboard) > 10:  # Limit leaderboard to top 10 scores
        leaderboard = leaderboard[:10]

# Function to display the leaderboard
def display_leaderboard():
    y_position = 100
    for name, score in leaderboard:
        leaderboard_surface = FONT.render(f"{name}: {score}", True, BLACK)
        screen.blit(leaderboard_surface, (WIDTH // 2 - leaderboard_surface.get_width() // 2, y_position))
        y_position += 40

# Function to save the leaderboard
def save_leaderboard():
    # Implement saving to a file (e.g., JSON, CSV)
    pass

# Function to load the leaderboard
def load_leaderboard():
    # Implement loading from a file
    pass

# Function to show the game over screen and leaderboard
def show_game_over_screen(player_name, score):
    screen.fill(WHITE)
    game_over_surface = FONT.render("Game Over!", True, BLACK)
    screen.blit(game_over_surface, (WIDTH // 2 - game_over_surface.get_width() // 2, HEIGHT // 3))
    
    # Display score and leaderboard
    score_surface = FONT.render(f"Your Score: {score}", True, BLACK)
    screen.blit(score_surface, (WIDTH // 2 - score_surface.get_width() // 2, HEIGHT // 2))
    
    display_leaderboard()
    pygame.display.flip()
    time.sleep(3)

# Main Game Loop
def game_loop():
    clock = pygame.time.Clock()
    avatar = Avatar()
    avatar_group = pygame.sprite.Group()
    avatar_group.add(avatar)

    score = 0
    player_name = "Player"  # Replace with player input functionality (e.g., ask for name)
    timer = 10
    correct_answer = None
    question_text = ""
    answers = []
    running = True
    start_time = time.time()

    # Generate the first question
    num1, num2, answers = generate_question()
    question_text = f"What is {num1} + {num2}?"
    correct_answer = answers[0]
    answer_objects = [Answer(str(ans), i * TILE_WIDTH + 100, HEIGHT - ANSWER_BOX_HEIGHT, ans == correct_answer) for i, ans in enumerate(answers)]

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                avatar.jump()

        # Countdown timer
        elapsed_time = time.time() - start_time
        timer = max(10 - int(elapsed_time), 0)
        if timer == 0:
            # Time up, reset game with a new question
            num1, num2, answers = generate_question()
            question_text = f"What is {num1} + {num2}?"
            correct_answer = answers[0]
            answer_objects = [Answer(str(ans), i * TILE_WIDTH + 100, HEIGHT - ANSWER_BOX_HEIGHT, ans == correct_answer) for i, ans in enumerate(answers)]
            start_time = time.time()

        # Draw question text
        question_surface = FONT.render(question_text, True, BLACK)
        screen.blit(question_surface, (WIDTH // 2 - question_surface.get_width() // 2, 50))

        # Draw answers
        for answer in answer_objects:
            answer.draw(screen)

        # Check for mouse click on answer
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for answer in answer_objects:
                if answer.rect.collidepoint(mouse_x, mouse_y):
                    if answer.is_correct:
                        score += 1
                        avatar.rect.y -= 50  # Move avatar up on correct answer
                        # Generate a new question after correct answer
                        num1, num2, answers = generate_question()
                        question_text = f"What is {num1} + {num2}?"
                        correct_answer = answers[0]
                        answer_objects = [Answer(str(ans), i * TILE_WIDTH + 100, HEIGHT - ANSWER_BOX_HEIGHT, ans == correct_answer) for i, ans in enumerate(answers)]
                        start_time = time.time()  # Reset timer
                    else:
                        score -= 1

        # Update and draw avatar
        avatar_group.update()
        avatar_group.draw(screen)

        # Draw score
        score_surface = FONT.render(f"Score: {score}", True, BLACK)
        screen.blit(score_surface, (10, 10))

        # Draw timer
        timer_surface = FONT.render(f"Time: {timer}s", True, BLACK)
        screen.blit(timer_surface, (WIDTH - 100, 10))

        # End the game if the score is 0 or less
        if score <= 0:
            add_to_leaderboard(player_name, score)
            show_game_over_screen(player_name, score)
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Start the game
game_loop()
