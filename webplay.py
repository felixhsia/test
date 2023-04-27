# Initialize the pygame library
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Set the background color
screen.fill((0, 0, 0))

# Create the paddle
paddle = pygame.Rect(200, 500, 100, 20)

# Create the ball
ball = pygame.Rect(300, 200, 20, 20)

# Set the ball's velocity
ball_velocity = (5, 5)

# Create the bricks
bricks = []
for i in range(10):
    for j in range(10):
        bricks.append(pygame.Rect(20 + i * 100, 20 + j * 20, 100, 20))

# Start the main loop
while True:
    # Check for events
    for event in pygame.event.get():
        # If the user quits, exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # If the user presses the left arrow key, move the paddle left
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            paddle.x -= 10

        # If the user presses the right arrow key, move the paddle right
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            paddle.x += 10

    # Move the ball
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # Check if the ball hit the top or bottom of the screen
    if ball.y < 0 or ball.y > 600:
        ball_velocity[1] *= -1

    # Check if the ball hit the paddle
    if ball.colliderect(paddle):
        ball_velocity[0] *= -1

    # Check if the ball hit a brick
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_velocity[0] *= -1

    # Draw the paddle
    pygame.draw.rect(screen, (255, 255, 255), paddle)

    # Draw the ball
    pygame.draw.circle(screen, (255, 0, 0), ball.center, 10)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, (255, 0, 0), brick)

    # Update the display
    pygame.display.update()