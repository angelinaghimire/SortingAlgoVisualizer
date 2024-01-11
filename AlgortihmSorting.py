import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def bubble_sort_visualizer(arr, current_step, current_comparison):
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                render(arr)
                pygame.time.delay(10)

        if not swapped:
            break

    render(arr)
    pygame.time.delay(50)
    

def merge_sort_visualizer(arr, original_array, current_step, current_comparison, left_bound=0, right_bound=None):
    if right_bound is None:
        right_bound = len(arr)

    if right_bound - left_bound > 1:
        mid = (left_bound + right_bound) // 2
        left_half = arr[left_bound:mid]
        right_half = arr[mid:right_bound]

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[left_bound + k] = left_half[i]
                i += 1
            else:
                arr[left_bound + k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[left_bound + k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[left_bound + k] = right_half[j]
            j += 1
            k += 1

        render(arr)
        pygame.time.delay(50)  

        merge_sort_visualizer(arr, original_array, current_step, current_comparison, left_bound, mid)
        merge_sort_visualizer(arr, original_array, current_step, current_comparison, mid, right_bound)

        if right_bound - left_bound == len(original_array):
            render(arr)
            pygame.time.delay(100)  


def quick_sort_partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            render(arr)
            pygame.time.delay(10)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    render(arr)
    pygame.time.delay(10)

    return i + 1

def quick_sort_recursive(arr, low, high):
    if low < high:
        partition_index = quick_sort_partition(arr, low, high)
        quick_sort_recursive(arr, low, partition_index - 1)
        quick_sort_recursive(arr, partition_index + 1, high)

def quick_sort_visualizer(arr, current_step, current_comparison):
    quick_sort_recursive(arr, 0, len(arr) - 1)
    render(arr)
    pygame.time.delay(50)


def render(arr):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluOrtho2D(0, len(arr), 0, 1) 

    colors = [
        (1.0, 0.8, 0.8),
        (1.0, 0.9, 0.7),
        (0.9, 1.0, 0.9),
        (0.8, 0.8, 1.0),
        (1.0, 0.8, 1.0),
        (0.9, 1.0, 1.0),
        (1.0, 1.0, 0.8),
        (1.0, 0.8, 0.9),
    ]

    for i, value in enumerate(arr):
        color = colors[i % len(colors)]
        border_color = (0.0, 0.0, 0.0)

        glBegin(GL_QUADS)
        glColor3f(*color)
        glVertex2f(i, 0)
        glVertex2f(i + 1, 0)
        glVertex2f(i + 1, value)
        glVertex2f(i, value)
        glEnd()

        glLineWidth(2.0)
        glBegin(GL_LINE_LOOP)
        glColor3f(*border_color)
        glVertex2f(i, 0)
        glVertex2f(i + 1, 0)
        glVertex2f(i + 1, value)
        glVertex2f(i, value)
        glEnd()

    pygame.display.flip()

def landing_page():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(0, display[0], 0, display[1])

    font = pygame.font.SysFont('Arial', 24)
    instructions = [
        "Sorting Algorithm Visualizer by Angelina Ghimire",
        "Choose a sorting algorithm",
        "1. Bubble Sort",
        "2. Merge Sort", 
        "3. Quick Sort",
        "Press 'b', 'q' or 'm' to select and algorithm"
        "by Angelina Ghimire"
    ]

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return bubble_sort_visualizer
                elif event.key == pygame.K_m:
                    return merge_sort_visualizer
                elif event.key == pygame.K_q:
                    return quick_sort_visualizer
                elif event.key == pygame.K_r:
                    return None

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        for i, line in enumerate(instructions):
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(display[0] // 2, 100 + i * 30))
            pygame.display.get_surface().blit(text_surface, text_rect.topleft)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    landing_page()



def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 0.95, 0.95, 1.0)

    original_array = [0.2, 0.6, 0.4, 0.8, 0.3, 0.7, 0.1, 0.5, 0.9, 0.2, 0.7, 0.4, 0.5, 0.8, 0.3, 0.6, 0.1, 0.9, 0.4, 0.7, 0.2, 0.6, 0.4, 0.8, 0.3, 0.7, 0.1, 0.5, 0.9, 0.2, 0.7, 0.4, 0.5, 0.8, 0.3, 0.6, 0.1, 0.9, 0.4, 0.7,0.2, 0.6, 0.4, 0.8, 0.3, 0.7, 0.1, 0.5, 0.9, 0.2, 0.7, 0.4, 0.5, 0.8, 0.3, 0.6, 0.1, 0.9, 0.4, 0.7, 0.2, 0.6, 0.4, 0.8, 0.3, 0.7, 0.1, 0.5, 0.9, 0.2, 0.7, 0.4, 0.5, 0.8, 0.3, 0.6, 0.1, 0.9, 0.4, 0.7,0.1 ]

    array_to_sort_bubble = original_array.copy()
    array_to_sort_merge = original_array.copy()
    array_to_sort_quick = original_array.copy()

    current_step_quick = 0
    current_comparison_quick = 0
    current_step_bubble = 0
    current_comparison_bubble = 0
    current_step_merge = 0
    current_comparison_merge = 0
    chosen_algorithm = None

    clock = pygame.time.Clock()  

    while True:
        if chosen_algorithm is None:
            chosen_algorithm = landing_page()

            if chosen_algorithm:
                print(f"Selected {chosen_algorithm.__name__.replace('_visualizer', '').title()} Sort")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    chosen_algorithm = None

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        if chosen_algorithm:
            if chosen_algorithm == bubble_sort_visualizer:
                chosen_algorithm(array_to_sort_bubble, current_step_bubble, current_comparison_bubble)
                current_step_bubble += 1
            elif chosen_algorithm == merge_sort_visualizer:
                chosen_algorithm(array_to_sort_merge, original_array, current_step_merge, current_comparison_merge)
                current_step_merge += 1
            elif chosen_algorithm == quick_sort_visualizer:
                chosen_algorithm(array_to_sort_quick, current_step_quick, current_comparison_quick)
                current_step_quick += 1

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()